# -*- coding: utf-8 -*-
"""Генератор 5 лендингов стабилизаторов. Запуск: python build.py  ->  site/<папка>/index.html"""
import html
import pathlib

from catalog import ex_card, rs_card, series_card, RS, MODEL_IMG, stock_card, PRICE

DOMAIN = "https://oasis.com.ru"
PHONE_HREF = "+79785792995"
PHONE_TEXT = "+7 978 579-29-95"
HOURS = "с 7:00 до 22:00"
OPERATOR = "индивидуальный предприниматель Гуриненко Наталья Николаевна"
OPERATOR_SHORT = "ИП Гуриненко Н.Н."
INN = "910206048286"
OGRNIP = "325911200103115"
ADDRESS = "Республика Крым, г. Симферополь, ул. Глинки, д. 61А, оф. 70"
POLICY_DATE = "4 октября 2026 г."

# ---------------------------------------------------------------- контент
COMMON_PROTECT = [
    ("Защита от скачков", "Отсекает опасное повышенное напряжение и импульсы, пока они не дошли до техники."),
    ("Стабильные 220 В", "На выходе держит 220 В с точностью ±8% при просадках и перепадах в сети."),
    ("Быстрый отклик", "Релейная схема реагирует за миллисекунды, свет и техника не «моргают»."),
    ("Доставка по Крыму", "Отправляем транспортными компаниями по всему Крыму и на новые территории."),
]

STEPS = [
    ("Свяжитесь с нами", "Позвоните или напишите в Telegram. Назовите, что хотите защитить, — подберём модель."),
    ("Согласуем заказ", "Уточним цену и наличие, договоримся о способе и сроках доставки."),
    ("Получите заказ", "Отправляем транспортной компанией по Крыму или на новые территории."),
]

USES_HOME = [
    ("Дом и дача", "Освещение, холодильник, телевизор, стиральная машина."),
    ("Насосы и скважины", "Погружные и поверхностные насосы, гидроаккумуляторы."),
    ("Отопление", "Газовые и электрокотлы, циркуляционные насосы, автоматика."),
    ("Кондиционеры", "Сплит-системы и другая техника с компрессором."),
]

FAQ_COMMON = [
    ("Как выбрать мощность стабилизатора?",
     "Сложите мощность всех приборов, которые работают одновременно, и добавьте запас 20–30%. "
     "Для насосов и компрессоров учтите пусковой ток — он в 3–5 раз выше рабочего. "
     "Если сомневаетесь, назовите нам список техники — посчитаем."),
    ("Вы устанавливаете стабилизаторы?",
     "Нет, установку мы не делаем. Подключение к щитку лучше доверить электрику — "
     "мы подскажем, какие провода и автоматы понадобятся."),
    ("Как вы доставляете заказ?",
     "Отправляем транспортными компаниями по всему Крыму и на новые территории. "
     "Способ и сроки согласуем при оформлении заказа."),
    ("Как узнать цену и наличие?",
     "Позвоните " + PHONE_TEXT + " или напишите нам в Telegram — ответим по конкретной модели."),
]

