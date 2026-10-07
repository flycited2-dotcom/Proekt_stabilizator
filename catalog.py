# -*- coding: utf-8 -*-
"""Каталог проверенных данных и фото. Источники:
 Exegate — https://www.exegate.com/catalogue/stabilizer/ (карточки моделей)
 Ресанта — https://resanta.ru/category/stabilizatory-napryazheniya/filter/ponizhennogo-napryazheniya/
Цены не берём: у вас свои. Запуск `python catalog.py` оптимизирует фото из assets/ в site/img/."""
import pathlib

ROOT = pathlib.Path(__file__).parent
IMG = "/img/"  # публичный адрес картинок на сайте

# ---------------------------------------------------------------- Exegate (официальные данные)
# series: код -> (название серии, монтаж, вход В)
EX_SERIES = {
    "AS": ("Expert AS", "Напольный / настольный", "140–260"),
    "AV": ("Master AV", "Настенный / напольный", "140–260"),
    "AVS": ("Master Turbo AVS", "Настенный / напольный", "100–265"),
    "AST": ("Expert Turbo AST", "Напольный / настольный", "80–260"),
    "XV": ("Master Turbo XV", "Настенный / напольный", "80–265"),
}
# модель -> (мощность кВт, макс. ток А, подключение, габариты мм, вес кг, байпас)
EX = {
    "AS-10000": (10, 50, "клеммы 5P и 2 евророзетки", "305×335×425", "13,5", False),
    "AV-10000": (10, 50, "клеммы 5P и 2 евророзетки", "265×320×140", "10,5", False),
    "AVS-10000": (10, 50, "клеммы 5P и 2 евророзетки", "265×320×140", "12", False),
    "AST-10000": (10, 50, "клеммы 5P и 2 евророзетки", "300×300×420", "16", False),
    "XV-10000": (10, 50, "клеммы 5P и 2 евророзетки", "400×460×230", "14,4", False),
    "AS-15000": (15, 75, "клеммы 5P", "305×330×420", "16", False),
    "AV-15000": (15, 75, "клеммы 5P", "310×312×167", "20,5", True),
    "AVS-15000": (15, 75, "клеммы 5P", "310×312×167", "22", True),
    "AST-15000": (15, 75, "клеммы 4P и 2 евророзетки", "300×400×545", "23,2", True),
    "XV-15000": (15, 75, "клеммы 4P и 2 евророзетки", "450×595×290", "24,1", True),
}
# файл главного фото (из assets/exegate) для каждой модели
EX_PHOTO_SRC = {
    "AS-10000": "AS-10000_preview2e_1.jpg", "AV-10000": "AV-10000_preview2e_1.jpg", "AVS-10000": "AVS-10000_preview2e_1.jpg",
    "AST-500": "AST-500_preview2e_1.jpg", "AST-2000": "AST-2000_preview2e_1.jpg", "AVS-2000": "AVS-2000_preview2e_1.jpg",
    "AST-10000": "AST-10000_preview2e_2.jpg", "XV-10000": "XV-10000_preview2e_2.jpg",
    "AS-15000": "AS-15000_preview2e_1.jpg", "AV-15000": "AV-15000_preview2e_1.jpg", "AVS-15000": "AVS-15000_preview2e_1.jpg",
    "AST-15000": "AST-15000_preview2e_2.jpg", "XV-15000": "XV-15000_preview2e_2.jpg",
}
# дополнительные ракурсы (для галереи AS-15000 и др.)
EX_GALLERY_SRC = {
    "AS-15000": ["AS-15000_preview2_3.jpg", "AS-15000_preview2_5.jpg"],
    "AV-15000": ["AV-15000_preview2_3.jpg", "AV-15000_preview2_5.jpg"],
    "AST-15000": ["AST-15000_preview2_4.jpg", "AST-15000_preview2_5.jpg", "AST-15000_preview2_6.jpg"],
}

# ---------------------------------------------------------------- Ресанта СПН (официальные данные)
# модель -> (мощность кВт, ток А, вход В, дисплей, файл фото)
RS = {
    "СПН-900": ("0,9", "4,7", "90–260", "LED", "thumb_19880.png"),
    "СПН-3600": ("3,6", "18,9", "90–260", "LCD", "thumb_19890.png"),
    "СПН-5400": ("5,4", "28,4", "90–260", "LCD", "thumb_19900.png"),
    "СПН-8300": ("8,3", "43,7", "90–260", "LCD", "thumb_19911.png"),
    "СПН-13500": ("13,5", "71", "90–260", "LCD", "spn-13500_main.png"),
    "СПН-17000": ("17", "89,4", "90–260", "LCD", "thumb_57469.png"),
    "СПН-20000/45": ("20", "90", "45–275", "LCD", "thumb_87125.png"),
    "СПН-22500": ("22,5", "118,4", "90–260", "LCD", "thumb_57479.png"),
}
RS_GALLERY_SRC = ["spn-13500_56769.png", "spn-13500_56770.png", "spn-13500_56771.png", "spn-13500_56772.png"]


