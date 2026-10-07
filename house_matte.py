# -*- coding: utf-8 -*-
"""Качественное вырезание дома с чисто белого фона (альфа-матирование «обратным смешиванием»).
Пиксель на краю кроны = α·F + (1-α)·255. Цвет листвы F восстанавливаем по ближайшей «чисто листвяной» области,
отсюда α и F без белой каймы. Жёсткие объекты (стены, плита участка) режем по маске."""
import pathlib

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi

ROOT = pathlib.Path(__file__).parent


def matte(src, out_png):
    im = Image.open(src).convert("RGB")
    rgb = np.asarray(im).astype(np.float32)
    mn = rgb.min(2)
    mx = rgb.max(2)
    sat = mx - mn
    h, w = mn.shape

    # 1. маска объекта: всё, что не белый фон; белые просветы внутри (между кроной и стеной) считаем фоном
    nonwhite = (mn < 250) | (sat > 10)
    lab, n = ndi.label(ndi.binary_closing(nonwhite, iterations=2))
    sizes = ndi.sum(nonwhite, lab, range(1, n + 1))
    obj = lab == (1 + int(np.argmax(sizes)))
    white = (mn >= 249) & (sat <= 6)
    wl, wn = ndi.label(white)
    wsz = ndi.sum(white, wl, range(1, wn + 1))
    gaps = np.isin(wl, [i + 1 for i, s in enumerate(wsz) if s > 90])
    obj &= ~gaps
    obj = ndi.binary_opening(obj, iterations=1)

    # 2. «уверенный» передний план и цвет листвы рядом
    sure = ndi.binary_erosion(obj, iterations=4) & ~ndi.binary_dilation(gaps, iterations=2)
    sure_f = sure.astype(np.float32)
    mn_fg = ndi.gaussian_filter(mn * sure_f, 4) / np.maximum(ndi.gaussian_filter(sure_f, 4), 1e-3)
    idx = ndi.distance_transform_edt(~sure, return_distances=False, return_indices=True)
    fmin = mn_fg[idx[0], idx[1]]            # «темнота» ближайшего уверенного пикселя
    fcol = rgb[idx[0], idx[1]]               # цвет ближайшего уверенного пикселя (запасной)

    # 3. зона листвы: зелёно-оливковые пиксели + их окрестность
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    leaf = (G >= R - 3) & (G > B + 6) & (mn < 170)
    leaf_c = ndi.binary_closing(leaf, iterations=3)
    white_any = (mn >= 205) & (rgb[..., 1] > 0)
    # настоящий внешний фон: чисто белые области, связанные с краем кадра; зону чистки держим недалеко от него
    outer_w = (mn >= 244) & (sat <= 8)
    ol, on = ndi.label(outer_w)
    border = set(np.unique(np.concatenate([ol[0, :], ol[-1, :], ol[:, 0], ol[:, -1]]))) - {0}
    outer = np.isin(ol, list(border))
    near_outer = ndi.distance_transform_edt(~outer) < 80
    zone = ndi.binary_dilation(leaf_c, iterations=9) & ndi.binary_dilation(obj, iterations=3) & ndi.binary_dilation(white_any, iterations=8) & near_outer
    lf = leaf.astype(np.float32)
    den = np.maximum(ndi.gaussian_filter(lf, 6), 1e-4)
    leaf_rgb = np.stack([ndi.gaussian_filter(rgb[..., k] * lf, 6) / den for k in range(3)], -1)   # цвет листвы вокруг
    leaf_mn = leaf_rgb.min(2)
    fm = np.clip(leaf_mn, 20, 170)

    a_mask = np.asarray(Image.fromarray((obj * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.9))).astype(np.float32) / 255
    alpha = np.where(sure, 1.0, a_mask)
    alpha = np.where(obj & ~sure, a_mask, alpha)

    # внутри зоны листвы: чистый белый — это просвет (прозрачность), остальное разбираем смешиванием с белым
    pure_white = zone & (mn >= 226) & (sat <= 8)
    a_z = np.clip((255.0 - mn) / np.maximum(255.0 - fm, 30.0), 0, 1)
    F = (rgb - 255.0 * (1 - a_z[..., None])) / np.maximum(a_z, 0.06)[..., None]
    err = np.abs(F - leaf_rgb).mean(2)
    greenish = (G > B + 4) & (G >= R - 6)
    mixable = zone & greenish & (a_z < 0.985) & (err < 60) & (mn < 226) & (leaf_mn < 170) & (den > 3e-3)
    alpha = np.where(zone & ~pure_white, np.where(mixable, a_z, np.where(obj, 1.0, 0.0)), alpha)
    alpha = np.where(pure_white, 0.0, alpha)
    # почти белые нейтральные пиксели внутри кроны — это просветы фона, а не листья (листья жёлто-зелёные)
    near_white = zone & ~mixable & (mn >= 196) & ~pure_white
    a_nw = np.clip((255.0 - mn) / np.maximum(255.0 - fm, 60.0), 0, 1) * 0.35
    alpha = np.where(near_white, np.minimum(alpha, a_nw), alpha)
    # мелкая чистка: убираем изолированные точки и сглаживаем альфу
    alpha = np.clip(ndi.gaussian_filter(alpha, 0.6), 0, 1)
    alpha[alpha < 0.05] = 0
    F = np.clip(F, 0, 255)
    out_rgb = np.where((mixable & (alpha > 0) & (alpha < 0.985))[..., None], F, rgb)
    # 5. дефринжинг: край на 1 px внутрь, кромку красим цветом ближайшей «твёрдой» листвы/стены
    alpha = ndi.minimum_filter(alpha, size=3)
    alpha = np.clip(ndi.gaussian_filter(alpha, 0.5) * 1.06, 0, 1)
    alpha[alpha < 0.06] = 0
    solid = alpha >= 0.92
    idx2 = ndi.distance_transform_edt(~solid, return_distances=False, return_indices=True)
    near = out_rgb[idx2[0], idx2[1]]
    edge = (alpha > 0) & (alpha < 0.92)
    out_rgb = np.where(edge[..., None], near, out_rgb)
    # остатки белого фона: светлые пиксели в зоне листвы и на любой полупрозрачной кромке убираем совсем
    alpha = np.where(zone & (out_rgb.min(2) >= 214), 0.0, alpha)
    alpha = np.where((alpha < 0.97) & (out_rgb.min(2) >= 232) & (sat <= 10), 0.0, alpha)
    # светлые пиксели у кромки (остатки белого фона) делаем ещё прозрачнее
    bright = (out_rgb.min(2) > 205) & (alpha < 0.98) & (alpha > 0)
    alpha = np.where(bright, alpha * 0.5, alpha)
    # крупные нейтрально-серые поверхности (плита участка, перекрытия, парапеты) защищаем от чистки листвы
    neutral = (sat <= 9) & (mn >= 120) & (mn <= 232)
    nl, nn = ndi.label(neutral)
    nsz = ndi.sum(neutral, nl, range(1, nn + 1))
    prot = np.isin(nl, [i + 1 for i, v in enumerate(nsz) if v > 2500])
    prot = ndi.binary_closing(prot, iterations=2) & ndi.binary_dilation(obj, iterations=1)
    alpha = np.where(prot, np.maximum(alpha, 1.0), alpha)
    out_rgb = np.where(prot[..., None], rgb, out_rgb)
    # вода бассейна (голубая) и её блики не трогаем: внутри объекта всегда непрозрачна
    water = ndi.binary_closing(B > R + 28, iterations=5) & ndi.binary_erosion(obj, iterations=2)
    water = ndi.binary_dilation(ndi.binary_erosion(water, iterations=2), iterations=3) & obj
    alpha = np.where(water, 1.0, alpha)
    out_rgb = np.where(water[..., None], rgb, out_rgb)
    res = Image.fromarray(np.dstack([out_rgb, alpha * 255]).astype(np.uint8), "RGBA")
    bb = res.getchannel("A").point(lambda v: 255 if v > 6 else 0).getbbox()
    res = res.crop((max(0, bb[0] - 4), max(0, bb[1] - 4), min(w, bb[2] + 4), min(h, bb[3] + 4)))
    res.save(out_png)
    return res


if __name__ == "__main__":
    r = matte(ROOT / "assets/house/house_src.png", ROOT / "assets/house/house_cut.png")
    print(r.size)