PAGES = [
    dict(
        slug="resanta", theme="t1",
        title="Стабилизатор Ресанта в Симферополе — купить, доставка по Крыму",
        desc="Стабилизаторы напряжения Ресанта СПН-3600 и СПН-13500 для квартиры и дома. Цены, доставка по Крыму и на новые территории. Звоните: " + PHONE_TEXT,
        eyebrow="Симферополь · доставка по всему Крыму",
        h1="Стабилизатор напряжения Ресанта",
        lead="Две модели СПН: 3,6 кВт для квартиры и небольшого дома и 13,5 кВт для частного дома. Работают при просадках сети до 90 В.",
        big="Ресанта", device="СПН-13500", hero_img="/img/rs-spn-13500.webp",
        stats=[("3,6 и 13,5 кВт", "две модели"), ("90–260 В", "входное напряжение"), ("от 12 490 ₽", "цены")],
        advantages=[
            ("Известный бренд", "Ресанта — один из самых популярных производителей стабилизаторов в России."),
            ("Широкий диапазон входа", "Модели СПН работают при входном напряжении от 90 до 260 В."),
            ("Защита и дисплей", "Защита от повышенного напряжения, перегрева и короткого замыкания, LCD-дисплей."),
            ("Доставка по Крыму", "Отправляем транспортными компаниями по всему Крыму и на новые территории."),
        ],
        models_title="Модели Ресанта СПН",
        models=[stock_card("spn-3600"), stock_card("spn-13500")],
        specs_title="Характеристики Ресанта СПН-13500",
        specs=[("Цена", "28 990 ₽"), ("Мощность", "13,5 кВт, макс. ток 71 А"), ("Входное напряжение", "90–260 В"), ("Выходное напряжение", "220 В ±8%"),
               ("Тип", "Релейный, однофазный, микропроцессорное управление"), ("Время регулирования", "менее 15 мс"), ("КПД", "97%"),
               ("Размещение", "Настенное"), ("Защиты", "От повышенного напряжения (245 ±5 В), перегрева, короткого замыкания")],
        uses=USES_HOME,
        faq=[("Какую модель выбрать?", "СПН-3600 (3,6 кВт) подойдёт для квартиры или небольшого дома: холодильник, телевизор, техника на кухне. СПН-13500 (13,5 кВт) — для частного дома с насосом, котлом и кондиционером. Нужна другая мощность — позвоните, подскажем."),
             ("Чем хорош релейный стабилизатор?", "Он быстро переключает ступени и не имеет механических деталей, которые изнашиваются, — поэтому надёжен в бытовой сети."),
             ("Что с мощностью при низком напряжении?", "У СПН выходная мощность снижается при низком входе: например, у СПН-13500 при 90 В на входе она составляет около 4,8 кВт. Учитывайте это при выборе.")] + FAQ_COMMON,
    ),
    dict(
        slug="10kvt", theme="t2",
        title="Стабилизатор для дома 10 кВт в Симферополе — доставка по Крыму",
        desc="Стабилизатор для дома на 10 кВт: Ресанта СПН-13500 (13,5 кВт) и Exegate AST-15000 (15 кВт) — модели с запасом мощности. Цены, доставка по Крыму. Звоните: " + PHONE_TEXT,
        eyebrow="Симферополь · доставка по всему Крыму",
        h1="Стабилизатор для дома 10 кВт",
        lead="Для нагрузки 10 кВт берут стабилизатор с запасом: Ресанта СПН-13500 на 13,5 кВт и Exegate AST-15000 на 15 кВт. Свет, котёл, насос и кондиционер под защитой.",
        big="10 кВт", device="10 кВт", hero_img="/img/rs-spn-13500.webp",
        stats=[("13,5 и 15 кВт", "модели с запасом под 10 кВт"), ("80–260 В", "вход (AST), у СПН 90–260 В"), ("±8%", "точность на выходе")],
        advantages=[
            ("Запас мощности", "Нагрузка 10 кВт плюс запас 20–30% и пусковые токи насоса или кондиционера — это 13,5–15 кВт."),
            ("Две модели на выбор", "Ресанта СПН-13500 (настенная) и Exegate AST-15000 (напольная, с байпасом)."),
            ("Работают при просадках", "AST-15000 принимает вход от 80 В, СПН-13500 — от 90 В."),
            ("Доставка по Крыму", "Отправляем транспортными компаниями по всему Крыму и на новые территории."),
        ],
        models_title="Модели с запасом под 10 кВт",
        models=[stock_card("spn-13500"), stock_card("ast-15000")],
        specs_title="Сравнение моделей",
        specs=[("Ресанта СПН-13500", "28 990 ₽ · 13,5 кВт · вход 90–260 В · макс. ток 71 А · настенный"),
               ("Exegate AST-15000", "31 990 ₽ · 15 кВт · вход 80–260 В · макс. ток 75 А · напольный · байпас"),
               ("Выходное напряжение", "220 В ±8% у обеих моделей"), ("Время переключения", "СПН — менее 15 мс, AST — менее 7 мс"), ("КПД", "СПН — 97%, AST — 98%"),
               ("При глубокой просадке", "У СПН-13500 мощность падает: около 4,8 кВт при входе 90 В"),
               ("Защиты", "От повышенного напряжения, перегрузки, перегрева и короткого замыкания")],
        uses=USES_HOME,
        faq=[("Почему не стабилизатор ровно на 10 кВт?", "Нагрузку считают с запасом 20–30%, а у насосов и кондиционеров пусковой ток в 3–5 раз выше рабочего. Поэтому для дома на 10 кВт берут модель на 13,5–15 кВт."),
             ("Какая модель лучше при глубоких просадках?", "AST-15000 принимает на вход от 80 В, СПН-13500 — от 90 В; у СПН при низком входе выходная мощность заметно падает. Если сеть проседает глубоко, позвоните — подберём вариант."),
             ("Напольный или настенный?", "СПН-13500 вешается на стену, AST-15000 ставится на пол или на стол. Принцип работы у обоих релейный.")] + FAQ_COMMON,
    ),
    dict(
        slug="spn-13500", theme="t3",
        title="Стабилизатор Ресанта СПН-13500 — купить в Симферополе, доставка по Крыму",
        desc="Стабилизатор Ресанта СПН-13500, 13,5 кВт, вход 90–260 В, гарантия производителя 3 года, цена 28 990 ₽. Доставка по Крыму и на новые территории. Звоните: " + PHONE_TEXT,
        eyebrow="Симферополь · доставка по всему Крыму",
        h1="Стабилизатор Ресанта СПН-13500",
        lead="13,5 кВт мощности и рабочий диапазон входа 90–260 В — для дома, где напряжение «плавает» всерьёз. Цена 28 990 ₽.",
        big="13,5 кВт", device="СПН-13500", hero_img="/img/rs-spn-13500.webp",
        gallery=["/img/rs-spn-13500-g%d.webp" % i for i in (1, 2, 3, 4)],
        stats=[("13,5 кВт", "номинальная мощность"), ("90–260 В", "рабочий вход"), ("28 990 ₽", "цена")],
        advantages=[
            ("Широкий вход", "Работает при просадке сети до 90 В — выручит там, где другие отключаются."),
            ("Мощный запас", "13,5 кВт и ток до 71 А: хватает на дом целиком вместе с насосом и котлом."),
            ("Защита по напряжению", "Отключает нагрузку при превышении 245 ±5 В, включает автоматически при возврате в норму."),
            ("Гарантия 3 года", "Гарантия производителя на стабилизаторы Ресанта СПН."),
        ],
        models_title="",
        models=[],
        specs_title="Технические характеристики",
        specs=[("Цена", "28 990 ₽"), ("Мощность", "13,5 кВт (при входе от 190 В; при 90 В — около 4,8 кВт)"), ("Макс. ток", "71 А"), ("Входное напряжение", "90–260 В"),
               ("Выходное напряжение", "220 В ±8%"), ("Тип", "Релейный, однофазный, микропроцессорное управление"), ("Время регулирования", "менее 15 мс"),
               ("КПД", "97%"), ("Высоковольтная защита", "245 ±5 В"), ("Прочие защиты", "От перегрева и короткого замыкания"),
               ("Дисплей", "LCD"), ("Размещение", "Настенное"), ("Охлаждение", "Принудительное"), ("Класс защиты", "IP20"),
               ("Рабочая температура", "0…+40 °C"), ("Вес", "21 кг"), ("Гарантия", "3 года (производитель)")],
        uses=USES_HOME,
        faq=[("Что с мощностью при низком напряжении?", "Ниже 190 В выходная мощность постепенно снижается, при 90 В — около 4,8 кВт. Если в вашей сети просадки глубокие, учитывайте это при расчёте нагрузки."),
             ("Подойдёт ли для всего дома?", "Да, 13,5 кВт покрывает большинство частных домов. Подключается к вводу после счётчика — это работа для электрика."),
             ("Где устанавливать?", "СПН-13500 настенный, класс защиты IP20: ставьте в сухом проветриваемом помещении (рабочая температура 0…+40 °C).")] + FAQ_COMMON,
    ),
    dict(
        slug="exegate", theme="t4",
        title="Стабилизатор Exegate для дома в Симферополе — доставка по Крыму",
        desc="Стабилизаторы напряжения Exegate для дома: Expert Turbo AST-500, AST-2000, AST-15000 и Master Turbo AVS-2000. Цены, доставка по Крыму. Звоните: " + PHONE_TEXT,
        eyebrow="Симферополь · доставка по всему Крыму",
        h1="Стабилизатор Exegate для дома",
        lead="Модели Exegate для дома: от компактных для техники до мощного AST-15000 на весь дом. Релейное переключение менее 7 мс, КПД 98%.",
        big="Exegate", device="Exegate", hero_img="/img/ex-ast-2000.webp",
        stats=[("80–265 В", "вход, в зависимости от модели"), ("98%", "КПД"), ("от 3 190 ₽", "цены")],
        advantages=[
            ("Быстрый отклик", "Менее 7 мс — техника не замечает скачков напряжения."),
            ("КПД 98%", "Минимум потерь и нагрева при работе."),
            ("От 500 ВА до 15 кВт", "Маленькие модели для техники и мощный AST-15000 для всего дома."),
            ("Доставка по Крыму", "Отправляем транспортными компаниями по всему Крыму и на новые территории."),
        ],
        models_title="Модели Exegate",
        models=[stock_card("ast-500"), stock_card("ast-2000"), stock_card("avs-2000"), stock_card("ast-15000")],
        specs_title="Общие характеристики моделей",
        specs=[("Выходное напряжение", "220 В ±8% (у AVS-2000 — ±10%)"), ("Время переключения", "менее 7 мс"), ("КПД", "98%"), ("Тип", "Релейный, однофазный"),
               ("Вход AST", "80–260 В"), ("Вход AVS-2000", "100–265 В"),
               ("Индикация", "Цифровая индикация входного и выходного напряжения (AST-15000 — дисплей)"),
               ("Защиты", "От повышенного и пониженного напряжения, высоковольтных импульсов, перегрузки, перегрева и короткого замыкания")],
        uses=USES_HOME,
        faq=[("Какую модель выбрать?", "AST-500 (500 ВА) — компьютер, телевизор, роутер. AST-2000 и AVS-2000 (2000 ВА) — холодильник, телевизор, небольшая техника; AVS-2000 вешается на стену. AST-15000 (15 кВт) — весь дом целиком."),
             ("Что делать, если напряжение падает ниже 100 В?", "AST-500, AST-2000 и AST-15000 работают от 80 В, AVS-2000 — от 100 В. Подскажем модель под вашу сеть.")] + FAQ_COMMON,
    ),
    dict(
        slug="exegate-15kvt", theme="t5",
        title="Стабилизатор Exegate 15 кВт AST-15000 — купить в Симферополе, доставка по Крыму",
        desc="Стабилизатор Exegate Expert Turbo AST-15000 на 15 кВт: вход 80–260 В, байпас, цена 31 990 ₽. Доставка по Крыму. Звоните: " + PHONE_TEXT,
        eyebrow="Симферополь · доставка по всему Крыму",
        h1="Стабилизатор Exegate 15 кВт",
        lead="Expert Turbo AST-15000: 15 кВт, вход 80–260 В, байпас, клеммная колодка и две розетки. Для большого дома, мастерской и небольшого производства. Цена 31 990 ₽.",
        big="15 кВт", device="15 кВт", hero_img="/img/ex-ast-15000.webp",
        gallery=["/img/ex-ast-15000-2.webp", "/img/ex-ast-15000-3.webp", "/img/ex-ast-15000-4.webp"],
        stats=[("15 кВт", "мощность"), ("80–260 В", "вход"), ("31 990 ₽", "цена")],
        advantages=[
            ("Большой запас мощности", "Тянет весь дом с котлом, насосом, кондиционерами и мастерской."),
            ("Дисплей параметров", "Показывает входное и выходное напряжение и режим работы."),
            ("Байпас и защиты", "Байпас-автомат на задней панели, защита от перенапряжения, перегрузки, перегрева и короткого замыкания."),
            ("Доставка по Крыму", "Отправляем транспортными компаниями по всему Крыму и на новые территории."),
        ],
        models_title="Модель на 15 кВт",
        models=[stock_card("ast-15000")],
        specs_title="Характеристики Expert Turbo AST-15000",
        specs=[("Цена", "31 990 ₽"), ("Мощность", "15 кВт (15 000 ВА)"), ("Входное напряжение", "80–260 В"), ("Выходное напряжение", "220 В ±8%"),
               ("Время переключения", "менее 7 мс"), ("КПД", "98%"), ("Макс. входной ток", "75 А"), ("Частота", "50 Гц"),
               ("Подключение", "Клеммная колодка 4P и 2 евророзетки"), ("Байпас", "Есть"), ("Размещение", "Напольное или настольное"),
               ("Габариты, вес", "300×400×545 мм, 23,2 кг"),
               ("Защиты", "От повышенного и пониженного напряжения, высоковольтных импульсов, перегрузки, перегрева и короткого замыкания")],
        uses=[("Большой дом", "Весь дом целиком, включая отопление и насосы."), ("Мастерская", "Станки и электроинструмент с пусковыми токами."),
              ("Небольшое производство", "Оборудование, требующее стабильного питания."), ("Гостевой дом, база отдыха", "Много потребителей одновременно.")],
        faq=[("Нужен ли 15 кВт для дома?", "Для обычного дома хватает 8–10 кВт. 15 кВт нужны при электрокотле, мастерской или нескольких мощных потребителях — поможем посчитать."),
             ("Что такое байпас?", "Режим, в котором нагрузка подключается напрямую к сети мимо стабилизатора — например, на время обслуживания. У AST-15000 байпас-автомат стоит на задней панели."),
             ("Как подключается?", "Входные и выходные провода подключаются к клеммной колодке 4P, плюс на панели две розетки 220 В. Подключение — работа для электрика, мы установку не выполняем.")] + FAQ_COMMON,
    ),
]