def slug(s):
    return s.lower().replace("/", "-").replace("ё", "e").replace(" ", "-")


def ex_img(model):
    return IMG + "ex-" + slug(model) + ".webp"


def rs_img(model):
    t = {"СПН": "spn"}
    return IMG + "rs-" + slug(model).replace("спн", "spn") + ".webp"


EX_WORD = {"AS": "Expert", "AV": "Master", "AVS": "Master Turbo", "AST": "Expert Turbo", "XV": "Master Turbo"}


def ex_name(model):
    return "Exegate " + EX_WORD[model.split("-")[0]] + " " + model


def ex_card(model):
    """(название, тег, пункты) для карточки модели Exegate."""
    ser, mount, vin = EX_SERIES[model.split("-")[0]]
    kw, amp, conn, size, wt, bypass = EX[model]
    items = [f"{kw} кВт, однофазный, вход {vin} В", f"Макс. ток {amp} А · {conn}", f"{size} мм · {wt} кг" + (" · байпас" if bypass else "")]
    return (ex_name(model), mount, items)


def rs_card(model):
    kw, amp, vin, disp, _ = RS[model]
    items = [f"{kw} кВт, макс. ток {amp} А", f"Вход {vin} В, выход 220 В ±8%", f"Дисплей {disp}, релейный"]
    return ("Ресанта " + model, "Пониженного напряжения", items)


# имя карточки -> путь к картинке (для всех шаблонов)
MODEL_IMG = {}
for _m in EX:
    MODEL_IMG[ex_name(_m)] = ex_img(_m)
for _m in RS:
    MODEL_IMG["Ресанта " + _m] = rs_img(_m)
# карточки серий (страница «Exegate для дома»): фото модели на 10 кВт этой серии
for _code, (_title, _mount, _vin) in EX_SERIES.items():
    MODEL_IMG[_title] = ex_img(_code + "-10000")

EX_POWER_RANGE = {"AS": "0,5–20", "AV": "0,5–20", "AVS": "0,5–20", "AST": "0,5–30", "XV": "0,5–20"}


def series_card(code):
    title, mount, vin = EX_SERIES[code]
    items = [f"Вход {vin} В, выход 220 В ±8%", f"{mount} монтаж", f"Мощность {EX_POWER_RANGE[code]} кВт, КПД 98%"]
    return (title, "Серия Exegate", items)


_SESSION = None


def _cut(path):
    """Нейросетевое вырезание (rembg/u2net) с кэшем в assets/cut; возвращает RGBA, обрезанный по контуру."""
    global _SESSION
    from PIL import Image
    cache = ROOT / "assets" / "cut" / (pathlib.Path(path).stem + ".png")
    if cache.exists():
        return Image.open(cache).convert("RGBA")
    from rembg import remove, new_session
    if _SESSION is None:
        _SESSION = new_session("u2net")
    out = remove(Image.open(path).convert("RGB"), session=_SESSION)
    bbox = out.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox()
    if bbox:
        pad = 10
        out = out.crop((max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(out.width, bbox[2] + pad), min(out.height, bbox[3] + pad)))
    cache.parent.mkdir(exist_ok=True)
    out.save(cache)
    return out


def _save(im, dst, size):
    im = im.copy()
    im.thumbnail((size, size))
    im.save(dst, "WEBP", quality=88, method=6)


def optimize():
    from PIL import Image
    out = ROOT / "site" / "img"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("ex-*.jpg"):
        old.unlink()
    n = 0
    for m, f in EX_PHOTO_SRC.items():
        _save(_cut(ROOT / "assets" / "exegate" / f), out / pathlib.Path(ex_img(m)).name, 900); n += 1
    for m, fl in EX_GALLERY_SRC.items():
        for k, f in enumerate(fl, 2):
            _save(_cut(ROOT / "assets" / "exegate" / f), out / f"ex-{slug(m)}-{k}.webp", 900); n += 1
    for m, row in RS.items():
        im = Image.open(ROOT / "assets" / "resanta" / row[4]).convert("RGBA")
        bbox = im.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox()
        if bbox:
            im = im.crop(bbox)
        _save(im, out / pathlib.Path(rs_img(m)).name, 900); n += 1
    for k, f in enumerate(RS_GALLERY_SRC, 1):
        im = Image.open(ROOT / "assets" / "resanta" / f).convert("RGBA")
        bbox = im.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox()
        if bbox:
            im = im.crop(bbox)
        _save(im, out / f"rs-spn-13500-g{k}.webp", 900); n += 1
    size = sum(p.stat().st_size for p in out.iterdir()) // 1024
    print(n, "картинок,", size, "КБ")


