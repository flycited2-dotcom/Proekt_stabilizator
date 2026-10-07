# -*- coding: utf-8 -*-
"""Разные интерактивы для разных страниц (каждый возвращает (html, css, js)):
 hotspots()      — метки на одном крупном фото (страница Exegate 15 кВт)
 voltage_picker  — шкала напряжения в сети: какие серии подходят (страница 10 кВт)
 calculator      — калькулятор нагрузки -> подбор модели СПН (страница Ресанта)
 series_tabs     — вкладки серий с крупным фото и параметрами (страница Exegate для дома)
 house3d         — настоящий 3D-дом на three.js (первый экран Exegate для дома)
Цвета берутся из CSS-переменных страницы: --fg, --muted, --line, --card, --pf-accent."""
import html
import json

from catalog import EX, EX_SERIES, EX_WORD, RS, ex_img, rs_img, ex_name, STOCK, STOCK_BY, money, power_text


def _e(s):
    return html.escape(s, quote=True)


# ====================================================================== МЕТКИ НА ФОТО
HOTSPOT_MODELS = [
    dict(name="AST-15000 · спереди", sub="Лицевая панель", img="/img/ex-ast-15000.webp", ratio=(834, 817), points=[
        (62, 29, "Дисплей", "Показывает входное и выходное напряжение, нагрузку и режим работы: сразу видно, что делает стабилизатор."),
        (89, 67, "Автоматический выключатель", "Включение и отключение стабилизатора (Power On / Off) прямо на лицевой панели."),
        (73, 69, "Задержка включения (Delay Reset)", "Кнопка и подписи 2 с и 6 с: после возврата напряжения в норму нагрузка включается не сразу."),
        (29, 55, "Вентиляция", "Решётки на боковой стенке отводят тепло. КПД стабилизатора — 98%."),
    ]),
    dict(name="AST-15000 · сзади", sub="Подключение", img="/img/ex-ast-15000-4.webp", ratio=(691, 900), points=[
        (26, 21, "Байпас-автомат", "Подписи «Байпас Вкл. / Выкл.»: режим, при котором нагрузка подключается напрямую к сети мимо стабилизатора."),
        (55, 25, "Две розетки 220 В", "На задней панели две евророзетки с подписью «Выход 220 В» — для подключения техники без электрика."),
        (28, 52, "Два вентилятора", "Принудительное охлаждение при работе на большой нагрузке."),
        (60, 80, "Клеммная колодка 4P", "Подписи «Вход L, N» и «Выход N, L»: сюда подключаются провода сети и нагрузки. Подключение — работа для электрика."),
        (25, 89, "Заземление", "Болт заземления на задней панели (знак G)."),
    ]),
]


