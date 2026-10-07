# -*- coding: utf-8 -*-
"""Два «вау»-лендинга со scroll-анимацией. Запуск: python build_wow.py -> preview/<имя>/index.html
Факты и контакты берутся из build.py, чтобы не расходились с основными страницами."""
import html
import pathlib

import build as B
from catalog import MODEL_IMG, PRICE
from fx import pf, anatomy, PF_CSS, PF_JS
from widgets import hotspots

PAGES = {p["slug"]: p for p in B.PAGES}


def e(s):
    return html.escape(s, quote=True)


def pic(name):
    img = MODEL_IMG.get(name)
    return pf(img, name) if img else ""


CSS = r"""
:root{--pf-glow:rgba(56,240,255,.26);--pf-rim:rgba(0,0,0,.55);--pf-accent:#38f0ff;--bg:#04070c;--bg2:#0a1018;--fg:#e9f1f7;--muted:#8fa2b3;--line:#1b2733;--cyan:#38f0ff;--green:#44ff9a;--amber:#ffb224;--red:#ff4d5e;--card:#0c141d;--glass:#0c141dcc;--btn-fg:#021218;--pulse:#38f0ff55;--bd2:#ffffff44;--stat-grad:linear-gradient(180deg,#fff,#8fe8ff);--tcard:linear-gradient(160deg,#0f1b27,#0a1018);--delivery:linear-gradient(135deg,#0c1a24,#0a1018);--glow:#38f0ff22;--inp:#060b11;--barbg:#04070cee;--font:'Segoe UI Variable Display','Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;--head:'Bahnschrift','Segoe UI Variable Display','Segoe UI',system-ui,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--fg);font-family:var(--font);line-height:1.55;font-size:16px;overflow-x:hidden;padding-bottom:70px}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.top{position:fixed;inset:0 0 auto 0;z-index:60;display:flex;justify-content:space-between;align-items:center;padding:14px 20px;background:linear-gradient(var(--bg),transparent)}
.brand{font-weight:700;font-size:14px;letter-spacing:.04em;text-transform:uppercase}
.brand i{color:var(--cyan);font-style:normal}
.tel{font-weight:700;text-decoration:none;border:1px solid var(--line);padding:8px 14px;border-radius:99px;background:var(--glass);backdrop-filter:blur(8px)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:16px 28px;border-radius:99px;font-weight:700;font-size:16px;text-decoration:none;border:0;cursor:pointer;font-family:inherit;line-height:1.2}
.btn-main{background:var(--cyan);color:var(--btn-fg);box-shadow:0 0 0 0 var(--pulse);animation:pulse 2.4s infinite}
.btn-alt{background:transparent;color:var(--fg);border:1.5px solid var(--bd2)}
@keyframes pulse{0%{box-shadow:0 0 0 0 var(--pulse)}70%{box-shadow:0 0 0 16px transparent}100%{box-shadow:0 0 0 0 transparent}}
.cta{display:flex;flex-wrap:wrap;gap:12px}
h1,h2,h3{font-family:var(--head);line-height:1.05;font-weight:800;letter-spacing:-.01em}
h2{font-size:clamp(30px,6vw,60px);margin-bottom:24px}
.eyebrow{font-family:Consolas,monospace;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--cyan);margin-bottom:18px}
section{position:relative}
.pad{padding:96px 0}
/* hero */
.hero{min-height:100svh;display:flex;align-items:center;position:relative;overflow:hidden;isolation:isolate}
.hero::before{content:"";position:absolute;inset:0;z-index:-2;background:radial-gradient(600px circle at var(--mx,70%) var(--my,35%),#38f0ff22,transparent 60%),radial-gradient(900px circle at 10% 90%,#44ff9a14,transparent 60%)}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;background-image:linear-gradient(#ffffff08 1px,transparent 1px),linear-gradient(90deg,#ffffff08 1px,transparent 1px);background-size:56px 56px;mask-image:radial-gradient(circle at 50% 40%,#000,transparent 75%)}
.hero h1{font-size:clamp(38px,8.5vw,104px);max-width:11em;margin-bottom:22px}
.hero h1 em{font-style:normal;background:linear-gradient(90deg,var(--cyan),var(--green));-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{font-size:clamp(17px,2.4vw,22px);color:var(--muted);max-width:34em;margin-bottom:30px}
.hero .big{position:absolute;right:-2vw;bottom:-6vw;font-family:var(--head);font-weight:900;font-size:clamp(180px,42vw,620px);line-height:.8;color:transparent;-webkit-text-stroke:2px #38f0ff33;z-index:-1;letter-spacing:-.04em;pointer-events:none}
.scrollhint{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);font-size:12px;letter-spacing:.2em;color:var(--muted);text-transform:uppercase;display:flex;flex-direction:column;align-items:center;gap:8px}
.scrollhint i{width:1.5px;height:34px;background:linear-gradient(var(--cyan),transparent);animation:drip 1.8s infinite}
@keyframes drip{0%{transform:scaleY(0);transform-origin:top}50%{transform:scaleY(1);transform-origin:top}51%{transform-origin:bottom}100%{transform:scaleY(0);transform-origin:bottom}}
/* sticky stage */
.stage{position:relative}
.sticky{position:sticky;top:0;height:100svh;overflow:hidden;background:radial-gradient(1200px circle at 50% 50%,#0a1620,#04070c)}
.sticky canvas{position:absolute;inset:0;width:100%;height:100%;display:block}
.hud{position:absolute;inset:0;pointer-events:none;display:flex;flex-direction:column;justify-content:space-between;padding:76px 20px 26px;max-width:1120px;margin:0 auto}
.chip{font-family:Consolas,monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;padding:6px 12px;border:1px solid var(--line);border-radius:99px;background:#0c141dcc}
.note{font-size:12px;color:var(--muted)}
.hud-top{display:flex;justify-content:space-between;align-items:center;gap:10px}
.readout{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-top:14px}
.readout small{flex-basis:100%;font-size:13px;color:var(--muted)}
.readout b{font-family:var(--head);font-size:clamp(64px,11vw,128px);line-height:.9;font-variant-numeric:tabular-nums;transition:color .25s}
.readout span{font-size:clamp(24px,4vw,44px);color:var(--muted);font-family:var(--head)}
.readout em{font-style:normal;font-family:Consolas,monospace;font-size:13px;letter-spacing:.14em;padding:5px 12px;border-radius:99px;border:1px solid currentColor}
.cap{font-family:var(--head);font-size:clamp(20px,3.6vw,38px);line-height:1.1;max-width:20em;min-height:2.4em;text-shadow:0 2px 20px #000}
.cap small{display:block;font-family:var(--font);font-weight:400;font-size:15px;color:var(--muted);margin-top:8px;text-shadow:none}
.prog{height:3px;background:var(--line);border-radius:3px;margin-top:16px;overflow:hidden}
.prog i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--cyan),var(--green))}
/* reveal */
.rv{opacity:0;transform:translateY(34px);transition:opacity .8s cubic-bezier(.2,.7,.2,1),transform .8s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}
.rv.d1{transition-delay:.1s}.rv.d2{transition-delay:.2s}.rv.d3{transition-delay:.3s}
/* stats */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:22px;overflow:hidden}
.stat{background:var(--bg2);padding:34px 26px}
.stat b{display:block;white-space:nowrap;margin-bottom:12px;font-family:var(--head);font-size:clamp(36px,5.4vw,76px);line-height:1.05;background:var(--stat-grad);-webkit-background-clip:text;background-clip:text;color:transparent;font-variant-numeric:tabular-nums}
.stat span{display:block;color:var(--muted);font-size:15px;line-height:1.5}
/* horizontal pinned */
.hs{height:300vh}
.hs .sticky{background:var(--bg)}
.hs-in{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:28px}
.hs-in h2{padding:0 20px;max-width:1120px;margin:0 auto 0;width:100%}
.track{display:flex;gap:18px;padding:0 20px;will-change:transform}
.tcard{flex:0 0 min(78vw,420px);height:min(52vh,360px);border-radius:26px;padding:28px;background:var(--tcard);border:1px solid var(--line);display:flex;flex-direction:column;justify-content:flex-end;position:relative;overflow:hidden}
.tcard::before{content:attr(data-n);position:absolute;top:10px;right:20px;font-family:var(--head);font-size:120px;font-weight:900;color:#ffffff08;line-height:1}
.tcard h3{font-size:30px;margin-bottom:8px}
.tcard p{color:var(--muted)}
.tcard .ic{position:absolute;top:26px;left:28px;width:54px;height:54px;border-radius:16px;background:#38f0ff18;border:1px solid #38f0ff55;display:grid;place-items:center;color:var(--cyan);font-size:26px}
/* models */
.g3{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(270px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:26px}
.pic{background:#fefefe;border-radius:18px;display:grid;place-items:center;overflow:hidden;padding:10px;margin:-6px -6px 18px;aspect-ratio:1/1}
.pic img{width:100%;height:auto;display:block}
.mprice{font-size:26px;font-weight:700;margin:2px 0 10px;color:var(--pf-accent)}
.card h3{font-size:22px;margin:6px 0 10px}
.card ul{list-style:none}
.card li{color:var(--muted);padding:7px 0 7px 22px;border-top:1px solid var(--line);position:relative;font-size:15px}
.card li:first-child{border-top:0}
.card li::before{content:"";position:absolute;left:0;top:15px;width:8px;height:8px;border-radius:50%;background:var(--cyan)}
.tag{font-family:Consolas,monospace;font-size:12px;letter-spacing:.1em;color:var(--cyan);text-transform:uppercase}
table{width:100%;border-collapse:collapse}
th,td{text-align:left;padding:16px 4px;border-bottom:1px solid var(--line);vertical-align:top}
th{width:38%;color:var(--muted);font-weight:600;font-size:15px}
.delivery{border:1px solid var(--line);border-radius:26px;padding:clamp(24px,5vw,48px);background:var(--delivery)}
.delivery p{color:var(--muted);max-width:40em}
.delivery p+p{margin-top:10px}
details{border-bottom:1px solid var(--line);padding:20px 0}
summary{cursor:pointer;font-weight:700;font-size:18px;list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-size:26px;line-height:1;color:var(--cyan)}
details[open] summary::after{content:"–"}
details p{color:var(--muted);margin-top:12px;max-width:46em}
/* final */
.final{text-align:center;padding:110px 20px;background:radial-gradient(800px circle at 50% 0,var(--glow),transparent 70%),var(--bg2);border-top:1px solid var(--line)}
.final h2{max-width:14em;margin:0 auto 14px}
.final>p{color:var(--muted);margin-bottom:28px}
.form{display:grid;gap:10px;max-width:420px;margin:0 auto 24px;text-align:left}
.form input,.form textarea{width:100%;padding:16px 18px;border-radius:16px;border:1.5px solid var(--line);font:inherit;font-size:16px;background:var(--inp);color:var(--fg)}
.form input:focus,.form textarea:focus{outline:0;border-color:var(--cyan)}
.form textarea{min-height:76px;resize:vertical}
.form .hp{position:absolute;left:-9999px;opacity:0}
.form-msg{font-weight:700;min-height:1.4em}
.form-note{font-size:12px;color:var(--muted)}
.final .cta{justify-content:center}
footer{padding:30px 20px 16px;text-align:center;color:var(--muted);font-size:13px}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:70;display:flex;gap:8px;padding:10px 12px;background:var(--barbg);backdrop-filter:blur(10px);border-top:1px solid var(--line)}
.bar .btn{flex:1;padding:14px 10px}
@media(max-width:480px){.brand{font-size:11px;letter-spacing:.02em;white-space:nowrap}.tel{padding:7px 11px;font-size:13px;white-space:nowrap}.top{padding:12px 14px}.hud,.hudB{padding-top:70px}}
@media(max-width:400px){.brand span{display:none}.top{padding:12px 12px}}
@media(min-width:820px){body{padding-bottom:0}.bar{display:none}}
@media(prefers-reduced-motion:reduce){.btn-main{animation:none}.rv{opacity:1;transform:none;transition:none}.scrollhint i{animation:none}}
"""

