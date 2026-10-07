# -*- coding: utf-8 -*-
"""Вырезание товара с белого студийного фона -> RGBA. Запуск: python cutout.py
Фон белый (≈254), под товаром мягкая серая тень. Алгоритм:
1) «фоновые» пиксели = светлые и малонасыщенные; берём те, что связаны с краем кадра (заливка);
2) тень убираем вторым, более мягким порогом, но только вокруг основания (снизу), чтобы не съесть белые грани корпуса;
3) границу сглаживаем: небольшая эрозия + растушёвка альфы, «обесцвечиваем» белый ореол по краю."""
import pathlib

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi

ROOT = pathlib.Path(__file__).parent


def cutout(src, bright=198, sat_thr=22, grad_thr=7.0):
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.float32)
    mn, mx = a.min(2), a.max(2)
    sat = mx - mn
    h, w = mn.shape
    gray = ndi.gaussian_filter(a.mean(2), 0.8)
    gx = ndi.sobel(gray, axis=1) / 8.0
    gy = ndi.sobel(gray, axis=0) / 8.0
    grad = np.hypot(gx, gy)
    # фон и тень: светлые, бесцветные и «плавные» (без чётких контуров); контур товара — барьер
    cand = (mn >= bright) & (sat <= sat_thr) & (grad < grad_thr)
    lab, n = ndi.label(cand)
    edge_labels = set(np.unique(np.concatenate([lab[0, :], lab[-1, :], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(edge_labels))
    # чистый белый фон всегда фон (даже если он отрезан барьером от края)
    bg |= (mn >= 250) & (sat <= 6) & ndi.binary_dilation(bg, iterations=2)
    obj = ~bg
    # контур: пара пикселей барьера по краю принадлежит товару, но не больше
    lab3, n3 = ndi.label(obj)
    if n3 > 1:
        sizes = ndi.sum(obj, lab3, range(1, n3 + 1))
        obj = lab3 == (1 + int(np.argmax(sizes)))
    obj = ndi.binary_opening(obj, iterations=1)
    obj = ndi.binary_fill_holes(obj)
    m = ndi.binary_erosion(obj, iterations=1)
    alpha = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0))
    rgb = a.copy()
    al = np.asarray(alpha).astype(np.float32) / 255.0
    inner = ndi.binary_erosion(m, iterations=3)
    idx = ndi.distance_transform_edt(~inner, return_distances=False, return_indices=True)
    fill = rgb[idx[0], idx[1]]
    edge = (al > 0) & (al < 1)
    rgb[edge] = fill[edge]
    res = Image.fromarray(np.dstack([rgb, al * 255]).astype(np.uint8), "RGBA")
    bbox = res.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        pad = 12
        res = res.crop((max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(w, bbox[2] + pad), min(h, bbox[3] + pad)))
    return res


if __name__ == "__main__":
    import sys
    from catalog import EX_PHOTO_SRC
    out = ROOT / "assets" / "cut"
    out.mkdir(exist_ok=True)
    only = sys.argv[1:]
    for m, f in EX_PHOTO_SRC.items():
        if only and m not in only:
            continue
        cutout(ROOT / "assets" / "exegate" / f).save(out / f"ex-{m}.png")
        print("cut", m)