def hotspots(models=HOTSPOT_MODELS):
    tabs = "".join(f'<button class="hp-tab{" on" if i == 0 else ""}" data-m="{i}">{_e(m["name"])}<small>{_e(m["sub"])}</small></button>' for i, m in enumerate(models))
    stages, lists = "", ""
    for mi, m in enumerate(models):
        w, h = m["ratio"]
        pins = "".join(
            f'<button class="hp-pin" style="left:{x}%;top:{y}%" data-i="{i}" aria-label="{_e(t)}"><span>{i + 1}</span></button>'
            for i, (x, y, t, d) in enumerate(m["points"]))
        stages += (f'<div class="hp-stage{" on" if mi == 0 else ""}" data-m="{mi}"><div class="hp-photo" style="aspect-ratio:{w}/{h}">'
                   f'<span class="hp-glow"></span><img src="{_e(m["img"])}" alt="{_e(m["name"])}" draggable="false" loading="lazy">{pins}'
                   f'<div class="hp-tip"><b></b><p></p></div></div></div>')
        items = "".join(
            f'<li data-i="{i}"><i>{i + 1}</i><div><h4>{_e(t)}</h4><p>{_e(d)}</p></div></li>' for i, (x, y, t, d) in enumerate(m["points"]))
        lists += f'<ol class="hp-list{" on" if mi == 0 else ""}" data-m="{mi}">{items}</ol>'
    body = (f'<section class="hp" id="hp"><div class="wrap"><div class="eyebrow rv">Устройство</div><h2 class="rv">Рассмотрим <em>вблизи</em></h2>'
            f'<p class="hp-sub rv">Нажимайте на цифры на фото: покажем, что есть на лицевой панели.</p>'
            f'<div class="hp-tabs rv">{tabs}</div><div class="hp-grid"><div class="hp-stages">{stages}</div><div class="hp-lists">{lists}</div></div></div></section>')
    css = r"""
.hp{padding:100px 0}
.hp-sub{color:var(--muted);margin-bottom:26px;max-width:36em}
.hp-tabs{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:30px}
.hp-tab{font:inherit;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:16px;padding:12px 20px;cursor:pointer;text-align:left;transition:.3s;display:flex;flex-direction:column;line-height:1.2}
.hp-tab small{color:var(--muted);font-size:12px;margin-top:3px}
.hp-tab.on{border-color:var(--pf-accent,#38f0ff);box-shadow:0 0 0 1px var(--pf-accent,#38f0ff),0 10px 40px -10px var(--pf-glow,rgba(56,240,255,.4))}
.hp-grid{display:grid;gap:34px;align-items:center}
@media(min-width:960px){.hp-grid{grid-template-columns:1.1fr .9fr}}
.hp-stage{display:none}.hp-stage.on{display:block;animation:hpin .6s cubic-bezier(.2,.7,.2,1)}
@keyframes hpin{from{opacity:0;transform:translateY(16px) scale(.97)}to{opacity:1;transform:none}}
.hp-photo{position:relative;width:100%;max-width:640px;margin:0 auto;perspective:1100px;transform:rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));transition:transform .3s cubic-bezier(.2,.7,.2,1);transform-style:preserve-3d}
.hp-glow{position:absolute;inset:6%;border-radius:50%;background:radial-gradient(closest-side,var(--pf-glow,rgba(56,240,255,.28)),transparent 72%);filter:blur(16px)}
.hp-photo img{position:relative;width:100%;height:100%;object-fit:contain;display:block;filter:drop-shadow(0 28px 26px var(--pf-rim,rgba(0,0,0,.5)));user-select:none;-webkit-user-drag:none}
.hp-pin{position:absolute;width:34px;height:34px;margin:-17px 0 0 -17px;border-radius:50%;border:2px solid #fff;background:var(--pf-accent,#38f0ff);color:#021218;font:700 14px/1 var(--font,system-ui);cursor:pointer;display:grid;place-items:center;z-index:3;transition:transform .25s;padding:0;transform:translateZ(30px)}
.hp-pin::after{content:"";position:absolute;inset:-9px;border-radius:50%;border:2px solid var(--pf-accent,#38f0ff);opacity:.7;animation:hpring 2.2s infinite}
@keyframes hpring{0%{transform:scale(.6);opacity:.9}100%{transform:scale(1.5);opacity:0}}
.hp-pin.on{transform:translateZ(30px) scale(1.25);background:#fff}
.hp-pin.on::after{animation-duration:1.2s}
.hp-tip{position:absolute;z-index:5;width:230px;padding:14px 16px;border-radius:16px;background:rgba(10,14,20,.92);color:#fff;border:1px solid rgba(255,255,255,.18);backdrop-filter:blur(10px);pointer-events:none;opacity:0;transform:translateY(6px);transition:.25s;font-size:13px;line-height:1.45}
.hp-tip b{display:block;font-size:15px;margin-bottom:4px}
.hp-tip p{opacity:.85;margin:0}
.hp-tip.on{opacity:1;transform:none}
@media(max-width:700px){.hp-tip{display:none}}
.hp-list{display:none;list-style:none;margin:0;padding:0}.hp-list.on{display:block}
.hp-list li{display:flex;gap:16px;padding:16px;border:1px solid transparent;border-radius:18px;cursor:pointer;transition:.3s;align-items:flex-start}
.hp-list li i{flex:0 0 32px;height:32px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-weight:700;font-size:14px;border:1.5px solid var(--pf-accent,#38f0ff);color:var(--pf-accent,#38f0ff);transition:.3s}
.hp-list li h4{font-size:17px;margin-bottom:2px;font-weight:600}
.hp-list li p{color:var(--muted);font-size:14px}
.hp-list li.on{background:var(--card);border-color:var(--line)}
.hp-list li.on i{background:var(--pf-accent,#38f0ff);color:#021218}
"""
    js = r"""
(function(){
  var sec = document.getElementById('hp'); if (!sec) return;
  var tabs = [].slice.call(sec.querySelectorAll('.hp-tab')), stages = [].slice.call(sec.querySelectorAll('.hp-stage')), lists = [].slice.call(sec.querySelectorAll('.hp-list'));
  var cur = 0, idx = 0, auto = true, timer;
  function pts(){ return [].slice.call(stages[cur].querySelectorAll('.hp-pin')); }
  function show(i){
    idx = i; var ps = pts(), li = [].slice.call(lists[cur].querySelectorAll('li')), photo = stages[cur].querySelector('.hp-photo'), tip = stages[cur].querySelector('.hp-tip');
    ps.forEach(function(p,k){ p.classList.toggle('on', k===i); }); li.forEach(function(l,k){ l.classList.toggle('on', k===i); });
    var p = ps[i], x = parseFloat(p.style.left), y = parseFloat(p.style.top), L = li[i];
    tip.querySelector('b').textContent = L.querySelector('h4').textContent; tip.querySelector('p').textContent = L.querySelector('p').textContent;
    tip.style.left = (x > 55 ? 'auto' : 'calc(' + x + '% + 28px)'); tip.style.right = (x > 55 ? 'calc(' + (100-x) + '% + 28px)' : 'auto');
    tip.style.top = 'calc(' + Math.min(Math.max(y,12),78) + '% - 30px)'; tip.classList.add('on');
  }
  function setModel(m){ cur = m; tabs.forEach(function(t,k){ t.classList.toggle('on', k===m); }); stages.forEach(function(s,k){ s.classList.toggle('on', k===m); }); lists.forEach(function(s,k){ s.classList.toggle('on', k===m); }); show(0); }
  tabs.forEach(function(t,k){ t.addEventListener('click', function(){ setModel(k); }); });
  sec.addEventListener('click', function(e){
    var pin = e.target.closest('.hp-pin'), li = e.target.closest('.hp-list li');
    if (pin || li){ auto = false; show(+(pin||li).getAttribute('data-i') || [].indexOf.call((pin||li).parentNode.children, li)); }
  });
  sec.addEventListener('mouseover', function(e){ var pin = e.target.closest('.hp-pin'); if (pin){ auto = false; show(+pin.getAttribute('data-i')); } });
  stages.forEach(function(s){ var ph = s.querySelector('.hp-photo');
    ph.addEventListener('pointermove', function(e){ if (REDUCE) return; var r = ph.getBoundingClientRect(); ph.style.setProperty('--ry', ((e.clientX-r.left)/r.width-.5)*10+'deg'); ph.style.setProperty('--rx', (-((e.clientY-r.top)/r.height-.5))*8+'deg'); });
    ph.addEventListener('pointerleave', function(){ ph.style.setProperty('--ry','0deg'); ph.style.setProperty('--rx','0deg'); }); });
  setModel(0);
  timer = setInterval(function(){ if (!auto || !visible(sec) || REDUCE) return; show((idx+1) % pts().length); }, 3200);
})();
"""
    return body, css, js


# ====================================================================== ШКАЛА НАПРЯЖЕНИЯ
VP_MODELS = ["spn-13500", "ast-15000"]