# ---------------------------------------------------------------- CSS
BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:var(--font);background:var(--bg);color:var(--fg);line-height:1.55;font-size:16px;padding-bottom:72px}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
header.top{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:16px 20px;max-width:1080px;margin:0 auto}
.brand{font-weight:700;font-size:15px;letter-spacing:.01em}
.top-phone{font-weight:700;text-decoration:none;white-space:nowrap}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:15px 26px;border-radius:var(--radius);font-weight:700;font-size:16px;text-decoration:none;border:2px solid transparent;cursor:pointer;line-height:1.2}
.btn-main{background:var(--accent);color:var(--accent-fg)}
.btn-alt{background:transparent;color:var(--hero-fg);border-color:currentColor}
.btn:active{transform:translateY(1px)}
.hero{background:var(--hero-bg);color:var(--hero-fg)}
.hero-in{max-width:1080px;margin:0 auto;padding:36px 20px 56px;display:grid;gap:32px;grid-template-columns:1fr}
.eyebrow{font-size:14px;opacity:.75;margin-bottom:14px}
h1{font-family:var(--head-font);font-size:clamp(30px,6vw,52px);line-height:1.1;font-weight:800;margin-bottom:16px}
.lead{font-size:18px;opacity:.85;max-width:34em;margin-bottom:24px}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:12px}
.price-note{font-size:14px;opacity:.7}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:28px}
.stat b{display:block;font-family:var(--head-font);font-size:clamp(20px,4vw,28px);line-height:1.1}
.stat span{font-size:13px;opacity:.7}
.visual{display:flex;align-items:center;justify-content:center}
.visual svg{width:100%;max-width:360px;height:auto}
.bignum{display:none;font-family:var(--head-font);font-weight:800;line-height:.95}
section{padding:56px 0}
h2{font-family:var(--head-font);font-size:clamp(24px,4vw,36px);line-height:1.15;margin-bottom:28px;font-weight:800}
.grid{display:grid;gap:16px}
.g4{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px}
.card h3{font-size:18px;margin-bottom:8px;font-family:var(--head-font)}
.card p{color:var(--muted);font-size:15px}
.tag{display:inline-block;font-size:12px;font-weight:700;color:var(--accent);margin-bottom:8px;text-transform:uppercase;letter-spacing:.06em}
.card ul{list-style:none;margin-top:10px}
.card li{color:var(--muted);font-size:15px;padding:5px 0 5px 20px;position:relative;border-top:1px solid var(--line)}
.card li:first-child{border-top:0}
.card li::before{content:"";position:absolute;left:0;top:13px;width:8px;height:8px;border-radius:50%;background:var(--accent)}
table{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
th,td{text-align:left;padding:14px 18px;border-bottom:1px solid var(--line);font-size:15px;vertical-align:top}
th{width:38%;color:var(--muted);font-weight:600}
tr:last-child th,tr:last-child td{border-bottom:0}
.steps{counter-reset:s}
.step{position:relative;padding-left:60px}
.step::before{counter-increment:s;content:counter(s);position:absolute;left:0;top:0;width:42px;height:42px;border-radius:50%;background:var(--accent);color:var(--accent-fg);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:18px}
.step h3{font-size:18px;margin-bottom:6px}
.step p{color:var(--muted);font-size:15px}
.delivery{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:28px}
.delivery p{max-width:40em;color:var(--muted)}
.delivery p+p{margin-top:8px}
details{border-bottom:1px solid var(--line);padding:18px 0}
details summary{cursor:pointer;font-weight:700;font-size:17px;list-style:none;display:flex;justify-content:space-between;gap:16px}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"+";font-size:24px;line-height:1;color:var(--accent)}
details[open] summary::after{content:"–"}
details p{color:var(--muted);margin-top:10px;max-width:46em}
.final{background:var(--hero-bg);color:var(--hero-fg);text-align:center;padding:64px 20px}
.final h2{margin-bottom:12px}
.final p{opacity:.8;margin-bottom:24px}
.final .cta{justify-content:center}
footer{padding:28px 20px 12px;text-align:center;color:var(--muted);font-size:14px}
.form{display:grid;gap:10px;max-width:420px;margin:0 auto 24px;text-align:left}
.form input,.form textarea{width:100%;padding:14px 16px;border-radius:var(--radius);border:2px solid transparent;font:inherit;font-size:16px;background:#fff;color:#111}
.form textarea{min-height:76px;resize:vertical}
.form .hp{position:absolute;left:-9999px;opacity:0}
.form button{border:0;font-family:inherit}
.form-note{font-size:12px;opacity:.65;margin-top:2px}
.form-msg{font-weight:700;min-height:1.4em;margin-bottom:4px}
.photo{width:100%;max-width:460px;border-radius:var(--radius);display:block;margin:0 auto}
.has-photo .visual svg,.has-photo .bignum{display:none!important}
.pic{background:#fefefe;border-radius:var(--radius);display:grid;place-items:center;overflow:hidden;padding:10px}
.pic img{width:100%;height:auto;display:block}
.card .pic{margin:-8px -8px 16px;aspect-ratio:1/1}
.hero-pic{width:100%;max-width:480px;margin:0 auto;box-shadow:0 30px 70px -30px rgba(0,0,0,.45)}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:50;display:flex;gap:8px;padding:10px 12px;background:var(--bg);border-top:1px solid var(--line)}
.bar .btn{flex:1;padding:14px 10px}
@media(min-width:820px){
 body{padding-bottom:0}.bar{display:none}
 .hero-in{grid-template-columns:1.15fr .85fr;align-items:center;padding:56px 20px 72px}
}
"""

THEMES = {
    # 1: светлый чистый
    "t1": """
:root{--font:'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;--head-font:var(--font);--bg:#fff;--fg:#14202b;--muted:#5a6b78;--card:#f5f9fa;--line:#e1eaee;--accent:#0f8b8d;--accent-fg:#fff;--hero-bg:#eaf6f6;--hero-fg:#14202b;--radius:12px;--dev:#fff;--dev2:#c6dfe0}
.btn-alt{color:#0f8b8d}
.final{background:#0f8b8d}.final{--accent:#fff;--accent-fg:#0f8b8d}
""",
    # 2: тёплый домашний
    "t2": """
:root{--font:'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;--head-font:Georgia,'Times New Roman',serif;--bg:#fbf6ee;--fg:#3a2e25;--muted:#7a6a5c;--card:#fff;--line:#eadfce;--accent:#c4622d;--accent-fg:#fff;--hero-bg:#f3e7d3;--hero-fg:#3a2e25;--radius:20px;--dev:#fffaf2;--dev2:#e3cfb0}
h1,h2{font-weight:700}
.btn-alt{color:#3a2e25}
.hero{border-radius:0 0 40px 40px}
.final{background:#3a2e25;--accent:#e08a4f}
""",
    # 3: тёмный технический
    "t3": """
:root{--font:'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;--head-font:Bahnschrift,'Segoe UI',system-ui,sans-serif;--bg:#16181c;--fg:#e8eaed;--muted:#9aa1ab;--card:#1f2228;--line:#2c3038;--accent:#ff7a1a;--accent-fg:#16181c;--hero-bg:#0f1114;--hero-fg:#fff;--radius:6px;--dev:#2a2e36;--dev2:#3a404a}
.visual svg{display:none}
.bignum{display:block;font-size:clamp(48px,9vw,104px);white-space:nowrap;color:var(--accent);text-align:center}
.stat{border-left:3px solid var(--accent);padding-left:12px}
th{font-family:Consolas,monospace;font-size:13px;text-transform:uppercase;letter-spacing:.04em}
.final{background:#0f1114}
""",
    # 4: журнальный минимализм
    "t4": """
:root{--font:'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;--head-font:'Segoe UI',system-ui,sans-serif;--bg:#fff;--fg:#000;--muted:#555;--card:#fff;--line:#000;--accent:#0a8f3c;--accent-fg:#fff;--hero-bg:#fff;--hero-fg:#000;--radius:0px;--dev:#fff;--dev2:#000}
h1{font-size:clamp(40px,9vw,88px);letter-spacing:-.03em;line-height:1}
h2{letter-spacing:-.02em}
.hero{border-bottom:2px solid #000}
.hero-in{grid-template-columns:1fr!important}
.visual{justify-content:flex-start}.visual svg{display:none}
.bignum{display:block;font-size:clamp(64px,18vw,200px);white-space:nowrap;overflow:hidden;letter-spacing:-.05em;color:#000;opacity:.07;margin-top:-8px}
.card,table,.delivery{border:1.5px solid #000}
th,td{border-bottom:1.5px solid #000}
details{border-bottom:1.5px solid #000}
.btn-alt{color:#000}
.stats{border-top:2px solid #000;padding-top:16px}
section h2::before{content:"";display:block;width:40px;height:4px;background:var(--accent);margin-bottom:14px}
.final{background:#000}.final{--accent:#17c25a}
.bar{border-top:2px solid #000}
""",
    # 5: яркий контрастный
    "t5": """
:root{--font:'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;--head-font:'Arial Black','Segoe UI',system-ui,sans-serif;--bg:#f3f6fb;--fg:#0b1f4d;--muted:#4a5a7d;--card:#fff;--line:#d9e1f0;--accent:#ffc800;--accent-fg:#0b1f4d;--hero-bg:#0b1f4d;--hero-fg:#fff;--radius:14px;--dev:#13306f;--dev2:#2a4a96}
h1,h2{font-weight:900}
.visual svg{display:none}
.bignum{display:block;font-size:clamp(52px,10vw,112px);white-space:nowrap;color:var(--accent);text-align:center;text-shadow:6px 6px 0 rgba(255,255,255,.08)}
.stat{background:rgba(255,255,255,.08);border-radius:12px;padding:12px}
.card{border:0;box-shadow:0 4px 18px rgba(11,31,77,.08)}
.tag{background:var(--accent);color:var(--accent-fg);padding:3px 10px;border-radius:99px}
.step::before{background:#0b1f4d;color:#ffc800}
.final{background:#0b1f4d}
""",
}

# ---------------------------------------------------------------- компоненты
def e(s):
    return html.escape(s, quote=True)


def device_svg(label):
    return f"""<svg viewBox="0 0 320 260" role="img" aria-label="Стабилизатор напряжения {e(label)}">
<rect x="30" y="20" width="260" height="210" rx="18" fill="var(--dev)" stroke="var(--dev2)" stroke-width="4"/>
<rect x="56" y="46" width="208" height="64" rx="10" fill="var(--hero-fg)" opacity=".1"/>
<text x="160" y="92" text-anchor="middle" font-family="Consolas,monospace" font-size="38" font-weight="700" fill="var(--accent)">220 V</text>
<g stroke="var(--dev2)" stroke-width="4" stroke-linecap="round"><line x1="60" y1="136" x2="260" y2="136"/><line x1="60" y1="152" x2="260" y2="152"/><line x1="60" y1="168" x2="260" y2="168"/></g>
<circle cx="70" cy="204" r="7" fill="var(--accent)"/><circle cx="96" cy="204" r="7" fill="var(--dev2)"/>
<text x="260" y="210" text-anchor="end" font-family="Segoe UI,Arial,sans-serif" font-size="16" font-weight="700" fill="var(--hero-fg)" opacity=".6">{e(label)}</text>
</svg>"""


def cards_models(models):
    out = []
    for name, tag, items in models:
        lis = "".join(f"<li>{e(i)}</li>" for i in items)
        img = MODEL_IMG.get(name)
        pic = f'<div class="pic"><img src="{img}" alt="{e(name)}" loading="lazy" width="380" height="380"></div>' if img else ""
        out.append(f'<div class="card">{pic}<span class="tag">{e(tag)}</span><h3>{e(name)}</h3><ul>{lis}</ul></div>')
    return "".join(out)


def find_photo(slug):
    base = pathlib.Path(__file__).parent / "photos"
    for ext in ("jpg", "jpeg", "webp", "png"):
        f = base / f"{slug}.{ext}"
        if f.exists():
            return f
    return None


def render(p):
    photo = find_photo(p["slug"])
    photo_html = f'<img class="photo" src="photo{photo.suffix}" alt="{e(p["h1"])}" width="460" height="345" fetchpriority="high">' if photo else ""
    if p.get("hero_img"):
        photo = True
        photo_html = f'<div class="pic hero-pic"><img src="{p["hero_img"]}" alt="{e(p["h1"])}" width="520" height="520" fetchpriority="high"></div>'
    gallery = ""
    if p.get("gallery"):
        pics = "".join(f'<div class="pic"><img src="{g}" alt="{e(p["h1"])} — фото {i}" loading="lazy" width="420" height="420"></div>' for i, g in enumerate(p["gallery"], 1))
        gallery = f'<section id="photos"><div class="wrap"><h2>Фото</h2><div class="grid g4">{pics}</div></div></section>'

    adv = "".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in p["advantages"])
    stats = "".join(f'<div class="stat"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in p["stats"])
    rows = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in p["specs"])
    uses = "".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in p["uses"])
    steps = "".join(f'<div class="step"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in STEPS)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in p["faq"])
    models = ""
    if p["models"]:
        models = f'<section id="models"><div class="wrap"><h2>{e(p["models_title"])}</h2><div class="grid g3">{cards_models(p["models"])}</div></div></section>'
    url = f"{DOMAIN}/{p['slug']}/"
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23ffc800'/%3E%3Cpath d='M36 8 18 36h12l-4 20 20-30H34z' fill='%230b1f4d'/%3E%3C/svg%3E">
<style>{THEMES[p['theme']].strip()}
{BASE_CSS.strip()}
{THEMES[p['theme']].strip()}</style>
</head>
<body class="{p['theme']}{' has-photo' if photo else ''}">
<header class="top">
 <div class="brand">⚡ Стабилизаторы · Симферополь</div>
 <a class="top-phone" href="tel:{PHONE_HREF}" data-goal="call">{PHONE_TEXT}</a>
</header>

<div class="hero"><div class="hero-in">
 <div>
  <div class="eyebrow">{e(p['eyebrow'])}</div>
  <h1>{e(p['h1'])}</h1>
  <p class="lead">{e(p['lead'])}</p>
  <div class="cta">
   <a class="btn btn-main" href="tel:{PHONE_HREF}" data-goal="call">Позвонить {PHONE_TEXT}</a>
   <a class="btn btn-alt tg" href="#" target="_blank" rel="noopener" data-goal="tg">Написать в Telegram</a>
  </div>
  <div class="price-note">Цену и наличие уточняйте по телефону · работаем {HOURS}</div>
  <div class="stats">{stats}</div>
 </div>
 <div class="visual">{photo_html}{device_svg(p['device'])}<div class="bignum">{e(p['big'])}</div></div>
</div></div>

<section id="why"><div class="wrap"><h2>Почему это удобно</h2><div class="grid g4">{adv}</div></div></section>
{models}
{gallery}
<section id="specs"><div class="wrap"><h2>{e(p['specs_title'])}</h2><table>{rows}</table></div></section>
<section id="use"><div class="wrap"><h2>Для чего подходит</h2><div class="grid g4">{uses}</div></div></section>
<section id="how"><div class="wrap"><h2>Как заказать</h2><div class="grid g3 steps">{steps}</div></div></section>
<section id="delivery"><div class="wrap"><div class="delivery"><h2>Доставка по Крыму и на новые территории</h2>
 <p>Отправляем заказы транспортными компаниями по всему Крыму и на новые территории — логистика налажена.</p>
 <p>Установку мы не выполняем: подключение к щитку лучше доверить электрику, а мы подскажем, что для этого нужно.</p></div></div></section>
<section id="faq"><div class="wrap"><h2>Частые вопросы</h2>{faq}</div></section>

<div class="final">
 <h2>Подберём стабилизатор под вашу нагрузку</h2>
 <p>Оставьте номер — перезвоним и ответим по цене и наличию. Работаем {HOURS}.</p>
 <form class="form" id="lead" novalidate>
  <input type="text" name="name" placeholder="Ваше имя" autocomplete="name" maxlength="60">
  <input type="tel" name="phone" placeholder="Телефон" autocomplete="tel" inputmode="tel" required maxlength="25">
  <textarea name="comment" placeholder="Что нужно защитить? (необязательно)" maxlength="400"></textarea>
  <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="form-msg" id="lead-msg" role="status"></div>
  <button class="btn btn-main" type="submit">Перезвоните мне</button>
  <div class="form-note">Нажимая кнопку, вы соглашаетесь на обработку персональных данных на условиях <a href="/privacy/">политики конфиденциальности</a>.</div>
 </form>
 <p>Или свяжитесь сами:</p>
 <div class="cta">
  <a class="btn btn-main" href="tel:{PHONE_HREF}" data-goal="call">Позвонить {PHONE_TEXT}</a>
  <a class="btn btn-alt tg" href="#" target="_blank" rel="noopener" data-goal="tg" style="color:#fff">Написать в Telegram</a>
 </div>
</div>
<footer>Симферополь · доставка по Крыму и на новые территории · {HOURS} · установку не выполняем<br>{OPERATOR_SHORT}, ИНН {INN}, ОГРНИП {OGRNIP} · <a href="/privacy/">Политика конфиденциальности</a></footer>

<div class="bar">
 <a class="btn btn-main" href="tel:{PHONE_HREF}" data-goal="call">Позвонить</a>
 <a class="btn btn-main tg" href="#" target="_blank" rel="noopener" data-goal="tg">Telegram</a>
</div>

<script>
// Настройки: ссылка на Telegram (например "https://t.me/username") и номер счётчика Яндекс.Метрики
var TG_URL = "https://t.me/B2B_opt_simf";
var YM_ID = "113489938";
(function(){{
  document.querySelectorAll('.tg').forEach(function(a){{
    if (TG_URL) a.href = TG_URL; else a.remove();
  }});
  if (YM_ID) {{
    (function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};
    m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0];k.async=1;k.src=r;a.parentNode.insertBefore(k,a)}})
    (window,document,"script","https://mc.yandex.ru/metrika/tag.js","ym");
    ym(YM_ID,"init",{{clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true}});
  }}
  var form = document.getElementById('lead');
  if (form) form.addEventListener('submit', function(ev){{
    ev.preventDefault();
    var msg = document.getElementById('lead-msg'), btn = form.querySelector('button');
    var phone = form.phone.value.replace(/\\D/g,'');
    if (phone.length < 10) {{ msg.textContent = 'Введите номер телефона'; return; }}
    btn.disabled = true; msg.textContent = 'Отправляем…';
    fetch('/send.php', {{method:'POST', headers:{{'Content-Type':'application/json'}},
      body: JSON.stringify({{name:form.name.value, phone:form.phone.value, comment:form.comment.value, website:form.website.value, page:location.pathname, search:location.search.slice(0,200), ref:document.referrer.slice(0,200)}})}})
    .then(function(r){{ return r.json(); }})
    .then(function(j){{
      if (!j.ok) throw 0;
      msg.textContent = 'Спасибо! Мы перезвоним в ближайшее время.';
      form.reset();
      if (YM_ID && window.ym) ym(YM_ID,'reachGoal','form');
    }})
    .catch(function(){{ msg.textContent = 'Не удалось отправить. Позвоните нам: {PHONE_TEXT}'; btn.disabled = false; }});
  }});
  document.addEventListener('click', function(ev){{
    var a = ev.target.closest('[data-goal]');
    if (a && YM_ID && window.ym) ym(YM_ID,'reachGoal',a.getAttribute('data-goal'));
  }});
}})();
</script>
</body>
</html>
"""


def render_index():
    cards = "".join(
        f'<a class="card" href="/{p["slug"]}/" style="text-decoration:none;display:block"><h3>{e(p["h1"])}</h3><p>Подробнее и заказать →</p></a>'
        for p in PAGES)
    title = "Стабилизаторы напряжения в Симферополе — доставка по Крыму"
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="Стабилизаторы напряжения Ресанта и Exegate для дома. Доставка по Крыму и на новые территории. Звоните: {PHONE_TEXT}">
<link rel="canonical" href="{DOMAIN}/">
<style>{THEMES['t1'].strip()}
{BASE_CSS.strip()}
{THEMES['t1'].strip()}
body{{padding-bottom:0}}</style>
</head>
<body class="t1">
<header class="top">
 <div class="brand">⚡ Стабилизаторы · Симферополь</div>
 <a class="top-phone" href="tel:{PHONE_HREF}">{PHONE_TEXT}</a>
</header>
<div class="hero"><div class="hero-in" style="grid-template-columns:1fr">
 <div>
  <h1>Стабилизаторы напряжения в Симферополе</h1>
  <p class="lead">Ресанта и Exegate для дома. Подберём модель под вашу нагрузку и отправим по всему Крыму и на новые территории.</p>
  <div class="cta"><a class="btn btn-main" href="tel:{PHONE_HREF}">Позвонить {PHONE_TEXT}</a></div>
  <div class="price-note">Работаем {HOURS}</div>
 </div>
</div></div>
<section><div class="wrap"><h2>Выберите стабилизатор</h2><div class="grid g3">{cards}</div></div></section>
<footer>{OPERATOR_SHORT}, ИНН {INN}, ОГРНИП {OGRNIP} · <a href="/privacy/">Политика конфиденциальности</a></footer>
</body>
</html>
"""


def render_privacy():
    sections = [
        ("1. Общие положения", [
            f"Настоящая политика определяет порядок обработки и защиты персональных данных посетителей сайта {DOMAIN.replace('https://', '')} (далее — сайт). Она разработана в соответствии с Федеральным законом от 27.07.2006 № 152-ФЗ «О персональных данных».",
            f"Оператор персональных данных — {OPERATOR} ({OPERATOR_SHORT}), ИНН {INN}, ОГРНИП {OGRNIP}. Адрес для корреспонденции: {ADDRESS}. Телефон: {PHONE_TEXT}.",
            "Используя сайт и отправляя заявку, вы подтверждаете, что ознакомились с политикой и согласны на обработку ваших персональных данных на указанных в ней условиях.",
        ]),
        ("2. Какие данные мы обрабатываем", [
            "Данные, которые вы указываете в форме заявки: имя, номер телефона, текст комментария.",
            "Технические данные, которые передаёт браузер: IP-адрес, тип устройства и браузера, страница сайта, с которой отправлена заявка, данные cookie.",
        ]),
        ("3. Цели обработки", [
            "Связаться с вами по вашей заявке: проконсультировать, подобрать модель стабилизатора, сообщить цену и наличие, согласовать заказ и доставку.",
            "Исполнить заказ и организовать доставку транспортной компанией.",
            "Анализировать работу сайта и эффективность рекламы в обезличенном виде.",
        ]),
        ("4. Правовое основание", [
            "Обработка осуществляется на основании вашего согласия, которое вы даёте, отправляя форму заявки, а также для заключения и исполнения договора, стороной которого вы являетесь.",
        ]),
        ("5. Как и сколько мы храним данные", [
            "Мы обрабатываем данные с использованием средств автоматизации и без них: сбор, запись, систематизация, хранение, уточнение, использование, передача (в случаях, указанных ниже), удаление.",
            "Данные хранятся не дольше, чем необходимо для целей обработки, либо до отзыва вами согласия, если иное не требуется законом.",
        ]),
        ("6. Передача данных третьим лицам", [
            "Мы не продаём и не передаём ваши данные третьим лицам, кроме случаев, когда это необходимо для исполнения заказа (например, транспортной компании для доставки) или предусмотрено законом.",
            "Заявка с сайта может поступать оператору по электронной почте или через мессенджер Telegram. Для анализа посещаемости на сайте может использоваться сервис Яндекс.Метрика, который собирает обезличенные данные о поведении посетителей с помощью cookie.",
        ]),
        ("7. Cookie", [
            "Сайт может использовать cookie для статистики и работы сервисов аналитики. Вы можете отключить cookie в настройках браузера, это не повлияет на возможность позвонить или отправить заявку.",
        ]),
        ("8. Ваши права", [
            "Вы вправе получить информацию об обработке своих данных, потребовать их уточнения, блокирования или удаления, а также в любой момент отозвать согласие на обработку.",
            f"Для этого направьте обращение по адресу: {ADDRESS}, либо сообщите по телефону {PHONE_TEXT}. Мы рассмотрим обращение в сроки, установленные законом.",
            "Вы также вправе обратиться в уполномоченный орган по защите прав субъектов персональных данных (Роскомнадзор) или в суд.",
        ]),
        ("9. Защита данных", [
            "Мы принимаем правовые и организационные меры, чтобы защитить данные от неправомерного доступа, изменения, раскрытия и уничтожения.",
        ]),
        ("10. Изменения политики", [
            f"Оператор вправе изменять политику. Актуальная версия всегда размещена на этой странице. Дата последнего обновления: {POLICY_DATE}",
        ]),
    ]
    body = "".join(f"<h2>{e(t)}</h2>" + "".join(f"<p>{e(x)}</p>" for x in ps) for t, ps in sections)
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Политика конфиденциальности — {e(OPERATOR_SHORT)}</title>
<meta name="description" content="Политика обработки персональных данных на сайте oasis.com.ru">
<link rel="canonical" href="{DOMAIN}/privacy/">
<style>
body{{margin:0;font-family:'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;color:#1c2630;background:#fff;line-height:1.6}}
main{{max-width:760px;margin:0 auto;padding:32px 20px 56px}}
h1{{font-size:clamp(26px,5vw,36px);line-height:1.2;margin:0 0 8px}}
h2{{font-size:20px;margin:32px 0 8px}}
p{{margin:0 0 10px;color:#3b4854}}
a{{color:#0f8b8d}}
</style>
</head>
<body>
<main>
<h1>Политика конфиденциальности</h1>
<p>Оператор: {e(OPERATOR)}</p>
{body}
</main>
</body>
</html>
"""


def main(pages=True):
    import shutil, zipfile
    here = pathlib.Path(__file__).parent
    root = here / "site"
    for p in (PAGES if pages else []):
        d = root / p["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(render(p), encoding="utf-8")
        photo = find_photo(p["slug"])
        if photo:
            shutil.copy(photo, d / f"photo{photo.suffix}")
        print("OK", d / "index.html", "(фото)" if photo else "")
    (root / "privacy").mkdir(exist_ok=True)
    (root / "privacy" / "index.html").write_text(render_privacy(), encoding="utf-8")
    for f in (here / "server").iterdir():
        shutil.copy(f, root / f.name)
    urls = "".join(f"<url><loc>{DOMAIN}/{p['slug']}/</loc></url>" for p in PAGES)
    (root / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>", encoding="utf-8")
    robots = ["User-agent: *", "Allow: /", "Disallow: /config.php", "Sitemap: " + DOMAIN + "/sitemap.xml", ""]
    (root / "robots.txt").write_text("\n".join(robots), encoding="utf-8")
    (root / "index.html").write_text(render_index(), encoding="utf-8")
    links = "".join(f'<li><a href="site/{p["slug"]}/">{e(p["h1"])}</a> <small>({p["theme"]})</small></li>' for p in PAGES)
    (here / "compare.html").write_text(
        f'<!doctype html><meta charset="utf-8"><title>Варианты</title>'
        f'<body style="font-family:Segoe UI,Arial;max-width:600px;margin:40px auto;padding:0 20px;line-height:2"><h1>5 лендингов</h1><ul>{links}</ul>',
        encoding="utf-8")
    dist = here / "dist"
    dist.mkdir(exist_ok=True)
    with zipfile.ZipFile(dist / "oasis-site.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(root.rglob("*")):
            if f.is_file() and f.name != "config.php":
                z.write(f, f.relative_to(root).as_posix())
    print("ZIP", dist / "oasis-site.zip")


if __name__ == "__main__":
    main()