# ------------------------------------------------------------------ общий каркас
def shell(p, slug_out, title, desc, hero, stage_and_more, extra_css, page_js):
    specs = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in p["specs"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in p["faq"])
    models = ""
    if p["models"]:
        cards = "".join(
            f'<div class="card rv">{pic(n)}<span class="tag">{e(t)}</span><h3>{e(n)}</h3><div class="mprice">{PRICE.get(n, "")}</div><ul>{"".join(f"<li>{e(i)}</li>" for i in its)}</ul></div>'
            for n, t, its in p["models"])
        models = f'<section class="pad"><div class="wrap"><div class="eyebrow rv">Модели</div><h2 class="rv">{e(p["models_title"])}</h2><div class="g3">{cards}</div></div></section>'
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#04070c">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2304070c'/%3E%3Cpath d='M36 8 18 36h12l-4 20 20-30H34z' fill='%2338f0ff'/%3E%3C/svg%3E">
<style>{CSS}
{PF_CSS}
{extra_css}</style>
</head>
<body>
<header class="top">
 <div class="brand"><i>⚡</i> Стабилизаторы<span> · Симферополь</span></div>
 <a class="tel" href="tel:{B.PHONE_HREF}" data-goal="call">{B.PHONE_TEXT}</a>
</header>

{hero}
{stage_and_more}
{models}