def voltage_picker():
    data = []
    for sid in VP_MODELS:
        m = STOCK_BY[sid]
        lo, hi = [int(x) for x in m["vin"].replace("–", "-").split("-")]
        data.append(dict(code=m["short"], name=m["name"], lo=lo, hi=hi, img=m["img"], mount=m["mount"], kw=float(m["kw"].replace(",", ".")), price=money(m["price"]), sid=sid))
    rows = "".join(
        f'<div class="vp-row" data-i="{i}"><div class="vp-thumb"><img src="{_e(d["img"])}" alt="{_e(d["name"])}" loading="lazy" draggable="false"></div>'
        f'<div class="vp-name"><b>{_e(d["name"])}</b><small>{_e(d["mount"])} · {d["kw"]:g} кВт · {d["price"]}</small></div>'
        f'<div class="vp-bar"><i style="left:{(d["lo"] - 40) / 240 * 100:.2f}%;width:{(d["hi"] - d["lo"]) / 240 * 100:.2f}%"></i></div>'
        f'<div class="vp-range">{d["lo"]}–{d["hi"]} В</div><div class="vp-st"></div></div>' for i, d in enumerate(data))
    ticks = "".join(f'<span style="left:{(v - 40) / 240 * 100:.2f}%">{v}</span>' for v in (40, 80, 120, 160, 200, 240, 280))
    chips = "".join(f'<button class="vp-chip" data-v="{v}">{v} В</button>' for v in (200, 160, 130, 100, 80))
    body = f"""<section class="s vp" id="vp"><div class="wrap">
 <div class="label rv">Подбор модели</div>
 <h2 class="rv">Какая у вас <em>сеть</em>?</h2>
 <p class="sub rv">Передвиньте ползунок на самое низкое напряжение, до которого проседает сеть, — покажем, какие модели справятся и сколько мощности доступно.</p>
 <div class="vp-card glass rv">
  <div class="vp-top"><div class="vp-val"><b id="vp-v">160</b><span>В</span></div>
   <div class="vp-ctl"><input type="range" id="vp-r" min="40" max="280" step="1" value="160" aria-label="Самое низкое напряжение в сети"><div class="vp-chips">{chips}</div></div></div>
  <div class="vp-axis"><div class="vp-ticks">{ticks}</div></div>
  <div class="vp-rows"><div class="vp-line" id="vp-line"></div>{rows}</div>
  <p class="vp-note">Мощность СПН-13500 при пониженном входе: по паспорту 13,5 кВт от 190 В и около 4,8 кВт при 90 В; значения между ними ориентировочные.</p>
  <div class="vp-res"><div class="vp-resimg"><img id="vp-img" src="{_e(data[0]['img'])}" alt="" draggable="false"></div>
   <div><h3 id="vp-t"></h3><div class="vp-pr" id="vp-pr"></div><p id="vp-p"></p><a class="btn btn-w" href="tel:+79785792995" data-goal="call">Подобрать модель по телефону</a></div></div>
 </div>
</div></section>"""
    css = r"""
.vp-card{padding:clamp(20px,3.4vw,40px)}
.vp-top{display:grid;gap:18px;align-items:center;margin-bottom:10px}
@media(min-width:820px){.vp-top{grid-template-columns:auto 1fr}}
.vp-val{display:flex;align-items:baseline;gap:8px}
.vp-val b{font-size:clamp(70px,11vw,120px);line-height:.9;font-weight:400;letter-spacing:-.05em;font-variant-numeric:tabular-nums;color:var(--o);text-shadow:0 0 50px rgba(var(--orgb),.45)}
.vp-val span{font-size:30px;color:var(--muted)}
#vp-r{width:100%;height:40px;-webkit-appearance:none;appearance:none;background:transparent;cursor:pointer}
#vp-r::-webkit-slider-runnable-track{height:8px;border-radius:8px;background:linear-gradient(90deg,#ff5a3c,var(--o),#ffd98a,#7dffb0)}
#vp-r::-moz-range-track{height:8px;border-radius:8px;background:linear-gradient(90deg,#ff5a3c,var(--o),#ffd98a,#7dffb0)}
#vp-r::-webkit-slider-thumb{-webkit-appearance:none;width:30px;height:30px;border-radius:50%;background:#fff;border:3px solid var(--o);margin-top:-11px;box-shadow:0 0 0 6px rgba(var(--orgb),.25),0 4px 20px rgba(0,0,0,.5)}
#vp-r::-moz-range-thumb{width:26px;height:26px;border-radius:50%;background:#fff;border:3px solid var(--o);box-shadow:0 0 0 6px rgba(var(--orgb),.25)}
.vp-chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}
.vp-chip{font:inherit;font-size:13px;color:var(--fg);background:var(--glass);border:1px solid var(--line);border-radius:99px;padding:7px 14px;cursor:pointer;transition:.25s}
.vp-chip:hover{border-color:var(--o)}
.vp-axis{position:relative;margin:6px 0 0 0}
@media(min-width:820px){.vp-axis,.vp-rows .vp-bar{--x0:0}}
.vp-ticks{position:relative;height:22px;margin-left:calc(64px + 190px + 18px);margin-right:calc(96px + 90px + 36px)}
@media(max-width:819px){.vp-ticks{display:none}}
.vp-ticks span{position:absolute;transform:translateX(-50%);font-size:11px;color:var(--muted)}
.vp-rows{position:relative;display:grid;gap:10px}
.vp-row{display:grid;grid-template-columns:64px 1fr;gap:6px 14px;align-items:center;padding:10px 12px;border-radius:18px;border:1px solid var(--line);transition:.35s}
@media(min-width:820px){.vp-row{grid-template-columns:64px 190px 1fr 96px 90px}}
.vp-thumb{width:64px;height:64px;display:grid;place-items:center;transition:.35s}
.vp-thumb img{width:100%;height:100%;object-fit:contain;filter:drop-shadow(0 8px 8px rgba(0,0,0,.5))}
.vp-name b{display:block;font-weight:500;font-size:16px}.vp-name small{color:var(--muted);font-size:12px}
.vp-bar{position:relative;height:12px;border-radius:12px;background:rgba(255,255,255,.07);grid-column:1/-1}
@media(min-width:820px){.vp-bar{grid-column:auto}}
.vp-bar i{position:absolute;top:0;bottom:0;border-radius:12px;background:var(--muted);opacity:.5;transition:.35s}
.vp-range{font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.vp-st{font-size:13px;font-weight:500}
.vp-row.ok{border-color:rgba(var(--orgb),.55);background:rgba(var(--orgb),.07);box-shadow:0 10px 40px -20px rgba(var(--orgb),.6)}
.vp-row.ok .vp-bar i{background:linear-gradient(90deg,var(--o),#ffd98a);opacity:1;box-shadow:0 0 18px rgba(var(--orgb),.7)}
.vp-row.ok .vp-st{color:#7dffb0}
.vp-row.no .vp-thumb{filter:grayscale(1);opacity:.35}.vp-row.no .vp-name,.vp-row.no .vp-range{opacity:.45}
.vp-row.no .vp-st{color:var(--muted)}
.vp-line{position:absolute;top:-6px;bottom:-6px;width:2px;background:#fff;box-shadow:0 0 14px #fff,0 0 30px var(--o);z-index:4;pointer-events:none;transition:left .15s}
@media(max-width:819px){.vp-line{display:none}}
.vp-pr{font-size:clamp(30px,4.4vw,44px);font-weight:600;letter-spacing:-.03em;color:var(--o);margin:-2px 0 8px}
.vp-note{font-size:12.5px;color:var(--muted);margin-top:12px}
.vp-res{display:grid;gap:20px;align-items:center;margin-top:26px;padding-top:24px;border-top:1px solid var(--line)}
@media(min-width:720px){.vp-res{grid-template-columns:200px 1fr}}
.vp-resimg{height:190px;display:block;position:relative;overflow:hidden}
.vp-resimg::before{content:"";position:absolute;inset:6%;border-radius:50%;background:radial-gradient(closest-side,rgba(var(--orgb),.35),transparent 72%);filter:blur(10px)}
.vp-resimg img{position:relative;height:190px;width:100%;max-width:100%;object-fit:contain;filter:drop-shadow(0 18px 18px rgba(0,0,0,.6));transition:opacity .25s,transform .35s}
.vp-res h3{font-size:clamp(22px,3vw,32px);margin-bottom:8px;font-weight:400}
.vp-res p{color:var(--muted);margin-bottom:16px;max-width:36em}
"""
    js = r"""
(function(){
  var sec = document.getElementById('vp'); if (!sec) return;
  var D = """ + json.dumps(data, ensure_ascii=False) + r""";
  var r = document.getElementById('vp-r'), v = document.getElementById('vp-v'), line = document.getElementById('vp-line'), rows = [].slice.call(sec.querySelectorAll('.vp-row'));
  var img = document.getElementById('vp-img'), t = document.getElementById('vp-t'), p = document.getElementById('vp-p'), pr = document.getElementById('vp-pr'), last = '';
  function linePos(val){
    var bar = rows[0].querySelector('.vp-bar'), box = rows[0].parentNode.getBoundingClientRect(), b = bar.getBoundingClientRect();
    line.style.left = (b.left - box.left + (val-40)/240*b.width) + 'px';
  }
  // доступная мощность СПН-13500 по паспорту: 13,5 кВт при входе от 190 В и около 4,8 кВт при 90 В (между — ориентир)
  function pw(d, val){ if (d.sid !== 'spn-13500') return null; var k = val >= 190 ? 13.5 : 4.8 + (Math.max(val,90)-90)/100*8.7; return Math.round(k*10)/10; }
  function upd(){
    var val = +r.value; v.textContent = val; var ok = [];
    D.forEach(function(d,i){
      var good = val >= d.lo, k = pw(d,val);
      rows[i].classList.toggle('ok', good); rows[i].classList.toggle('no', !good);
      rows[i].querySelector('.vp-st').textContent = good ? ('Подходит' + (k ? ' · ≈' + String(k).replace('.',',') + ' кВт' : '')) : 'Не хватает ' + (d.lo - val) + ' В';
      if (good) ok.push(d);
    });
    linePos(val);
    var key = ok.length ? ok[0].code : 'none';
    if (ok.length){
      var names = ok.map(function(d){ return d.code; }).join(' и ');
      t.textContent = 'При ' + val + ' В подойд' + (ok.length > 1 ? 'ут: ' : 'ёт: ') + names;
      var spn = ok.filter(function(d){ return d.sid === 'spn-13500'; })[0], kk = spn ? pw(spn,val) : null, msg;
      if (spn && kk < 10) msg = 'Внимание: при входе ' + val + ' В СПН-13500 отдаёт около ' + String(kk).replace('.',',') + ' кВт — для нагрузки 10 кВт этого мало' + (ok.length > 1 ? ', берите AST-15000.' : '. Позвоните — подберём вариант.');
      else if (spn) msg = 'При таком напряжении у СПН-13500 доступно около ' + String(kk).replace('.',',') + ' кВт — хватит на нагрузку 10 кВт.';
      else msg = 'AST-15000 принимает вход от 80 В. Мощность при пониженном входе уточняйте по паспорту модели.';
      p.textContent = msg;
      var pick = ok[ok.length-1]; if (spn && kk >= 10) pick = spn;
      pr.textContent = pick.name.replace('Ресанта ','Ресанта ') + ' — ' + pick.price;
      if (pick.code + val*0 !== last){ img.style.opacity = 0; img.style.transform = 'scale(.92) rotateY(20deg)'; setTimeout(function(){ img.src = pick.img; img.alt = pick.name; img.style.opacity = 1; img.style.transform = ''; }, 180); last = pick.code; }
    } else {
      pr.textContent = '';
      t.textContent = 'Такой глубокой просадке нужна особая модель';
      p.textContent = 'Модели из наличия работают от 80 В (AST-15000) и от 90 В (СПН-13500). Позвоните — подберём вариант под вашу сеть.';
      last = 'none';
    }
  }
  r.addEventListener('input', upd);
  [].forEach.call(sec.querySelectorAll('.vp-chip'), function(c){ c.addEventListener('click', function(){ r.value = c.getAttribute('data-v'); upd(); }); });
  addEventListener('resize', upd); upd(); setTimeout(upd, 400);
})();
"""
    return body, css, js


