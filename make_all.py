# -*- coding: utf-8 -*-
"""Единая сборка сайта: python make_all.py  ->  site/ и dist/oasis-site.zip
Основные адреса получают финальные «вау»-версии (без noindex, с canonical)."""
import pathlib
import re
import zipfile

import build as B
import build_beacon
import build_home
import build_cinnabar
import build_wow
import build_zephyr

ROOT = pathlib.Path(__file__).parent

PAGES = {
    "10kvt": build_beacon.render,
    "resanta": build_cinnabar.render,
    "exegate": build_zephyr.render,
    "spn-13500": build_wow.page_scope,
    "exegate-15kvt": build_wow.page_layers,
}

MOBILE_CENTER = """<style>@media(max-width:820px){
h1,h2,.lead,.sub,.eyebrow,.label,.note,.hint,.price-note,.proof,.hp-sub,.tagpill{text-align:center}
.eyebrow,.label,.hprice,.proof,.tagpill{display:flex;width:max-content;max-width:100%;margin-left:auto;margin-right:auto;justify-content:center;flex-wrap:wrap}
.eyebrow::before{display:none}
.lead,.sub,.hp-sub,.lead-box p,.deliv p,.delivery p{margin-left:auto;margin-right:auto}
.hero .cta,.hero-in .cta,.hero2 .cta,.hc .cta,.lead-bar .cta,.final .cta,.cta{flex-direction:column;align-items:stretch;justify-content:center;max-width:420px;margin-left:auto;margin-right:auto}
.cta .btn,.cta .ghost,.cta .tgb{width:100%;justify-content:center;text-align:center}
.hprice{margin-bottom:22px}
.stat,.stats{text-align:center}
.stat b{margin-left:auto;margin-right:auto}
.gc-in{align-items:center;text-align:center}.gc-bot{flex-direction:column;gap:10px;width:100%}.gc-tag{align-self:center}
.fc{text-align:center}.fc i{margin-left:auto;margin-right:auto}
.price,.card,.series{text-align:center}.price .btn{margin-left:auto;margin-right:auto}.price ul,.card ul{text-align:left}
.price .ic,.card .ic{margin-left:auto;margin-right:auto}
.lead-box,.lead-bar,.deliv,.delivery{text-align:center}.deliv h2,.delivery h2,.lead-box h2,.lead-bar h2{text-align:center}
.form-note,.form-msg{text-align:center}
.ts-info,.ac-info{text-align:center}.ts-info .ghost{margin-left:auto;margin-right:auto}.ac-info ul{text-align:left}.ac-bot{flex-direction:column;gap:12px}
.hp-tabs,.ts-tabs,.vp-chips,.cc-pres{justify-content:center}
.vp-res,.cc-right{text-align:center}.vp-res .btn{margin-left:auto;margin-right:auto}
.vp-val{justify-content:center}.vp-top{text-align:center}
.anat-hud,.anat-txt{text-align:center}.anat-dots{justify-content:center}.anat-num{text-align:center}
.hud{text-align:center}.readout{justify-content:center}.cap{margin-left:auto;margin-right:auto}
.big,.big h3,.big p{text-align:center}.stat2{text-align:center}
.step,.how div{text-align:center}.how b,.st b{margin-left:auto;margin-right:auto}.step::before{position:static;margin:0 auto 12px}.step{padding-left:0}
.tl{text-align:center}
}</style>"""


def nbsp(h):
    """Неразрывные пробелы в ценах и мощности, чтобы цена не переносилась посреди числа."""
    import re as _re
    NB = chr(160)
    h = _re.sub(r"(\d{1,3}) (\d{3}) ₽", lambda m: m.group(1) + NB + m.group(2) + NB + "₽", h)
    h = _re.sub(r"(\d{1,3}) (\d{3}) ВА", lambda m: m.group(1) + NB + m.group(2) + NB + "ВА", h)
    h = _re.sub(r"(\d) ₽", lambda m: m.group(1) + NB + "₽", h)
    h = _re.sub(r"(Цена|цена|от|до) (\d)", lambda m: m.group(1) + NB + m.group(2), h)
    h = _re.sub(r"(\d) (кВт|кВА|ВА|Вт|мс|кг|мм)(?!\w)", lambda m: m.group(1) + NB + m.group(2), h)
    return h


def finalize(html_text, slug):
    fix = "<style>@media(max-width:420px){table{table-layout:fixed}td{overflow-wrap:anywhere;word-break:break-word}th{overflow-wrap:normal;word-break:normal;hyphens:none}.ts-tb th{width:42%}.cc-grid>*,.hp-grid>*,.ts-panel>*,.vp-res>*,.g3>*{min-width:0}.hero>.wrap{width:100%;min-width:0}.cc-n{min-width:0;flex:1}.cc-row{padding-left:0;padding-right:0}}</style>"
    html_text = html_text.replace("</head>", fix + MOBILE_CENTER + "</head>", 1)
    url = f"{B.DOMAIN}/{slug}/"
    html_text = html_text.replace('<meta name="robots" content="noindex">\n', "")
    title = re.search(r"<title>(.*?)</title>", html_text, re.S).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html_text, re.S).group(1)
    extra = (f'<link rel="canonical" href="{url}">\n<meta property="og:title" content="{title}">\n'
             f'<meta property="og:description" content="{desc}">\n<meta property="og:type" content="website">\n'
             f'<meta property="og:url" content="{url}">\n')
    html_text = html_text.replace("</title>", "</title>\n" + extra, 1) if "rel=\"canonical\"" not in html_text else html_text
    return nbsp(html_text)


def main():
    B.main(pages=False)  # политика, sitemap, robots, send.php, .htaccess
    build_home.main()    # главная страница (перезаписывает простой index.html)
    root = ROOT / "site"
    for slug, fn in PAGES.items():
        d = root / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(finalize(fn(), slug), encoding="utf-8")
        print("OK", d / "index.html")
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    with zipfile.ZipFile(dist / "oasis-site.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(root.rglob("*")):
            if f.is_file() and f.name != "config.php":
                z.write(f, f.relative_to(root).as_posix())
    print("ZIP", dist / "oasis-site.zip")


if __name__ == "__main__":
    main()
