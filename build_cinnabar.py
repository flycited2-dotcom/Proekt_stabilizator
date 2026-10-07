# -*- coding: utf-8 -*-
"""Страница «Cinnabar-стиль» для запроса «стабилизатор Ресанта»: багровый дым, световые следы, красные акценты в заголовке.
Запуск: python build_cinnabar.py -> preview/resanta-cinnabar/index.html"""
import pathlib

import build as B
from catalog import MODEL_IMG, RS, PRICE
from fx import pf, anatomy, PF_CSS
from widgets import calculator

CC_BODY, CC_CSS, CC_JS = calculator()
from build_wow import PAGES, COMMON_JS, e
from build_beacon import CSS as BEACON_CSS, ico

P = PAGES["resanta"]
P13 = PAGES["spn-13500"]

CSS = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');\n" + BEACON_CSS + r"""
:root{--bg:#060304;--bg2:#0a0405;--fg:#f6f1f1;--muted:#a29595;--line:rgba(255,255,255,.09);--pf-glow:rgba(255,45,62,.4);--pf-rim:rgba(255,45,62,.35);--pf-accent:#ff2d3e;--pf-floor:rgba(255,45,62,.35);--orgb:255,45,62;--o:#ff2d3e;--o2:#ff5a66;--sal:#ff3d4d;--font:'Inter','Segoe UI',system-ui,sans-serif}
body{font-weight:400}
h1,h2,h3{font-weight:600;letter-spacing:-.035em}
h2{font-size:clamp(30px,4.8vw,58px)}
.nav{padding-top:18px}
.nav-in{max-width:620px;margin:0 auto;padding:7px 8px 7px 8px;gap:4px;justify-content:center;background:rgba(14,6,8,.6)}
.nav-in .logo{display:none}
.nav a.l{white-space:nowrap;padding:9px 14px;border-radius:99px;font-size:14px;color:#d9cccc}
.nav a.l.on{background:rgba(255,255,255,.1);color:#fff}
.nav .tel{margin-left:6px}
@media(max-width:760px){.nav-in{max-width:none}.nav a.l{display:none}.nav .logo{display:flex}.nav-in{justify-content:space-between;padding-left:18px}}
.hero{justify-content:center;padding:150px 20px 80px}
.hero h1{font-size:clamp(40px,7.4vw,98px);font-weight:600;max-width:11em;margin-bottom:22px;line-height:1}
.hero h1 em{color:var(--o);text-shadow:0 0 50px rgba(255,45,62,.55)}
.hero .lead{max-width:34em}
.tagpill{display:flex;align-items:center;gap:9px;margin:0 auto 26px;padding:8px 18px;border-radius:99px;background:rgba(255,255,255,.05);border:1px solid var(--line);font-size:13px;font-weight:500;backdrop-filter:blur(8px)}
.tagpill i{width:7px;height:7px;border-radius:50%;background:var(--o);box-shadow:0 0 12px var(--o)}
.btn-w{box-shadow:0 8px 50px rgba(255,45,62,.35)}
.btn-o{background:var(--o);color:#fff}
.btn-g{background:rgba(255,255,255,.06)}
.ft2{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.big{position:relative;overflow:hidden;min-height:380px;padding:34px;display:flex;flex-direction:column;justify-content:space-between;background:linear-gradient(160deg,rgba(255,45,62,.10),rgba(255,255,255,.02) 60%);border-color:rgba(255,45,62,.22)}
.big::before{content:"";position:absolute;inset:-40% -20% auto auto;width:80%;height:80%;background:radial-gradient(closest-side,rgba(255,45,62,.28),transparent);pointer-events:none}
.big h3{font-size:clamp(26px,3.2vw,36px);line-height:1.1;margin-bottom:12px;position:relative}
.big h3 em{font-style:normal;color:var(--o)}
.big p{color:var(--muted);font-size:15px;max-width:26em;position:relative}
.stat2{position:relative;margin-top:20px;padding:18px 20px;border-radius:18px;background:rgba(0,0,0,.4);border:1px solid rgba(255,45,62,.3)}
.stat2 small{display:block;color:#ff8d95;font-size:12px;margin-bottom:8px}
.stat2 b{font-size:clamp(34px,5vw,52px);font-weight:600;letter-spacing:-.04em;line-height:1}
.stat2 span{color:var(--muted);font-size:13px;margin-left:8px}
.chart{width:100%;height:auto;margin-top:6px;overflow:visible}
.chart path.ln{fill:none;stroke:#ff3b4a;stroke-width:3;stroke-linecap:round;filter:drop-shadow(0 0 8px #ff2d3e)}
.chart path.gh{fill:none;stroke:rgba(255,45,62,.2);stroke-width:2}
.chart circle{fill:#fff;filter:drop-shadow(0 0 10px #ff2d3e)}
.pyr{display:block;margin:12px auto 0;width:min(230px,70%);height:auto;filter:drop-shadow(0 0 30px rgba(255,45,62,.55))}
.steps{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(270px,1fr))}
.st{padding:30px;position:relative;overflow:hidden}
.st b{display:block;font-size:84px;font-weight:700;line-height:.9;letter-spacing:-.05em;color:transparent;-webkit-text-stroke:1.5px rgba(255,45,62,.7);margin-bottom:18px}
.st h3{font-size:22px;margin-bottom:8px}
.st p{color:var(--muted);font-size:15px}
.price li::before{background-color:rgba(255,45,62,.2);background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m4.5 8.4 2.3 2.3 4.7-5' fill='none' stroke='%23ff2d3e' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")}
.price.hl{background:linear-gradient(180deg,rgba(255,45,62,.12),rgba(255,255,255,.03))}
.final-glow{position:absolute;left:50%;top:0;width:900px;max-width:100%;height:300px;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(255,45,62,.18),transparent);pointer-events:none}
"""

JS = r"""
(function(){
  var cv = document.getElementById('bc'), ctx = cv.getContext('2d'), hero = cv.parentNode;
  var W, H, DPR, t = 0, last = 0, mx = .5, tx = .5, blobs = [], trails = [];
  function size(){
    DPR = Math.min(2, devicePixelRatio||1); W = hero.clientWidth; H = hero.clientHeight;
    cv.width = W*DPR; cv.height = H*DPR; ctx.setTransform(DPR,0,0,DPR,0,0);
    blobs = []; var nb = W<700 ? 6 : 9;
    for (var i=0;i<nb;i++) blobs.push({x:Math.random(), y:Math.random()*.8, r:.22+Math.random()*.3, sp:.05+Math.random()*.1, ph:Math.random()*6.28, a:.16+Math.random()*.22});
    trails = []; var nt = W<700 ? 5 : 9;
    for (var j=0;j<nt;j++) trails.push(mkT(true));
  }
  function mkT(init){
    var y0 = Math.random()*.9;
    return {y0:y0, amp:.05+Math.random()*.16, k:.8+Math.random()*1.6, ph:Math.random()*6.28, p: init ? Math.random() : 0, v:.05+Math.random()*.09, len:.2+Math.random()*.28, w:.8+Math.random()*1.4, tilt:(Math.random()-.5)*.25};
  }
  size(); addEventListener('resize', size);
  hero.addEventListener('pointermove', function(e){ tx = e.clientX/innerWidth; });
  function frame(now){
    requestAnimationFrame(frame);
    if (!visible(hero)) return;
    var dt = Math.min(.05,(now-last)/1000); last = now; t += dt; mx += (tx-mx)*.04;
    ctx.globalCompositeOperation = 'source-over'; ctx.clearRect(0,0,W,H);
    // багровый дым
    var sh = (mx-.5)*(REDUCE?0:40);
    for (var i=0;i<blobs.length;i++){
      var b = blobs[i], x = (b.x + Math.sin(t*b.sp+b.ph)*.12)*W + sh, y = (b.y + Math.cos(t*b.sp*.8+b.ph)*.08)*H, r = b.r*Math.max(W,H*.9);
      var g = ctx.createRadialGradient(x,y,0,x,y,r);
      g.addColorStop(0,'rgba(190,12,32,'+b.a+')'); g.addColorStop(.5,'rgba(120,6,20,'+(b.a*.45)+')'); g.addColorStop(1,'rgba(60,2,10,0)');
      ctx.fillStyle = g; ctx.fillRect(x-r,y-r,r*2,r*2);
    }
    ctx.globalCompositeOperation = 'lighter';
    // световые следы
    for (var k=0;k<trails.length;k++){
      var T = trails[k]; T.p += T.v*dt*(REDUCE?0:1);
      if (T.p > 1+T.len){ trails[k] = mkT(false); continue; }
      var N = 120;
      for (var s=0;s<N;s++){
        var u = T.p - T.len*(s/N); if (u<0||u>1) continue;
        var x = u*(W+200)-100, y = (T.y0 + Math.sin(u*Math.PI*T.k+T.ph+t*.2)*T.amp + T.tilt*(u-.5))*H;
        var f = 1-s/N, rr = (1+T.w*2)*f;
        ctx.beginPath(); ctx.fillStyle = 'rgba(255,'+(60+Math.round(f*f*150))+','+(70+Math.round(f*f*140))+','+(.8*f*f).toFixed(3)+')';
        ctx.arc(x,y,rr,0,6.283); ctx.fill();
      }
    }
    ctx.globalCompositeOperation = 'source-over';
  }
  requestAnimationFrame(frame);
  // подсветка пункта меню по прокрутке
  var links = [].slice.call(document.querySelectorAll('.nav a.l'));
  function spy(){ var y = scrollY + innerHeight*.35, cur = links[0]; links.forEach(function(a){ var el = document.querySelector(a.getAttribute('href')); if (el && el.offsetTop <= y) cur = a; }); links.forEach(function(a){ a.classList.toggle('on', a===cur); }); }
  addEventListener('scroll', spy, {passive:true}); spy();
})();
"""

CHART = """<svg class="chart" viewBox="0 0 400 130" aria-hidden="true">
<path class="gh" d="M0 100C40 40 70 40 100 100S160 160 200 100 260 40 300 100s60 60 100 0"/>
<path class="ln" d="M0 100C40 40 70 40 100 100S160 160 200 100 260 40 300 100s60 60 100 0"/>
<circle cx="400" cy="100" r="6"/></svg>"""

PYR = """<svg class="pyr" viewBox="0 0 240 160" aria-hidden="true"><defs><linearGradient id="py" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff6a74"/><stop offset="1" stop-color="#a1081c"/></linearGradient></defs>
<g fill="none" stroke="url(#py)" stroke-width="2.4">
<ellipse cx="120" cy="140" rx="104" ry="14" fill="rgba(255,45,62,.10)"/><ellipse cx="120" cy="112" rx="82" ry="11" fill="rgba(255,45,62,.14)"/>
<ellipse cx="120" cy="86" rx="60" ry="9" fill="rgba(255,45,62,.2)"/><ellipse cx="120" cy="62" rx="38" ry="6" fill="rgba(255,45,62,.3)"/>
<path d="M120 10v44M110 22l10-12 10 12"/></g></svg>"""


def render():
    specs = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in P13["specs"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in P["faq"])
    steps = "".join(
        f'<div class="st glass rv d{i}"><b>0{i + 1}</b><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(B.STEPS))
    tiers = [
        ("Ресанта СПН-13500", "Для частного дома", True, ["13,5 кВт, макс. ток 71 А", "Вход 90–260 В, выход 220 В ±8%", "Релейный, LCD-дисплей, настенный", "Защита от перенапряжения 245 ±5 В", "Гарантия производителя 3 года"], "Заказать"),
        ("Ресанта СПН-3600", "Для квартиры и небольшого дома", False, ["3,6 кВт, макс. ток 18,9 А", "Вход 90–260 В, выход 220 В ±8%", "Релейный, LCD-дисплей, настенный"], "Заказать"),
        ("Помощь с выбором", "Бесплатно", False, ["Посчитаем нагрузку дома", "Учтём пусковые токи насосов", "Подскажем, что нужно для подключения"], "Позвонить"),
    ]
    tiers_html = ""
    for i, (n, tag, hl, items, btn) in enumerate(tiers):
        lis = "".join(f"<li>{e(x)}</li>" for x in items)
        badge = '<span class="badge">Главная модель</span>' if hl else ""
        amount = PRICE.get(n, "Консультация")
        img = MODEL_IMG.get(n)
        pic = pf(img, n) if img else f'<div class="ic">{ico("shield")}</div>'
        small = "с доставкой по Крыму — уточняйте" if n in PRICE else "позвоните — ответим сразу"
        tiers_html += (f'<div class="price glass{" hl" if hl else ""} rv d{i}">{badge}{pic}'
                       f'<h3>{e(n)}</h3><div class="t">{e(tag)}</div><div class="amount">{amount}</div>'
                       f'<small style="color:var(--muted)">{small}</small>'
                       f'<ul>{lis}</ul><a class="btn {"btn-o" if hl else "btn-g"}" href="tel:{B.PHONE_HREF}" data-goal="call">{btn}</a></div>')
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#060304">
<title>Стабилизатор Ресанта — Симферополь, доставка по Крыму</title>
<meta name="description" content="{e(P['desc'])}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23060304'/%3E%3Cpath d='M36 8 18 36h12l-4 20 20-30H34z' fill='%23ff2d3e'/%3E%3C/svg%3E">
<style>{CSS}
{PF_CSS}
.price .pf{{margin:-14px -14px 4px}}
{CC_CSS}</style>
</head>
<body>
<nav class="nav"><div class="nav-in">
 <div class="logo"><i>⚡</i> Стабилизаторы</div>
 <a class="l on" href="#top">Главная</a><a class="l" href="#why">О решении</a><a class="l" href="#how">Как заказать</a><a class="l" href="#models">Модели</a><a class="l" href="#faq">Вопросы</a>
 <a class="tel" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить</a>
</div></nav>

<header class="hero" id="top">
 <canvas id="bc"></canvas>
 <div class="tagpill"><i></i>Ресанта · Симферополь · доставка по Крыму</div>
 <h1>Простой <em>выбор</em>, надёжная <em>защита</em>, доставка по Крыму.</h1>
 <p class="lead">Стабилизаторы напряжения Ресанта СПН-3600 и СПН-13500 для квартиры и частного дома. Цены от 12 490 ₽, доставка транспортной компанией по Крыму.</p>
 <div class="cta">
  <a class="btn btn-w" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить {B.PHONE_TEXT} ↗</a>
  <a class="btn btn-g tg" href="#" target="_blank" rel="noopener" data-goal="tg">Написать в Telegram</a>
 </div>
 <div class="note">Работаем {B.HOURS}</div>
</header>

<section class="s" id="why" style="padding-top:30px"><div class="wrap">
 <div class="ft2">
  <div class="big glass rv">
   <div><h3>Реальная защита. Понятные <em>цифры.</em></h3><p>Ресанта СПН-13500 держит на выходе 220 В ±8%, даже когда сеть проседает до 90 В.</p></div>
   <div><div class="stat2"><small>Мощность СПН-13500</small><b>13,5 кВт</b><span>при входе от 190 В</span></div>{CHART}</div>
  </div>
  <div class="big glass rv d1">
   <div><h3>Прозрачные условия. Надёжный <em>сервис.</em></h3><p>Цену, наличие и сроки доставки называем сразу — по телефону или в Telegram. Без скрытых условий.</p></div>
   {PYR}
  </div>
 </div>
</div></section>

<section class="s" id="how"><div class="wrap">
 <div class="label rv">Как это работает</div>
 <h2 class="rv">Просто заказать. Надёжно <em style="font-style:normal;color:var(--o)">работает.</em></h2>
 <p class="sub rv">Три шага от звонка до получения стабилизатора.</p>
 <div class="steps">{steps}</div>
</div></section>

{CC_BODY}

<section class="s" id="models"><div class="wrap">
 <div class="label rv">Модели</div>
 <h2 class="rv">Выберите <em style="font-style:normal;color:var(--o)">свой</em> вариант</h2>
 <p class="sub rv">Две модели СПН для квартиры и частного дома. Цены с доставкой по Крыму — уточняйте по телефону.</p>
 <div class="g3">{tiers_html}</div>
</div></section>

<section class="s" id="specs"><div class="wrap">
 <div class="label rv">Характеристики</div>
 <h2 class="rv">Ресанта СПН-13500 в <em style="font-style:normal;color:var(--o)">цифрах</em></h2>
 <div class="glass rv" style="overflow:hidden"><table>{specs}</table></div>
</div></section>

<section class="s"><div class="wrap">
 <div class="glass rv" style="padding:clamp(26px,5vw,48px)">
  <div class="label" style="margin-left:0">Доставка</div>
  <h2 style="text-align:left;margin-bottom:12px">По всему Крыму и на <em style="font-style:normal;color:var(--o)">новые территории</em></h2>
  <p style="color:var(--muted);max-width:40em">Отправляем заказы транспортными компаниями — логистика налажена. Установку мы не выполняем: подключение к щитку лучше доверить электрику, а мы подскажем, что для этого нужно.</p>
 </div>
</div></section>

<section class="s" id="faq"><div class="wrap" style="max-width:820px">
 <div class="label rv">FAQ</div><h2 class="rv">Частые <em style="font-style:normal;color:var(--o)">вопросы</em></h2>{faq}
</div></section>

<section class="s" style="padding-top:20px" id="order"><div class="wrap" style="position:relative"><div class="final-glow"></div>
 <div class="lead-bar rv">
  <div><h3>Оставьте номер — <em style="font-style:normal;color:var(--o)">перезвоним</em></h3><p>Ответим по цене и наличию. Работаем {B.HOURS}.</p></div>
  <form class="form" id="lead" novalidate>
   <input type="text" name="name" placeholder="Ваше имя" autocomplete="name" maxlength="60">
   <input type="tel" name="phone" placeholder="Телефон" autocomplete="tel" inputmode="tel" required maxlength="25">
   <input type="hidden" name="comment" value="Стабилизатор Ресанта">
   <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
   <button class="btn btn-o" type="submit">Перезвоните мне</button>
   <div class="form-msg" id="lead-msg" role="status"></div>
   <div class="form-note">Нажимая кнопку, вы соглашаетесь на обработку персональных данных на условиях <a href="/privacy/">политики конфиденциальности</a>.</div>
  </form>
 </div>
</div></section>

<footer>Симферополь · доставка по Крыму и на новые территории · {B.HOURS} · установку не выполняем<br>{B.OPERATOR_SHORT}, ИНН {B.INN}, ОГРНИП {B.OGRNIP} · <a href="/privacy/">Политика конфиденциальности</a></footer>

<div class="bar">
 <a class="btn btn-w" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить</a>
 <a class="btn btn-g tg" href="#" target="_blank" rel="noopener" data-goal="tg">Telegram</a>
</div>

<script>
// Настройки: ссылка на Telegram и номер счётчика Яндекс.Метрики
var TG_URL = "https://t.me/B2B_opt_simf";
var YM_ID = "113489938";
{COMMON_JS}
{JS}
{CC_JS}
</script>
</body>
</html>
"""


def main():
    d = pathlib.Path(__file__).parent / "preview" / "resanta-cinnabar"
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(render(), encoding="utf-8")
    print("OK", d / "index.html")


if __name__ == "__main__":
    main()