# ====================================================================== КАЛЬКУЛЯТОР НАГРУЗКИ
CALC_APPS = [
    ("Освещение (LED), комплект", 300, 0), ("Холодильник", 400, 0), ("Телевизор", 150, 0), ("Компьютер / роутер", 400, 0),
    ("Стиральная машина", 2000, 0), ("Электрочайник", 2000, 0), ("Микроволновая печь", 1200, 0), ("Бойлер (водонагреватель)", 2000, 0),
    ("Скважинный насос", 1000, 1), ("Циркуляционный насос / автоматика котла", 200, 0), ("Кондиционер", 1500, 1), ("Электроинструмент", 1500, 1),
]
CALC_PRESETS = [("Квартира", {0: 1, 1: 1, 2: 1, 3: 1}), ("Дом с насосом и котлом", {0: 2, 1: 1, 2: 2, 3: 1, 4: 1, 8: 1, 9: 1}),
                ("Большой дом", {0: 2, 1: 2, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1})]


def calculator():
    models = [dict(name=m["name"], kw=float(m["kw"].replace(",", ".")), amp=m["amp"], vin=m["vin"], disp="LCD", img=m["img"], kws=m["kw"], price=money(m["price"]))
              for m in STOCK if m["brand"] == "resanta"]
    models.sort(key=lambda x: x["kw"])
    def _w(w):
        return f"{w:,}".replace(",", " ")
    rows = "".join(
        f'<div class="cc-row" data-i="{i}"><div class="cc-n"><b>{_e(n)}</b><small>~{_w(w)} Вт{" · пусковой ток выше" if st else ""}</small></div>'
        f'<div class="cc-q"><button class="cc-m" aria-label="Меньше">−</button><output>0</output><button class="cc-p" aria-label="Больше">+</button></div></div>'
        for i, (n, w, st) in enumerate(CALC_APPS))
    pres = "".join(f'<button class="cc-pre" data-p="{i}">{_e(n)}</button>' for i, (n, _) in enumerate(CALC_PRESETS))
    body = f"""<section class="s cc" id="cc"><div class="wrap">
 <div class="label rv">Калькулятор</div>
 <h2 class="rv">Какой стабилизатор нужен <em style="font-style:normal;color:var(--o)">вам</em></h2>
 <p class="sub rv">Отметьте приборы, которые работают одновременно, — посчитаем нагрузку с запасом 30% и подберём модель СПН (3,6 или 13,5 кВт).</p>
 <div class="cc-grid">
  <div class="cc-left glass rv"><div class="cc-pres"><span>Быстрый выбор:</span>{pres}<button class="cc-pre" data-p="-1">Сбросить</button></div><div class="cc-rows">{rows}</div>
   <p class="cc-note">Значения ориентировочные, точную мощность смотрите на шильдике прибора. У насосов, кондиционеров и электроинструмента пусковой ток в 3–5 раз выше рабочего.</p></div>
  <div class="cc-right glass rv d1">
   <div class="cc-gauge"><svg viewBox="0 0 200 120"><path class="g0" d="M20 110 A80 80 0 0 1 180 110"/><path class="g1" id="cc-arc" d="M20 110 A80 80 0 0 1 180 110" pathLength="100" stroke-dasharray="0 100"/></svg>
    <div class="cc-gv"><b id="cc-w">0</b><span>Вт · с запасом <em id="cc-wr">0</em></span></div></div>
   <div class="cc-pic"><img id="cc-img" src="{_e(models[1]['img'])}" alt="" draggable="false"></div>
   <h3 id="cc-t">Отметьте приборы</h3><p id="cc-s">Слева выберите, что будет подключено к стабилизатору.</p>
   <a class="btn btn-o" id="cc-btn" href="tel:+79785792995" data-goal="call">Позвонить и уточнить цену</a>
  </div>
 </div>
</div></section>"""
    css = r"""
.cc-grid{display:grid;gap:18px;align-items:start}
@media(min-width:940px){.cc-grid{grid-template-columns:1.15fr .85fr}.cc-right{position:sticky;top:90px}}
.cc-left{padding:clamp(18px,3vw,32px)}
.cc-pres{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:18px;font-size:13px;color:var(--muted)}
.cc-pre{font:inherit;font-size:13px;color:var(--fg);background:rgba(255,255,255,.06);border:1px solid var(--line);border-radius:99px;padding:8px 15px;cursor:pointer;transition:.25s}
.cc-pre:hover{border-color:var(--o);color:#fff}
.cc-row{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 4px;border-top:1px solid var(--line);transition:.3s}
.cc-row.on{background:linear-gradient(90deg,rgba(var(--orgb),.1),transparent)}
.cc-n b{display:block;font-weight:500;font-size:15.5px}.cc-n small{color:var(--muted);font-size:12px}
.cc-q{display:flex;align-items:center;gap:6px}
.cc-q button{width:36px;height:36px;border-radius:50%;border:1px solid var(--line);background:rgba(255,255,255,.06);color:#fff;font-size:20px;line-height:1;cursor:pointer;transition:.2s;font-family:inherit}
.cc-q button:hover{border-color:var(--o);background:rgba(var(--orgb),.25)}
.cc-q output{min-width:26px;text-align:center;font-size:18px;font-weight:600;font-variant-numeric:tabular-nums}
.cc-note{font-size:12.5px;color:var(--muted);margin-top:14px}
.cc-right{padding:clamp(20px,3vw,34px);text-align:center}
.cc-gauge{position:relative;max-width:300px;margin:0 auto}
.cc-gauge svg{width:100%;display:block;overflow:visible}
.cc-gauge path{fill:none;stroke-linecap:round;stroke-width:12}
.cc-gauge .g0{stroke:rgba(255,255,255,.1)}
.cc-gauge .g1{stroke:var(--o);filter:drop-shadow(0 0 10px rgba(var(--orgb),.8));transition:stroke-dasharray .6s cubic-bezier(.2,.7,.2,1),stroke .3s}
.cc-gv{position:absolute;left:0;right:0;bottom:2px}
.cc-gv b{display:block;font-size:44px;font-weight:600;letter-spacing:-.04em;line-height:1;font-variant-numeric:tabular-nums}
.cc-gv span{font-size:12px;color:var(--muted)}.cc-gv em{font-style:normal;color:#fff}
.cc-pic{height:210px;display:block;position:relative;margin:6px 0 4px;overflow:hidden}
.cc-pic::before{content:"";position:absolute;inset:8%;border-radius:50%;background:radial-gradient(closest-side,rgba(var(--orgb),.4),transparent 72%);filter:blur(12px)}
.cc-pic img{position:relative;height:210px;width:100%;object-fit:contain;filter:drop-shadow(0 20px 18px rgba(255,45,62,.35));transition:opacity .25s,transform .4s cubic-bezier(.2,.7,.2,1)}
.cc-right h3{font-size:clamp(24px,3vw,32px);margin-bottom:6px;font-weight:600}
.cc-right p{color:var(--muted);margin-bottom:18px;font-size:15px}
"""
    js = r"""
(function(){
  var sec = document.getElementById('cc'); if (!sec) return;
  var M = """ + json.dumps(models, ensure_ascii=False) + r""", W = """ + json.dumps([w for _, w, _ in CALC_APPS]) + r""", ST = """ + json.dumps([s for _, _, s in CALC_APPS]) + r""", PRE = """ + json.dumps([p for _, p in CALC_PRESETS]) + r""";
  var rows = [].slice.call(sec.querySelectorAll('.cc-row')), q = rows.map(function(){ return 0; });
  var arc = document.getElementById('cc-arc'), w = document.getElementById('cc-w'), wr = document.getElementById('cc-wr'), img = document.getElementById('cc-img'), t = document.getElementById('cc-t'), s = document.getElementById('cc-s'), btn = document.getElementById('cc-btn'), lastM = '';
  function fmt(n){ return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,' '); }
  function upd(){
    var tot = 0, start = false; q.forEach(function(n,i){ tot += n*W[i]; if (n && ST[i]) start = true; rows[i].classList.toggle('on', n>0); rows[i].querySelector('output').textContent = n; });
    var need = tot*1.3; w.textContent = fmt(tot); wr.textContent = fmt(need) + ' Вт';
    if (!tot){ arc.setAttribute('stroke-dasharray','0 100'); t.textContent = 'Отметьте приборы'; s.textContent = 'Слева выберите, что будет подключено к стабилизатору.'; btn.textContent = 'Позвонить и подобрать'; return; }
    var m = null; for (var i=0;i<M.length;i++){ if (M[i].kw*1000 >= need){ m = M[i]; break; } }
    if (!m){
      arc.setAttribute('stroke-dasharray','100 100'); t.textContent = 'Нагрузка выше возможностей модели в наличии'; s.textContent = 'Такая нагрузка выходит за рамки моделей СПН, которые есть сейчас (до 13,5 кВт). Позвоните — подберём решение.'; btn.textContent = 'Позвонить'; return;
    }
    var pct = Math.min(100, tot/(m.kw*1000)*100); arc.setAttribute('stroke-dasharray', pct.toFixed(1) + ' 100');
    t.textContent = m.name; s.textContent = m.kws + ' кВт · макс. ток ' + m.amp + ' А · вход ' + m.vin + ' В · дисплей ' + m.disp + '. Цена ' + m.price + '. Загрузка ' + Math.round(pct) + '%' + (start ? ' (у насосов и кондиционеров пуск выше — мы заложили запас).' : '.');
    btn.textContent = 'Заказать ' + m.name.replace('Ресанта ','') + ' · ' + m.price;
    if (m.name !== lastM){ img.style.opacity = 0; img.style.transform = 'translateY(14px) scale(.9) rotateY(25deg)'; setTimeout(function(){ img.src = m.img; img.alt = m.name; img.style.opacity = 1; img.style.transform = ''; }, 200); lastM = m.name; }
  }
  rows.forEach(function(r,i){
    r.querySelector('.cc-p').addEventListener('click', function(){ q[i] = Math.min(9, q[i]+1); upd(); });
    r.querySelector('.cc-m').addEventListener('click', function(){ q[i] = Math.max(0, q[i]-1); upd(); });
  });
  [].forEach.call(sec.querySelectorAll('.cc-pre'), function(b){ b.addEventListener('click', function(){
    var p = +b.getAttribute('data-p'); q = q.map(function(){ return 0; }); if (p >= 0) Object.keys(PRE[p]).forEach(function(k){ q[+k] = PRE[p][k]; }); upd(); }); });
  upd();
})();
"""
    return body, css, js