<section class="pad"><div class="wrap">
 <div class="eyebrow rv">Характеристики</div><h2 class="rv">{e(p['specs_title'])}</h2>
 <table class="rv">{specs}</table>
</div></section>

<section class="pad"><div class="wrap"><div class="delivery rv">
 <div class="eyebrow">Доставка</div>
 <h2>По всему Крыму и на новые территории</h2>
 <p>Отправляем заказы транспортными компаниями — логистика налажена.</p>
 <p>Установку мы не выполняем: подключение к щитку лучше доверить электрику, а мы подскажем, что для этого нужно.</p>
</div></div></section>

<section class="pad"><div class="wrap"><div class="eyebrow rv">FAQ</div><h2 class="rv">Частые вопросы</h2>{faq}</div></section>

<div class="final" id="order">
 <div class="eyebrow">Заказать</div>
 <h2>Подберём стабилизатор под вашу нагрузку</h2>
 <p>Оставьте номер — перезвоним и ответим по цене и наличию. Работаем {B.HOURS}.</p>
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
 <div class="cta" style="margin-top:14px">
  <a class="btn btn-main" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить {B.PHONE_TEXT}</a>
  <a class="btn btn-alt tg" href="#" target="_blank" rel="noopener" data-goal="tg">Написать в Telegram</a>
 </div>