if __name__ == "__main__":
    optimize()


# ---------------------------------------------------------------- ЧТО ЕСТЬ НА СКЛАДЕ (цены и список задаёт владелец)
def money(v):
    return f"{v:,}".replace(",", " ") + " ₽"


STOCK = [
    dict(id="ast-500", brand="exegate", name="Exegate Expert Turbo AST-500", short="AST-500", series="AST", code="AST-500", price=3190,
         kw="0,5", va="500 ВА", vin="80–260", vout="220 В ±8%", amp="2,5", conn="1 евророзетка (Schuko)", size="120×145×220", weight="2,4",
         mount="Напольный / настольный", indic="Двойная цифровая индикация входного и выходного напряжения", bypass=False, img="/img/ex-ast-500.webp"),
    dict(id="ast-2000", brand="exegate", name="Exegate Expert Turbo AST-2000", short="AST-2000", series="AST", code="AST-2000", price=4990,
         kw="2", va="2000 ВА", vin="80–260", vout="220 В ±8%", amp="10", conn="2 евророзетки (Schuko)", size="140×170×255", weight="5,4",
         mount="Напольный / настольный", indic="Двойная цифровая индикация входного и выходного напряжения", bypass=False, img="/img/ex-ast-2000.webp"),
    dict(id="avs-2000", brand="exegate", name="Exegate Master Turbo AVS-2000", short="AVS-2000", series="AVS", code="AVS-2000", price=4990,
         kw="2", va="2000 ВА", vin="100–265", vout="220 В ±10%", amp="10", conn="2 евророзетки (Schuko)", size="430×240×120", weight="5",
         mount="Настенный", indic="Цифровая индикация входного и выходного напряжения", bypass=False, img="/img/ex-avs-2000.webp"),
    dict(id="ast-15000", brand="exegate", name="Exegate Expert Turbo AST-15000", short="AST-15000", series="AST", code="AST-15000", price=31990,
         kw="15", va="15 000 ВА", vin="80–260", vout="220 В ±8%", amp="75", conn="клеммная колодка 4P и 2 евророзетки", size="300×400×545", weight="23,2",
         mount="Напольный / настольный", indic="ЖК-дисплей входных и выходных параметров", bypass=True, img="/img/ex-ast-15000.webp"),
    dict(id="spn-3600", brand="resanta", name="Ресанта СПН-3600", short="СПН-3600", series="СПН", code="СПН-3600", price=12490,
         kw="3,6", va="", vin="90–260", vout="220 В ±8%", amp="18,9", conn="клеммы", size="", weight="",
         mount="Настенный", indic="LCD-дисплей", bypass=False, img="/img/rs-spn-3600.webp"),
    dict(id="spn-13500", brand="resanta", name="Ресанта СПН-13500", short="СПН-13500", series="СПН", code="СПН-13500", price=28990,
         kw="13,5", va="", vin="90–260", vout="220 В ±8%", amp="71", conn="клеммы", size="", weight="21",
         mount="Настенный", indic="LCD-дисплей", bypass=False, img="/img/rs-spn-13500.webp"),
]
STOCK_BY = {s["id"]: s for s in STOCK}
PRICE = {s["name"]: money(s["price"]) for s in STOCK}
for _s in STOCK:
    MODEL_IMG[_s["name"]] = _s["img"]


def power_text(s):
    """Для маленьких Exegate производитель указывает только ВА — в ваттах не пересчитываем."""
    if s["brand"] == "exegate" and float(s["kw"].replace(",", ".")) < 5:
        return s["va"]
    return f"{s['kw']} кВт" + (f" ({s['va']})" if s["va"] else "")


def stock_card(sid):
    """(название, тег, пункты) для карточки модели «в наличии»."""
    s = STOCK_BY[sid]
    p1 = power_text(s) + f", макс. ток {s['amp']} А"
    items = [p1, f"Вход {s['vin']} В, выход {s['vout']}", s["indic"] + (", байпас" if s["bypass"] else "")]
    return (s["name"], s["mount"], items)