# ====================================================================== ВКЛАДКИ МОДЕЛЕЙ
def series_tabs():
    models = [STOCK_BY[i] for i in ("ast-500", "ast-2000", "avs-2000", "ast-15000")]
    data = []
    for m in models:
        data.append(dict(code=m["short"], name=m["name"], mount=m["mount"], vin=m["vin"], vout=m["vout"], price=money(m["price"]), img=m["img"],
                         power=power_text(m), amp=m["amp"], conn=m["conn"], size=m["size"], wt=m["weight"],
                         bypass=m["bypass"], indic=m["indic"]))
    tabs = "".join(f'<button class="ts-tab{" on" if i == 0 else ""}" data-i="{i}"><b>{_e(d["code"])}</b><small>{_e(d["price"])}</small></button>' for i, d in enumerate(data))
    body = f"""<section class="s" id="series"><div class="wrap">
 <div class="eyebrow rv">Модели Exegate</div>
 <h2 class="rv">Четыре модели — от компьютера до <em>всего дома</em></h2>
 <p class="sub rv">Принцип работы одинаковый, различаются мощность, диапазон входного напряжения и монтаж. Выберите модель.</p>
 <div class="ts-tabs rv">{tabs}</div>
 <div class="ts-panel rv d1">
  <div class="ts-photo"><span class="ts-glow"></span><img id="ts-img" src="{_e(data[0]['img'])}" alt="" draggable="false"></div>
  <div class="ts-info"><div class="ts-code" id="ts-code"></div><h3 id="ts-title"></h3><p class="ts-mount" id="ts-mount"></p>
   <div class="ts-vin"><span>Вход</span><b id="ts-vin"></b><em>В</em></div>
   <div class="ts-price"><span>Цена</span><b id="ts-price"></b></div>
   <table class="ts-tb"><tr><th>Мощность</th><td id="ts-pow"></td></tr><tr><th>Макс. ток</th><td id="ts-amp"></td></tr><tr><th>Выход</th><td id="ts-vout"></td></tr><tr><th>Подключение</th><td id="ts-conn"></td></tr><tr><th>Габариты, вес</th><td id="ts-size"></td></tr><tr><th>Индикация</th><td id="ts-ind"></td></tr><tr><th>Байпас</th><td id="ts-byp"></td></tr></table>
   <a class="ghost" href="tel:+79785792995" data-goal="call"><b><svg viewBox="0 0 24 24"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg></b>Заказать</a></div>
 </div>
</div></section>"""
    css = r"""
.ts-tabs{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:22px}
.ts-tab{font:inherit;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:18px;padding:12px 22px;cursor:pointer;transition:.35s;text-align:left;display:flex;flex-direction:column;line-height:1.15}
.ts-tab b{font-family:var(--head);font-size:22px;font-weight:800}.ts-tab small{color:var(--muted);font-size:13px;margin-top:2px}
.ts-tab:hover{transform:translateY(-3px)}
.ts-tab.on{background:var(--sage-d);color:#f4f1e8;border-color:var(--sage-d);box-shadow:0 18px 40px -20px rgba(58,68,55,.7)}
.ts-tab.on small{color:rgba(244,241,232,.75)}
.ts-panel{display:grid;gap:30px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:34px;padding:clamp(22px,4vw,46px)}
@media(min-width:900px){.ts-panel{grid-template-columns:1fr 1fr}}
.ts-photo{position:relative;aspect-ratio:1/1;max-width:480px;width:100%;margin:0 auto;display:grid;place-items:center;perspective:1000px}
.ts-glow{position:absolute;inset:8%;border-radius:50%;background:radial-gradient(closest-side,rgba(255,217,160,.75),transparent 72%);filter:blur(14px)}
.ts-photo img{position:relative;width:86%;height:86%;object-fit:contain;filter:drop-shadow(0 28px 24px rgba(40,50,38,.4));transition:transform .55s cubic-bezier(.2,.7,.2,1),opacity .3s}
.ts-photo img.sw{opacity:0;transform:rotateY(70deg) scale(.85)}
.ts-code{font-family:var(--head);font-weight:800;font-size:clamp(34px,11vw,92px);line-height:.95;white-space:nowrap;color:rgba(79,91,75,.16);margin-bottom:-14px}
.ts-info h3{font-size:clamp(26px,3.4vw,38px);margin-bottom:6px}
.ts-mount{color:var(--muted);margin-bottom:16px}
.ts-vin,.ts-price{display:flex;align-items:baseline;gap:10px;padding:12px 0;border-top:1px solid var(--line)}
.ts-price{border-bottom:1px solid var(--line);margin-bottom:12px}
.ts-vin span,.ts-price span{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);min-width:64px}
.ts-vin b{font-family:var(--head);font-weight:700;font-size:clamp(30px,4vw,44px);line-height:1;color:var(--amber);font-variant-numeric:tabular-nums}
.ts-price b{font-family:var(--head);font-weight:800;font-size:clamp(32px,4.4vw,50px);line-height:1;font-variant-numeric:tabular-nums}
.ts-vin em{font-style:normal;color:var(--muted)}
.ts-tb{width:100%;border-collapse:collapse;margin-bottom:22px;background:none;border:0;border-radius:0}
.ts-tb th,.ts-tb td{padding:9px 0;border-bottom:1px solid var(--line);font-size:15px;text-align:left}
.ts-tb th{width:34%;color:var(--muted);font-weight:500}
.ghost{color:var(--ink);border-color:rgba(36,44,32,.4)}
.ts-info .ghost{color:var(--ink)}
.ts-info .ghost b{background:var(--sage-dd)}
"""
    js = r"""
(function(){
  var D = """ + json.dumps(data, ensure_ascii=False) + r""", cur = 0;
  var tabs = [].slice.call(document.querySelectorAll('.ts-tab')), img = document.getElementById('ts-img');
  if (!img) return;
  function set(id, v){ document.getElementById(id).textContent = v; }
  function render(swap){
    var d = D[cur];
    tabs.forEach(function(t,i){ t.classList.toggle('on', i===cur); });
    set('ts-code', d.code); set('ts-title', d.name); set('ts-mount', d.mount + ' монтаж'); set('ts-vin', d.vin); set('ts-price', d.price);
    set('ts-pow', d.power); set('ts-amp', d.amp + ' А'); set('ts-vout', d.vout); set('ts-conn', d.conn); set('ts-size', d.size + ' мм · ' + d.wt + ' кг'); set('ts-ind', d.indic); set('ts-byp', d.bypass ? 'Есть' : 'Нет');
    if (swap){ img.classList.add('sw'); setTimeout(function(){ img.src = d.img; img.alt = d.name; img.classList.remove('sw'); }, 260); } else { img.src = d.img; img.alt = d.name; }
  }
  tabs.forEach(function(t,i){ t.addEventListener('click', function(){ cur = i; render(true); }); });
  var ph = img.parentNode;
  ph.addEventListener('pointermove', function(e){ if (REDUCE) return; var r = ph.getBoundingClientRect(); img.style.transform = 'rotateY('+(((e.clientX-r.left)/r.width-.5)*20)+'deg) rotateX('+(-((e.clientY-r.top)/r.height-.5)*14)+'deg) scale(1.04)'; });
  ph.addEventListener('pointerleave', function(){ img.style.transform = ''; });
  render(false);
})();
"""
    return body, css, js