</div>
<footer>Симферополь · доставка по Крыму и на новые территории · {B.HOURS} · установку не выполняем<br>{B.OPERATOR_SHORT}, ИНН {B.INN}, ОГРНИП {B.OGRNIP} · <a href="/privacy/">Политика конфиденциальности</a></footer>

<div class="bar">
 <a class="btn btn-main" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить</a>
 <a class="btn btn-alt tg" href="#" target="_blank" rel="noopener" data-goal="tg">Telegram</a>
</div>

<script>
// Настройки: ссылка на Telegram и номер счётчика Яндекс.Метрики
var TG_URL = "https://t.me/B2B_opt_simf";
var YM_ID = "113489938";
{COMMON_JS}
{page_js}
</script>
</body>
</html>
"""


COMMON_JS = r"""
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  window.REDUCE = reduce;
  document.querySelectorAll('.tg').forEach(function(a){ if (TG_URL) a.href = TG_URL; else a.remove(); });
  if (YM_ID) {
    (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
    m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0];k.async=1;k.src=r;a.parentNode.insertBefore(k,a)})
    (window,document,"script","https://mc.yandex.ru/metrika/tag.js","ym");
    ym(YM_ID,"init",{clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true});
  }
  document.addEventListener('click', function(ev){
    var a = ev.target.closest('[data-goal]');
    if (a && YM_ID && window.ym) ym(YM_ID,'reachGoal',a.getAttribute('data-goal'));
  });
  // появление блоков
  var io = new IntersectionObserver(function(es){ es.forEach(function(x){ if (x.isIntersecting){ x.target.classList.add('in'); io.unobserve(x.target);} }); }, {threshold:.15});
  document.querySelectorAll('.rv').forEach(function(el){ io.observe(el); });
  // счётчики
  function fmt(v, d){ return v.toFixed(d).replace('.', ','); }
  var cio = new IntersectionObserver(function(es){ es.forEach(function(x){
    if (!x.isIntersecting) return; cio.unobserve(x.target);
    var el = x.target, to = parseFloat(el.dataset.count), d = +(el.dataset.dec||0), t0 = performance.now();
    if (reduce) { el.textContent = fmt(to,d); return; }
    (function f(t){ var k = Math.min(1,(t-t0)/1400), q = 1-Math.pow(1-k,3); el.textContent = fmt(to*q,d); if (k<1) requestAnimationFrame(f); })(t0);
  }); }, {threshold:.6});
  document.querySelectorAll('[data-count]').forEach(function(el){ cio.observe(el); });
  // подсветка за курсором
  var hero = document.querySelector('.hero');
  if (hero && !reduce) hero.addEventListener('pointermove', function(ev){ var r = hero.getBoundingClientRect(); hero.style.setProperty('--mx', (ev.clientX-r.left)+'px'); hero.style.setProperty('--my', (ev.clientY-r.top)+'px'); });
  // форма
  var form = document.getElementById('lead');
  if (form) form.addEventListener('submit', function(ev){
    ev.preventDefault();
    var msg = document.getElementById('lead-msg'), btn = form.querySelector('button');
    var phone = form.phone.value.replace(/\D/g,'');
    if (phone.length < 10) { msg.textContent = 'Введите номер телефона'; return; }
    btn.disabled = true; msg.textContent = 'Отправляем…';
    fetch('/send.php', {method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({name:form.name.value, phone:form.phone.value, comment:form.comment.value, website:form.website.value, page:location.pathname, search:location.search.slice(0,200), ref:document.referrer.slice(0,200)})})
    .then(function(r){ return r.json(); })
    .then(function(j){ if (!j.ok) throw 0; msg.textContent = 'Спасибо! Мы перезвоним в ближайшее время.'; form.reset(); if (YM_ID && window.ym) ym(YM_ID,'reachGoal','form'); })
    .catch(function(){ msg.textContent = 'Не удалось отправить. Позвоните нам: """ + B.PHONE_TEXT + r"""'; btn.disabled = false; });
  });
  // прогресс прокрутки внутри высокой секции: 0..1
  window.sectionProgress = function(el){ var r = el.getBoundingClientRect(), total = el.offsetHeight - innerHeight; return Math.max(0, Math.min(1, -r.top / Math.max(1,total))); };
  window.visible = function(el){ var r = el.getBoundingClientRect(); return r.bottom > 0 && r.top < innerHeight; };
})();
"""
COMMON_JS = COMMON_JS + PF_JS

# ================================================================== СТРАНИЦА 1: осциллограф
SCOPE_CSS = r"""
.hero .wrap{position:relative;z-index:2;padding-top:90px;padding-bottom:110px;display:grid;gap:20px;align-items:center}
@media(min-width:900px){.hero .wrap{grid-template-columns:1.05fr .95fr}}
.hero .pf.lg{margin-top:10px}
.hprice{display:inline-flex;align-items:baseline;gap:18px;margin:0 0 22px;padding:12px 26px;border-radius:99px;border:1px solid #38f0ff55;background:#38f0ff14}
.hprice span{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.hprice b{font-family:var(--head);font-size:clamp(28px,5vw,40px);color:var(--cyan);letter-spacing:-.02em}
"""

SCOPE_JS = r"""
(function(){
  var stage = document.getElementById('stage'), cv = document.getElementById('scope'), ctx = cv.getContext('2d');
  var elV = document.getElementById('volt'), elS = document.getElementById('state'), elC = document.getElementById('cap'),
      elP = document.getElementById('phase'), elB = document.getElementById('bar');
  var W, H, DPR;
  function size(){ DPR = Math.min(2, devicePixelRatio||1); W = cv.clientWidth; H = cv.clientHeight; cv.width = W*DPR; cv.height = H*DPR; ctx.setTransform(DPR,0,0,DPR,0,0); }
  size(); addEventListener('resize', size);

  var KV = [[0,226],[.08,178],[.2,148],[.28,232],[.34,270],[.42,280],[.5,142],[.58,150],[.8,165],[1,168]];
  var KM = [[0,.08],[.1,.3],[.2,.5],[.3,.85],[.42,1],[.5,.9],[1,.55]];
  function interp(a, p){ for (var i=1;i<a.length;i++){ if (p<=a[i][0]){ var t=(p-a[i-1][0])/(a[i][0]-a[i-1][0]); t=t*t*(3-2*t); return a[i-1][1]+(a[i][1]-a[i-1][1])*t; } } return a[a.length-1][1]; }
  function sstep(a,b,x){ var t=Math.max(0,Math.min(1,(x-a)/(b-a))); return t*t*(3-2*t); }
  var CAPS = [
    [0,   'ВЕЧЕР', 'Все включили чайники и обогреватели — сеть проседает.', 'Свет тускнеет, холодильник и насос работают на износ.'],
    [.2,  'ПРОСАДКА', 'Напряжение падает до 150 В.', 'Двигатели перегреваются, электроника перезагружается.'],
    [.32, 'СКАЧОК', 'А потом — бросок до 270 В.', 'Именно так выгорают блоки питания, платы котлов и телевизоры.'],
    [.5,  'БЕЗ ЗАЩИТЫ', 'Техника получает всё это напрямую.', 'Но так быть не должно.'],
    [.56, 'ВКЛЮЧАЕМ СПН-13500', 'Ресанта СПН-13500 выравнивает сеть.', 'Вход 90–260 В, на выходе 220 В ±8%.'],
    [.82, 'НОРМА', 'Ровные 220 В.', 'Тихо, стабильно и без нервов. Иллюстрация, не замер.']
  ];
  var cur = REDUCE ? 1 : 0, tgt = 0, t = 0, last = 0, lastCap = -1;

  function draw(now){
    requestAnimationFrame(draw);
    if (!visible(stage)) return;
    var dt = Math.min(.05, (now-last)/1000); last = now; t += dt;
    tgt = REDUCE ? 1 : sectionProgress(stage);
    cur += (tgt-cur) * (REDUCE ? 1 : .12);
    var p = cur;
    var vin = interp(KV, p), mess = interp(KM, p), k = sstep(.54, .74, p);
    var vout = vin + (220 - vin) * k, messOut = mess * (1 - k);

    ctx.clearRect(0,0,W,H);
    var top = H*.485, bot = H*.665, S = H*.058/311;
    // сетка
    ctx.lineWidth = 1; ctx.strokeStyle = 'rgba(120,180,220,.07)';
    for (var gx=0; gx<W; gx+=48){ ctx.beginPath(); ctx.moveTo(gx,0); ctx.lineTo(gx,H); ctx.stroke(); }
    for (var gy=0; gy<H; gy+=48){ ctx.beginPath(); ctx.moveTo(0,gy); ctx.lineTo(W,gy); ctx.stroke(); }
    // эталон 220 В
    ctx.setLineDash([6,8]); ctx.strokeStyle = 'rgba(68,255,154,.35)';
    [-1,1].forEach(function(s){ ctx.beginPath(); ctx.moveTo(0,bot-s*311*S); ctx.lineTo(W,bot-s*311*S); ctx.stroke(); });
    ctx.setLineDash([]);
    ctx.font = '12px Consolas,monospace'; ctx.fillStyle = 'rgba(160,190,210,.8)';
    ctx.fillText('ВХОД · СЕТЬ', 20, top-H*.075); ctx.fillText('ВЫХОД · К ВАШИМ ПРИБОРАМ', 20, bot-H*.075);

    function trace(y0, vrms, m, color, glow){
      var A = vrms*1.414*S, f = 2*Math.PI/ (W/3.2);
      ctx.beginPath();
      for (var x=0; x<=W; x+=3){
        var ph = x*f - t*5;
        var n = Math.sin(x*.043+t*7)*.5 + Math.sin(x*.117-t*11)*.3 + Math.sin(x*.31+t*17)*.2;
        var sp = Math.sin(x*.021+t*2.3) > .965 ? (Math.sin(x*.9)*1.2) : 0;
        var y = y0 - (Math.sin(ph)*A + n*m*70*S*2.4 + sp*m*150*S*1.6);
        if (x===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
      }
      ctx.lineJoin = 'round'; ctx.lineWidth = 3; ctx.strokeStyle = color; ctx.shadowColor = color; ctx.shadowBlur = glow; ctx.stroke(); ctx.shadowBlur = 0;
    }
    var colIn = vin<170 ? '#ffb224' : (vin>245 ? '#ff4d5e' : '#38f0ff');
    trace(top, vin, mess, colIn, 14);
    var dev = Math.abs(vout-220), colOut = dev<18 ? '#44ff9a' : (dev<45 ? '#ffb224' : '#ff4d5e');
    trace(bot, vout, messOut, colOut, 18);

    // показания
    var show = vout + (Math.sin(t*23)*messOut*7);
    elV.textContent = Math.round(show);
    elV.style.color = colOut;
    elS.textContent = dev<18 ? 'НОРМА' : (vout>245 ? 'ОПАСНО · ПЕРЕНАПРЯЖЕНИЕ' : (dev<45 ? 'НЕСТАБИЛЬНО' : 'ОПАСНО · ПРОСАДКА'));
    elS.style.color = colOut;
    elB.style.width = (p*100).toFixed(1)+'%';
    var ci = 0; for (var i=0;i<CAPS.length;i++) if (p>=CAPS[i][0]) ci = i;
    if (ci !== lastCap){ lastCap = ci; elP.textContent = CAPS[ci][1]; elC.innerHTML = CAPS[ci][2] + '<small>' + CAPS[ci][3] + '</small>'; }
  }
  requestAnimationFrame(draw);

  // горизонтальная секция «что под защитой»
  var hs = document.getElementById('hs'), track = document.getElementById('track');
  function hscroll(){
    var p = sectionProgress(hs), max = Math.max(0, track.scrollWidth - innerWidth + 40);
    track.style.transform = 'translate3d(' + (-p*max) + 'px,0,0)';
  }
  addEventListener('scroll', hscroll, {passive:true}); addEventListener('resize', hscroll); hscroll();
})();
"""


ANAT_SPN = [
    ("/img/rs-spn-13500.webp", "Ресанта СПН-13500", "Однофазный релейный стабилизатор на 13,5 кВт с микропроцессорным управлением. Настенное размещение, вес 21 кг."),
    ("/img/rs-spn-13500-g3.webp", "Лицевая панель", "LCD-дисплей показывает входное и выходное напряжение. На шильдике — мощность 13,5 кВт и 4,8 кВт при минимальном входе 90 В."),
    ("/img/rs-spn-13500-g1.webp", "Клеммы и вентилятор", "Подключение клеммами и принудительное охлаждение. Класс защиты IP20, рабочая температура 0…+40 °C."),
    ("/img/rs-spn-13500-g2.webp", "Задняя стенка", "Настенное крепление: на стене стабилизатор не занимает место на полу."),
    ("/img/rs-spn-13500-g4.webp", "Крепёж для монтажа", "Анкеры и шурупы для установки на стену. Установку мы не выполняем — доверьте её электрику."),
]


def page_scope():
    p = PAGES["spn-13500"]
    hero = f"""<section class="hero">
 <div class="big" aria-hidden="true">220</div>
 <div class="wrap">
  <div>
  <div class="eyebrow">Симферополь · доставка по всему Крыму</div>
  <h1>Ресанта СПН-13500: <em>ровные 220&nbsp;В</em> в любой розетке</h1>
  <p class="lead">13,5 кВт мощности и рабочий вход 90–260 В. Цена 28 990 ₽. Листайте вниз — покажем, что происходит с вашей сетью и как стабилизатор это исправляет.</p>
  <div class="hprice"><span>Цена</span><b>28 990 ₽</b></div>
  <div class="cta">
   <a class="btn btn-main" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить {B.PHONE_TEXT}</a>
   <a class="btn btn-alt tg" href="#" target="_blank" rel="noopener" data-goal="tg">Написать в Telegram</a>
  </div>
  </div>
  {pf("/img/rs-spn-13500.webp", "Стабилизатор Ресанта СПН-13500", big=True)}
 </div>
 <div class="scrollhint">листайте<i></i></div>
</section>"""
    stage = f"""
<section class="stage" id="stage" style="height:520vh">
 <div class="sticky">
  <canvas id="scope"></canvas>
  <div class="hud">
   <div>
    <div class="hud-top"><span class="chip" id="phase">ВЕЧЕР</span><span class="note">Иллюстрация, не реальный замер</span></div>
    <div class="readout"><small>Напряжение у ваших приборов</small><b id="volt">220</b><span>В</span><em id="state">НОРМА</em></div>
   </div>
   <div><p class="cap" id="cap"></p><div class="prog"><i id="bar"></i></div></div>
  </div>
 </div>
</section>

<section class="pad"><div class="wrap">
 <div class="eyebrow rv">В цифрах</div><h2 class="rv">Что умеет СПН-13500</h2>
 <div class="stats">
  <div class="stat rv"><b data-count="13.5" data-dec="1">13,5</b><span>кВт — хватает на дом целиком (при входе от 190 В)</span></div>
  <div class="stat rv d1"><b>90–260</b><span>В — рабочий диапазон на входе</span></div>
  <div class="stat rv d2"><b>±<i style="font-style:normal" data-count="8">8</i>%</b><span>точность выходных 220 В</span></div>
  <div class="stat rv d3"><b>&lt;15</b><span>мс — время регулирования; защита от перенапряжения 245 ±5 В</span></div>
 </div>
</div></section>

{anatomy(ANAT_SPN, "Разложим по полочкам")}

<section class="hs" id="hs"><div class="sticky"><div class="hs-in">
 <h2>Что вы защитите</h2>
 <div class="track" id="track">
  <div class="tcard" data-n="1"><div class="ic">⌂</div><h3>Дом и дача</h3><p>Освещение, холодильник, телевизор, стиральная машина.</p></div>
  <div class="tcard" data-n="2"><div class="ic">≈</div><h3>Насосы и скважины</h3><p>Погружные и поверхностные насосы, гидроаккумуляторы.</p></div>
  <div class="tcard" data-n="3"><div class="ic">♨</div><h3>Отопление</h3><p>Газовые и электрокотлы, циркуляционные насосы, автоматика.</p></div>
  <div class="tcard" data-n="4"><div class="ic">❄</div><h3>Кондиционеры</h3><p>Сплит-системы и другая техника с компрессором.</p></div>
 </div>
</div></div></section>
"""
    return shell(p, "spn-13500", "Ресанта СПН-13500 — стабилизатор, Симферополь, доставка по Крыму",
                 p["desc"], hero, stage, SCOPE_CSS, SCOPE_JS)


# ================================================================== СТРАНИЦА 2: «по полочкам» на настоящих фото
ANAT_15 = [
    ("/img/ex-as-15000.webp", "Expert AS-15000 — напольная модель", "15 кВт, вход 140–260 В, макс. ток 75 А. ЖК-дисплей показывает входное и выходное напряжение, а автоматический выключатель — на лицевой панели."),
    ("/img/ex-as-15000-2.webp", "Боковая стенка с вентиляцией", "Решётки отводят тепло, поэтому КПД составляет 98%, а потери и нагрев минимальны."),
    ("/img/ex-as-15000-3.webp", "Верх с ручками", "Металлические ручки для переноски. Масса AS-15000 — 16 кг, габариты 305×330×420 мм."),
    ("/img/ex-av-15000.webp", "Master AV-15000 — настенная модель", "Монтаж на стену или на пол, 310×312×167 мм, 20,5 кг. У модели есть байпас, подключение клеммами 5P."),
    ("/img/ex-av-15000-2.webp", "Лицевая панель AV-15000", "Дисплей входных и выходных параметров и кнопка управления на передней панели."),
    ("/img/ex-av-15000-3.webp", "Боковая стенка AV-15000", "Вентиляционные решётки на боковой стенке: отвод тепла при полной нагрузке 15 кВт."),
]

LAYERS_CSS = r"""
.hero .wrap{position:relative;z-index:2;padding-top:90px;padding-bottom:110px;display:grid;gap:20px;align-items:center}
@media(min-width:900px){.hero .wrap{grid-template-columns:1.05fr .95fr}}
"""


HP_BODY, HP_CSS, HP_JS = hotspots()


def page_layers():
    p = PAGES["exegate-15kvt"]
    hero = f"""<section class="hero">
 <div class="wrap">
  <div>
   <div class="eyebrow">Симферополь · доставка по всему Крыму</div>
   <h1>Exegate <em>15&nbsp;кВт</em> — защита для большого дома</h1>
   <p class="lead">Релейный стабилизатор Expert Turbo AST-15000 для большого дома, мастерской и небольшого производства. Цена 31 990 ₽. Рассмотрим его вблизи на настоящих фото: нажимайте на метки.</p>
   <div class="hprice"><span>Цена</span><b>31 990 ₽</b></div>
   <div class="cta">
    <a class="btn btn-main" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить {B.PHONE_TEXT}</a>
    <a class="btn btn-alt tg" href="#" target="_blank" rel="noopener" data-goal="tg">Написать в Telegram</a>
   </div>
  </div>
  {pf("/img/ex-ast-15000.webp", "Стабилизатор Exegate Expert Turbo AST-15000", big=True)}
 </div>
 <div class="scrollhint">листайте<i></i></div>
</section>"""
    stage = f"""
{HP_BODY}

<section class="pad"><div class="wrap">
 <div class="eyebrow rv">В цифрах</div><h2 class="rv">Expert Turbo AST-15000</h2>
 <div class="stats">
  <div class="stat rv"><b data-count="15">15</b><span>кВт мощности (15 000 ВА)</span></div>
  <div class="stat rv d1"><b>80–260</b><span>В — входное напряжение</span></div>
  <div class="stat rv d2"><b data-count="98">98</b><span>% КПД</span></div>
  <div class="stat rv d3"><b>75</b><span>А — макс. входной ток</span></div>
 </div>
</div></section>
"""
    return shell(p, "exegate-15kvt", "Стабилизатор Exegate 15 кВт — Симферополь, доставка по Крыму",
                 p["desc"], hero, stage, LAYERS_CSS + HP_CSS, HP_JS)


def main():
    out = pathlib.Path(__file__).parent / "preview"
    for name, fn in (("spn-13500-wow", page_scope), ("exegate-15kvt-wow", page_layers)):
        d = out / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(fn(), encoding="utf-8")
        print("OK", d / "index.html")


if __name__ == "__main__":
    main()