# ====================================================================== 3D-ДОМ (three.js)
def house3d():
    body = '<div class="h3d" id="h3d" role="img" aria-label="Современный дом, который можно вращать"><canvas id="h3d-c"></canvas><div class="h3d-hint">потяните, чтобы повернуть</div></div>'
    css = r"""
.h3d{position:relative;width:100%;height:100%;min-height:340px;cursor:grab;touch-action:pan-y}
.h3d:active{cursor:grabbing}
.h3d canvas{width:100%;height:100%;display:block}
.h3d-hint{position:absolute;left:50%;bottom:4%;transform:translateX(-50%);font-size:11px;letter-spacing:.18em;text-transform:uppercase;opacity:.7;pointer-events:none;white-space:nowrap;transition:opacity .6s}
.h3d.used .h3d-hint{opacity:0}
"""
    js = r"""
(function(){
  var host = document.getElementById('h3d'); if (!host) return;
  function boot(){
    if (!window.THREE) return;
    var T = THREE, cv = document.getElementById('h3d-c'), renderer;
    try { renderer = new T.WebGLRenderer({canvas: cv, antialias: true, alpha: true}); } catch(e){ host.style.display = 'none'; return; }
    renderer.setPixelRatio(Math.min(2, devicePixelRatio||1)); renderer.shadowMap.enabled = true; renderer.shadowMap.type = T.PCFSoftShadowMap;
    renderer.outputEncoding = T.sRGBEncoding; renderer.toneMapping = T.ACESFilmicToneMapping; renderer.toneMapping = T.NoToneMapping; renderer.toneMappingExposure = 1;
    var scene = new T.Scene(), camera = new T.PerspectiveCamera(32, 1, .1, 100);
    var root = new T.Group(); scene.add(root);
    function mat(c, o){ o = o||{}; return new T.MeshStandardMaterial(Object.assign({color:c, roughness:.85, metalness:0}, o)); }
    function box(w,h,d,m,x,y,z, cast){ var b = new T.Mesh(new T.BoxGeometry(w,h,d), m); b.position.set(x,y,z); b.castShadow = cast!==false; b.receiveShadow = true; root.add(b); return b; }
    var white = mat(0xe4e1d6,{roughness:.9}), wood = mat(0x8a5430,{roughness:.75}), dark = mat(0x23271f,{roughness:.6}), stone = mat(0xb9b9ad,{roughness:.95});
    var glow = new T.MeshStandardMaterial({color:0xff9f45, emissive:0xff7a1a, emissiveIntensity:1.15, roughness:.25, metalness:0});
    var glass = new T.MeshStandardMaterial({color:0x9fb8c4, roughness:.1, metalness:.3, transparent:true, opacity:.55});
    // остров-платформа
    var top = new T.Mesh(new T.CylinderGeometry(6.2,6.2,.35,64), mat(0x8fb27a,{roughness:1})); top.position.y = -.18; top.receiveShadow = true; root.add(top);
    var soil = new T.Mesh(new T.CylinderGeometry(6.2,4.6,1.5,64), mat(0xb08f6a,{roughness:1})); soil.position.y = -1.1; root.add(soil);
    var rock = new T.Mesh(new T.ConeGeometry(4.4,1.8,48), mat(0x8c7a64,{roughness:1})); rock.rotation.x = Math.PI; rock.position.y = -2.7; root.add(rock);
    // дорожка и терраса
    box(1.4,.06,5.2,stone,2.3,.03,2.6,false); box(5.6,.08,2.6,mat(0xd8cdb8),-.2,.04,2.7,false);
    // первый этаж
    box(6.4,2.3,3.7,white,-.3,1.2,-.3); box(6.6,.16,3.9,dark,-.3,2.42,-.3);
    // второй этаж (смещён, в дереве)
    box(4.2,2.1,3.2,wood,.7,3.5,-.5); box(4.5,.16,3.5,white,.7,4.62,-.5);
    // стёкла и свет первого этажа
    function win(w,h,x,y,z, ry, light){ var g = new T.Mesh(new T.PlaneGeometry(w,h), light ? glow : glass); g.position.set(x,y,z); g.rotation.y = ry||0; root.add(g);
      var f = new T.Mesh(new T.BoxGeometry(w+.1,h+.1,.05), dark); f.position.set(x,y,z - (ry?0:.03)); if (ry){ f.position.x = x - .03; f.scale.set(1,1,1); f.rotation.y = ry; } root.add(f); return g; }
    win(3.2,1.7,-1.3,1.25,1.57,0,true); win(1.6,1.7,1.4,1.25,1.57,0,false);
    win(2.4,1.5,.3,3.5,1.12,0,true); win(1.2,1.5,2.0,3.5,1.12,0,false);
    win(2.2,1.7,2.88,1.25,-.2,Math.PI/2,true);
    // гараж/входная панель и тёплый свет у двери
    box(.9,1.7,.12,dark,1.4,1.0,1.59);
    // лампы-сферы на террасе
    [[-3.2,.7,3.7],[2.7,.7,3.8]].forEach(function(p){ var s = new T.Mesh(new T.SphereGeometry(.2,24,16), glow); s.position.set(p[0],p[1],p[2]); root.add(s); var l = new T.PointLight(0xffc27a,.7,5); l.position.set(p[0],p[1]+.2,p[2]); root.add(l); });
    // деревья
    function tree(x,z,s){ var tr = new T.Mesh(new T.CylinderGeometry(.09*s,.13*s,.9*s,8), mat(0x6b4a30)); tr.position.set(x,.45*s,z); tr.castShadow = true; root.add(tr);
      var cr = new T.Mesh(new T.IcosahedronGeometry(.62*s,1), mat(0x5f8a52,{roughness:1})); cr.position.set(x,1.25*s,z); cr.castShadow = true; root.add(cr); }
    tree(-4.3,-1.6,1.4); tree(-4.8,1.2,1.1); tree(4.4,-2.0,1.3); tree(4.0,2.4,.9); tree(-3.4,-3.2,1.0);
    // бассейн
    var pool = new T.Mesh(new T.BoxGeometry(2.4,.05,1.3), new T.MeshStandardMaterial({color:0x6fd0e6, roughness:.1, metalness:.2, emissive:0x2a8aa5, emissiveIntensity:.35})); pool.position.set(-2.2,.06,4.1); pool.receiveShadow = true; root.add(pool);
    // освещение
    scene.add(new T.HemisphereLight(0xdfe9d4, 0x6d7a5c, .62));
    var sun = new T.DirectionalLight(0xfff0d6, .85); sun.position.set(7,10,6); sun.castShadow = true; sun.shadow.mapSize.set(1024,1024);
    var sc = sun.shadow.camera; sc.left = -9; sc.right = 9; sc.top = 9; sc.bottom = -9; sc.near = 1; sc.far = 30; sun.shadow.bias = -.0005; scene.add(sun);
    var warm = new T.PointLight(0xffb455, 1.1, 9); warm.position.set(0,2.2,.6); root.add(warm);
    var warm2 = new T.PointLight(0xffb455, .9, 8); warm2.position.set(.6,3.8,.3); root.add(warm2);
    // камера и управление
    var rotY = -.65, rotX = .0, vel = 0, drag = false, lx = 0, auto = true, t0 = performance.now();
    function size(){ var w = host.clientWidth, h = host.clientHeight; renderer.setSize(w,h,false); camera.aspect = w/h; camera.position.set(0,7.2,17.4*(w/h<1 ? 1.2 : 1)); camera.lookAt(0,.7,0); camera.updateProjectionMatrix(); }
    size(); addEventListener('resize', size);
    host.addEventListener('pointerdown', function(e){ drag = true; lx = e.clientX; vel = 0; auto = false; host.classList.add('used'); try{ host.setPointerCapture(e.pointerId); }catch(_){} });
    host.addEventListener('pointermove', function(e){ if (!drag) return; var dx = e.clientX - lx; lx = e.clientX; vel = dx*.0065; rotY += vel; });
    function end(){ drag = false; setTimeout(function(){ auto = true; }, 2200); }
    host.addEventListener('pointerup', end); host.addEventListener('pointercancel', end);
    function frame(now){
      requestAnimationFrame(frame);
      var r = host.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return;
      var t = (now - t0)/1000;
      if (!drag){ vel *= .93; rotY += vel; if (auto && !REDUCE) rotY += .0032; }
      root.rotation.y = rotY; root.position.y = REDUCE ? 0 : Math.sin(t*.9)*.18;
      warm.intensity = 1.0 + Math.sin(t*1.7)*.12; renderer.render(scene, camera);
    }
    requestAnimationFrame(frame);
  }
  var s = document.createElement('script'); s.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js'; s.onload = boot; s.onerror = function(){ host.style.display = 'none'; }; document.head.appendChild(s);
})();
"""
    return body, css, js
