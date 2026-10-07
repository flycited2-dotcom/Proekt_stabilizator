# -*- coding: utf-8 -*-
"""Страница «Beacon-стиль» для запроса «стабилизатор для дома 10 кВт»: медный луч света, стекло, лососёвые акценты.
Запуск: python build_beacon.py -> preview/10kvt-beacon/index.html"""
import pathlib

import build as B
from catalog import MODEL_IMG, PRICE
from fx import pf, anatomy, PF_CSS
from widgets import voltage_picker

VP_BODY, VP_CSS, VP_JS = voltage_picker()
from build_wow import PAGES, COMMON_JS, e

P = PAGES["10kvt"]

CSS = r"""
:root{--bg:#050404;--bg2:#0a0706;--fg:#f5efe9;--muted:#9d9088;--line:rgba(255,255,255,.09);--glass:rgba(255,255,255,.04);--pf-glow:rgba(240,138,60,.32);--pf-rim:rgba(0,0,0,.65);--pf-accent:#f08a3c;--pf-floor:rgba(0,0,0,.65);--orgb:240,138,60;--o:#f08a3c;--o2:#ff9a52;--sal:#f7a07a;--font:'Outfit','Segoe UI',system-ui,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--fg);font-family:var(--font);font-weight:300;line-height:1.6;font-size:16px;overflow-x:hidden;padding-bottom:70px}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
h1,h2,h3{font-weight:400;letter-spacing:-.03em;line-height:1.05}
h2{font-size:clamp(32px,5.4vw,64px);text-align:center;margin-bottom:18px}
h2 em,h1 em{font-style:normal;color:var(--o)}
.sub{color:var(--muted);text-align:center;max-width:36em;margin:0 auto 44px;font-size:17px}
.label{display:flex;width:max-content;align-items:center;gap:8px;margin:0 auto 22px;padding:7px 16px;border-radius:99px;background:var(--glass);border:1px solid var(--line);font-size:13px;font-weight:400;backdrop-filter:blur(8px)}
.label::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--o);box-shadow:0 0 10px var(--o)}
/* шапка */
.nav{position:fixed;left:0;right:0;top:0;z-index:60;display:flex;justify-content:center;padding:14px 16px}
.nav-in{display:flex;align-items:center;gap:22px;width:100%;max-width:1120px;padding:10px 12px 10px 20px;border-radius:99px;background:rgba(10,7,6,.55);border:1px solid var(--line);backdrop-filter:blur(14px)}
.logo{font-weight:500;font-size:16px;display:flex;align-items:center;gap:8px;margin-right:auto;white-space:nowrap}
.logo i{color:var(--o);font-style:normal}
.nav a.l{font-size:14px;color:var(--muted);text-decoration:none;transition:color .2s}
.nav a.l:hover{color:#fff}
.tel{font-weight:500;text-decoration:none;font-size:14px;padding:9px 18px;border-radius:99px;background:#fff;color:#111;white-space:nowrap}
@media(max-width:760px){.nav a.l{display:none}.logo{font-size:13px}}
.logo{white-space:nowrap}
@media(max-width:520px){.logo span{display:none}.nav-in{padding-left:16px;gap:10px}.tel{padding:8px 14px;font-size:13px}}
/* hero */
.hero{position:relative;min-height:100svh;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;text-align:center;overflow:hidden;isolation:isolate;padding:120px 20px 74px}
.hero canvas{position:absolute;inset:0;width:100%;height:100%;z-index:-1}
.hero h1{font-size:clamp(38px,6.6vw,88px);max-width:12.5em;margin-bottom:18px;text-shadow:0 2px 40px #000}
.hero .lead{color:#cdbfb5;max-width:32em;font-size:clamp(15px,1.6vw,18px);margin-bottom:28px;text-shadow:0 1px 20px #000}
.cta{display:flex;flex-wrap:wrap;gap:12px;justify-content:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:15px 28px;border-radius:99px;font-weight:500;font-size:15px;text-decoration:none;border:0;cursor:pointer;font-family:inherit;line-height:1.2;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px)}
.btn-w{background:#fff;color:#111;box-shadow:0 8px 40px rgba(var(--orgb),.25)}
.btn-o{background:var(--sal);color:#2a1206}
.btn-g{background:var(--glass);border:1px solid var(--line);color:#fff;backdrop-filter:blur(8px)}
.note{margin-top:16px;font-size:13px;color:var(--muted)}
.pill{position:absolute;display:flex;align-items:center;gap:9px;padding:8px 16px 8px 8px;border-radius:99px;background:rgba(20,14,11,.7);border:1px solid var(--line);backdrop-filter:blur(8px);font-size:13px;font-weight:400;animation:bob 8s ease-in-out infinite;white-space:nowrap}
.pill svg{width:26px;height:26px;padding:5px;border-radius:50%;background:rgba(var(--orgb),.16);color:var(--o);stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.pill::after{content:"";position:absolute;left:50%;top:100%;width:1px;height:96px;background:linear-gradient(rgba(255,255,255,.28),transparent)}
.p1{left:3%;bottom:38%}.p2{right:3%;bottom:37%;animation-delay:-2s}.p3{left:9%;bottom:15%;animation-delay:-4s}.p4{right:9%;bottom:13%;animation-delay:-1s}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@media(max-width:1000px){.pills{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-bottom:22px}.pill{position:static;animation:none}.pill::after{display:none}}
@media(min-width:1001px){.pills{position:absolute;inset:0;pointer-events:none}}
/* секции */
section.s{padding:104px 0;position:relative}
.glass{background:var(--glass);border:1px solid var(--line);border-radius:24px;backdrop-filter:blur(8px)}
.g3{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(270px,1fr))}
.g4{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.fc{padding:28px;position:relative;overflow:hidden;transition:border-color .3s,transform .3s}
.fc:hover{border-color:rgba(var(--orgb),.5);transform:translateY(-4px)}
.fc::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;background:linear-gradient(90deg,transparent,rgba(var(--orgb),.7),transparent)}
.ic{width:50px;height:50px;border-radius:15px;background:rgba(var(--orgb),.12);border:1px solid rgba(var(--orgb),.3);display:grid;place-items:center;margin-bottom:20px;color:var(--o)}
.ic svg{width:24px;height:24px;stroke:currentColor;fill:none;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.fc h3{font-size:22px;margin-bottom:8px;font-weight:400}
.fc p{color:var(--muted);font-size:15px}
.hub{position:relative;display:grid;place-items:center;height:210px;margin-bottom:-26px}
.hub svg{width:210px;height:auto;filter:drop-shadow(0 0 40px rgba(var(--orgb),.55))}
.hub::before{content:"";position:absolute;inset:0;background:radial-gradient(closest-side,rgba(var(--orgb),.25),transparent)}
.mini{display:flex;flex-direction:column;align-items:center;gap:12px;text-align:center;padding:26px 16px}
.mini .ic{margin:0}
.mini b{font-weight:400;font-size:15px}
/* модели */
.price{padding:30px;display:flex;flex-direction:column;position:relative}
.price .pf{margin:-14px -14px 4px}
.anat{color:var(--fg)}
.anat-txt h3{font-weight:400}
.price.hl{border-color:rgba(var(--orgb),.7);box-shadow:0 0 0 1px rgba(var(--orgb),.35),0 20px 80px rgba(var(--orgb),.14);background:linear-gradient(180deg,rgba(var(--orgb),.09),rgba(255,255,255,.03))}
.badge{position:absolute;top:22px;right:22px;font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:5px 11px;border-radius:99px;background:var(--sal);color:#2a1206}
.price h3{font-size:24px;margin:16px 0 4px}
.price .t{color:var(--muted);font-size:14px;margin-bottom:18px}
.amount{font-size:34px;font-weight:400;letter-spacing:-.03em;margin-bottom:4px}
.amount small{font-size:14px;color:var(--muted);letter-spacing:0}
.price ul{list-style:none;margin:18px 0 26px;flex:1}
.price li{display:flex;gap:10px;align-items:flex-start;padding:7px 0;color:#d8ccc3;font-size:15px}
.price li::before{content:"";flex:0 0 17px;height:17px;margin-top:3px;border-radius:50%;background:rgba(var(--orgb),.2) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m4.5 8.4 2.3 2.3 4.7-5' fill='none' stroke='%23f08a3c' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/100% no-repeat}
.price .btn{width:100%}
table{width:100%;border-collapse:collapse}
th,td{text-align:left;padding:18px 24px;border-bottom:1px solid var(--line);vertical-align:top;font-size:16px}
th{width:36%;color:var(--muted);font-weight:300}
td{font-weight:400}
tr:last-child th,tr:last-child td{border-bottom:0}
details{border-bottom:1px solid var(--line);padding:22px 4px}
summary{cursor:pointer;font-weight:400;font-size:19px;list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-size:26px;line-height:1;color:var(--o)}
details[open] summary::after{content:"–"}
details p{color:var(--muted);margin-top:12px;max-width:46em}
/* заявка */
.lead-bar{display:grid;gap:18px;align-items:center;padding:30px;border-radius:26px;background:linear-gradient(120deg,rgba(var(--orgb),.13),rgba(255,255,255,.03));border:1px solid rgba(var(--orgb),.35)}
@media(min-width:900px){.lead-bar{grid-template-columns:1fr 1.25fr;padding:36px 44px}}
.lead-bar h3{font-size:clamp(26px,3.4vw,38px);margin-bottom:6px}
.lead-bar p{color:var(--muted)}
.form{display:grid;gap:10px}
@media(min-width:620px){.form{grid-template-columns:1fr 1fr auto}}
.form input{width:100%;padding:15px 18px;border-radius:99px;border:1px solid var(--line);background:rgba(0,0,0,.45);color:#fff;font:inherit;font-size:16px}
.form input:focus{outline:0;border-color:var(--o)}
.form .hp{position:absolute;left:-9999px;opacity:0}
.form-msg{font-weight:400;min-height:1.3em;grid-column:1/-1;font-size:14px}
.form-note{font-size:12px;color:var(--muted);grid-column:1/-1}
.form-note a{color:#cdbfb5}
footer{padding:34px 20px 24px;text-align:center;color:var(--muted);font-size:13px;border-top:1px solid var(--line);margin-top:40px}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:70;display:flex;gap:8px;padding:10px 12px;background:rgba(5,4,4,.92);backdrop-filter:blur(10px);border-top:1px solid var(--line)}
.bar .btn{flex:1;padding:14px 10px}
@media(min-width:820px){body{padding-bottom:0}.bar{display:none}}
.rv{opacity:0;transform:translateY(30px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}.rv.d1{transition-delay:.1s}.rv.d2{transition-delay:.2s}.rv.d3{transition-delay:.3s}
@media(prefers-reduced-motion:reduce){.pill{animation:none}.rv{opacity:1;transform:none;transition:none}}
"""

ICON = {
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "wave": '<path d="M2 12c2.5-7 5-7 7.5 0s5 7 7.5 0 3.5-5 5-3"/>',
    "gauge": '<circle cx="12" cy="13" r="8"/><path d="m12 13 4-4"/>',
    "shield": '<path d="m12 3 8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
    "truck": '<path d="M2 6h11v10H2zM13 9h4l3 3v4h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="16.5" cy="17.5" r="1.8"/>',
    "bulb": '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
    "fridge": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M6 10h12M9 6v2M9 13v3"/>',
    "tv": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8"/>',
    "washer": '<rect x="4" y="2" width="16" height="20" rx="2"/><circle cx="12" cy="14" r="5"/><path d="M8 6h.01M11 6h.01"/>',
    "drop": '<path d="M12 3c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z"/>',
    "flame": '<path d="M12 2c1 4 5 6 5 11a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-4-1-6 1-10z"/>',
    "snow": '<path d="M12 2v20M4 7l16 10M20 7 4 17"/>',
    "laptop": '<rect x="4" y="5" width="16" height="11" rx="1"/><path d="M2 20h20"/>',
}


def ico(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICON[name]}</svg>'


CUBE = """<svg viewBox="0 0 120 120" aria-hidden="true"><defs><linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffb070"/><stop offset="1" stop-color="#c24f10"/></linearGradient></defs>
<path d="M60 10 104 34v52L60 110 16 86V34z" fill="rgba(var(--orgb),.12)" stroke="url(#cg)" stroke-width="2"/>
<path d="M16 34 60 58l44-24M60 58v52" fill="none" stroke="url(#cg)" stroke-width="2"/>
<path d="M60 36 82 48v24L60 84 38 72V48z" fill="rgba(255,170,100,.35)" stroke="#ffb070" stroke-width="1.5"/></svg>"""

JS = r"""
(function(){
  var cv = document.getElementById('bc'), ctx = cv.getContext('2d'), hero = cv.parentNode;
  var W, H, DPR, mx = .5, tx = .5, t = 0, last = 0, streaks = [], ps = [];
  function gauss(){ return (Math.random()+Math.random()+Math.random()+Math.random()-2); }
  function mkP(init){ return {x:Math.random()*W, y: init ? Math.random()*H : H+10, r:.4+Math.random()*1.5, v:.2+Math.random()*.6, a:.3+Math.random()*.7, ph:Math.random()*6.28}; }
  function size(){
    DPR = Math.min(2, devicePixelRatio||1); W = hero.clientWidth; H = hero.clientHeight;
    cv.width = W*DPR; cv.height = H*DPR; ctx.setTransform(DPR,0,0,DPR,0,0);
    streaks = []; var N = W<700 ? 55 : 110;
    for (var i=0;i<N;i++) streaks.push({o:gauss()*W*.055, a:.12+Math.random()*.5, w:.5+Math.random()*1.3, ph:Math.random()*6.28, len:.45+Math.random()*.4, sp:.4+Math.random()});
    ps = []; var M = W<700 ? 45 : 90; for (var j=0;j<M;j++) ps.push(mkP(true));
  }
  size(); addEventListener('resize', size);
  hero.addEventListener('pointermove', function(e){ tx = e.clientX/innerWidth; });
  function frame(now){
    requestAnimationFrame(frame);
    if (!visible(hero)) return;
    var dt = Math.min(.05,(now-last)/1000); last = now; t += dt;
    mx += (tx-mx)*.04;
    var cx = W*.5 + (mx-.5)*(REDUCE?0:46);
    var s = Math.max(.2, 1 - scrollY/(H*1.1));
    ctx.globalCompositeOperation = 'source-over'; ctx.clearRect(0,0,W,H);
    // объёмное свечение луча
    var g = ctx.createLinearGradient(cx-W*.3,0,cx+W*.3,0);
    g.addColorStop(0,'rgba(240,110,40,0)'); g.addColorStop(.5,'rgba(240,120,45,'+(.42*s)+')'); g.addColorStop(1,'rgba(240,110,40,0)');
    ctx.fillStyle = g; ctx.fillRect(0,0,W,H);
    var m = ctx.createLinearGradient(0,0,0,H); m.addColorStop(0,'rgba(0,0,0,1)'); m.addColorStop(.38,'rgba(0,0,0,.8)'); m.addColorStop(.72,'rgba(0,0,0,.1)'); m.addColorStop(1,'rgba(0,0,0,0)');
    ctx.globalCompositeOperation = 'destination-in'; ctx.fillStyle = m; ctx.fillRect(0,0,W,H);
    ctx.globalCompositeOperation = 'lighter';
    // тонкие лучики (волокна)
    var lg = ctx.createLinearGradient(0,0,0,H*.9); lg.addColorStop(0,'rgba(255,170,90,1)'); lg.addColorStop(.55,'rgba(240,120,45,.55)'); lg.addColorStop(1,'rgba(240,100,30,0)');
    ctx.strokeStyle = lg;
    for (var i=0;i<streaks.length;i++){
      var k = streaks[i], x = cx + k.o + Math.sin(t*.35*k.sp+k.ph)*5;
      var fall = Math.exp(-Math.abs(k.o)/(W*.06));
      ctx.globalAlpha = Math.min(1, k.a*fall*(.55+.45*Math.sin(t*.9*k.sp+k.ph))*s*1.5);
      ctx.lineWidth = k.w; ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,H*(.5+k.len*.4)); ctx.stroke();
    }
    ctx.globalAlpha = 1;
    // ядро
    var cg = ctx.createLinearGradient(0,0,0,H*.8); cg.addColorStop(0,'rgba(255,225,190,'+(.85*s)+')'); cg.addColorStop(.5,'rgba(255,160,80,'+(.4*s)+')'); cg.addColorStop(1,'rgba(255,140,60,0)');
    ctx.fillStyle = cg; ctx.fillRect(cx-2,0,4,H*.8);
    var cg2 = ctx.createLinearGradient(cx-40,0,cx+40,0); cg2.addColorStop(0,'rgba(255,150,70,0)'); cg2.addColorStop(.5,'rgba(255,160,80,'+(.2*s)+')'); cg2.addColorStop(1,'rgba(255,150,70,0)');
    ctx.fillStyle = cg2; ctx.fillRect(cx-40,0,80,H*.7);
    // свечение сверху
    var tg = ctx.createRadialGradient(cx,0,0,cx,0,W*.3); tg.addColorStop(0,'rgba(255,170,90,'+(.5*s)+')'); tg.addColorStop(1,'rgba(255,140,60,0)');
    ctx.fillStyle = tg; ctx.fillRect(0,0,W,H*.5);
    // «горизонт»: волны внизу
    var base = H*.9;
    var hg = ctx.createRadialGradient(cx,H,0,cx,H,W*.55); hg.addColorStop(0,'rgba(240,110,40,.32)'); hg.addColorStop(1,'rgba(240,110,40,0)');
    ctx.fillStyle = hg; ctx.fillRect(0,H*.55,W,H*.45);
    for (var w=0; w<7; w++){
      ctx.beginPath();
      for (var x=0; x<=W; x+=6){
        var amp = H*.03*(1-w*.1), dx = (x-cx)/W;
        var y = base + w*H*.012 + Math.sin(x*.0042*(1+w*.12) + t*(.25+w*.05) + w*.9)*amp*(1-Math.abs(dx)*.6);
        if (x===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
      }
      ctx.lineWidth = w<2 ? 1.6 : 1; ctx.strokeStyle = 'rgba(255,'+(130+w*8)+',60,'+(.6-w*.07)+')';
      ctx.shadowColor = 'rgba(255,120,40,.9)'; ctx.shadowBlur = 14; ctx.stroke(); ctx.shadowBlur = 0;
    }
    // частицы
    for (var p=0;p<ps.length;p++){
      var q = ps[p]; q.y -= q.v*dt*60*(REDUCE?0:1); q.x += Math.sin(t*.7+q.ph)*.2 + (cx-q.x)*.0006;
      if (q.y < -10){ ps[p] = mkP(false); continue; }
      var b = Math.exp(-Math.abs(q.x-cx)/(W*.16));
      var al = Math.min(1, q.a*(.5+.5*Math.sin(t*1.8+q.ph))*(.25+1.2*b)*s);
      ctx.beginPath(); ctx.fillStyle = 'rgba(255,'+(150+Math.round(b*60))+',80,'+al.toFixed(3)+')';
      ctx.arc(q.x,q.y,q.r*(1+b*.5),0,6.283); ctx.fill();
    }
    ctx.globalCompositeOperation = 'source-over';
  }
  requestAnimationFrame(frame);
})();
"""


def render():
    specs = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in P["specs"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in P["faq"])
    how = [
        ("wave", "Сеть «плавает»", "Вечером напряжение проседает, днём прыгает. Стабилизатор принимает на входе от 80 до 260 В — в зависимости от модели."),
        ("bolt", "Реле выравнивает", "Релейная схема переключает ступени за считанные миллисекунды — быстрее, чем вы моргнёте."),
        ("shield", "Ровные 220 В на выходе", "Точность ±8% и КПД до 98%. Защита от перенапряжения, перегрева и короткого замыкания."),
    ]
    how_html = "".join(
        f'<div class="fc glass rv d{i}"><div class="ic">{ico(n)}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>'
        for i, (n, t, d) in enumerate(how))
    apps = [("bulb", "Освещение"), ("fridge", "Холодильник"), ("tv", "Телевизор"), ("washer", "Стиральная машина"),
            ("drop", "Насос и скважина"), ("flame", "Котёл"), ("snow", "Кондиционер"), ("laptop", "Компьютер и роутер")]
    apps_html = "".join(f'<div class="glass mini rv"><div class="ic">{ico(n)}</div><b>{e(t)}</b></div>' for n, t in apps)
    prices = []
    for i, (name, tag, items) in enumerate(P["models"]):
        hl = " hl" if i == 0 else ""
        badge = ""
        lis = "".join(f"<li>{e(x)}</li>" for x in items)
        btn = "btn-o" if i == 0 else "btn-g"
        img = MODEL_IMG.get(name)
        pic = pf(img, name) if img else ""
        prices.append(f'<div class="price glass{hl} rv d{i%3}">{badge}{pic}<h3>{e(name)}</h3><div class="t">{e(tag)}</div>'
                      f'<div class="amount">{PRICE.get(name, "Цена по запросу")}</div><small style="color:var(--muted)">с доставкой по Крыму — уточняйте</small>'
                      f'<ul>{lis}</ul><a class="btn {btn}" href="tel:{B.PHONE_HREF}" data-goal="call">Заказать</a></div>')
    pills = (f'<span class="pill p1">{ico("wave")}Вход 80–260 В</span><span class="pill p2">{ico("bolt")}13,5 и 15 кВт</span>'
             f'<span class="pill p3">{ico("gauge")}от 28 990 ₽</span><span class="pill p4">{ico("truck")}Доставка по Крыму</span>')
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#050404">
<title>Стабилизатор для дома 10 кВт — Симферополь, доставка по Крыму</title>
<meta name="description" content="{e(P['desc'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23050404'/%3E%3Cpath d='M36 8 18 36h12l-4 20 20-30H34z' fill='%23f08a3c'/%3E%3C/svg%3E">
<style>{CSS}
{PF_CSS}
{VP_CSS}</style>
</head>
<body>
<nav class="nav"><div class="nav-in">
 <div class="logo"><i>⚡</i> Стабилизаторы<span>&nbsp;· Симферополь</span></div>
 <a class="l" href="#how">Как работает</a><a class="l" href="#models">Модели</a><a class="l" href="#specs">Характеристики</a><a class="l" href="#faq">Вопросы</a>
 <a class="tel" href="tel:{B.PHONE_HREF}" data-goal="call">{B.PHONE_TEXT}</a>
</div></nav>

<header class="hero" id="top">
 <canvas id="bc"></canvas>
 <div class="pills">{pills}</div>
 <h1>Свет в доме <em>не мигает</em>.<br>Даже когда сеть шалит.</h1>
 <p class="lead">Для нагрузки 10 кВт берут модель с запасом: Ресанта СПН-13500 на 13,5 кВт и Exegate AST-15000 на 15 кВт. Свет, котёл, насос и кондиционер под защитой.</p>
 <div class="cta">
  <a class="btn btn-w" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить {B.PHONE_TEXT} ↗</a>
  <a class="btn btn-g tg" href="#" target="_blank" rel="noopener" data-goal="tg">Написать в Telegram</a>
 </div>
 <div class="note">Работаем {B.HOURS} · доставка по Крыму и на новые территории</div>
</header>

<section class="s" id="how"><div class="wrap">
 <div class="label rv">Как это работает</div>
 <h2 class="rv">Три шага от сети до <em>розетки</em></h2>
 <p class="sub rv">Стабилизатор стоит между сетью и вашими приборами и делает всю работу незаметно.</p>
 <div class="g3">{how_html}</div>
</div></section>

<section class="s" style="padding-top:20px"><div class="wrap">
 <div class="label rv">Что подключить</div>
 <h2 class="rv">Всё, что работает <em>от розетки</em></h2>
 <div class="hub rv">{CUBE}</div>
 <div class="g4">{apps_html}</div>
</div></section>

{VP_BODY}

<section class="s" id="models"><div class="wrap">
 <div class="label rv">Модели</div>
 <h2 class="rv">Две модели <em>с запасом</em></h2>
 <p class="sub rv">Обе подходят для дома на 10 кВт: выбирайте по месту установки и сети.</p>
 <div class="g3">{''.join(prices)}</div>
</div></section>

<section class="s" id="specs"><div class="wrap">
 <div class="label rv">Характеристики</div>
 <h2 class="rv">Что внутри <em>цифр</em></h2>
 <div class="glass rv" style="overflow:hidden"><table>{specs}</table></div>
</div></section>

<section class="s"><div class="wrap">
 <div class="glass rv" style="padding:clamp(26px,5vw,48px)">
  <div class="label" style="margin-left:0">Доставка</div>
  <h2 style="text-align:left;margin-bottom:12px">По всему Крыму и на <em>новые территории</em></h2>
  <p style="color:var(--muted);max-width:40em">Отправляем заказы транспортными компаниями — логистика налажена. Установку мы не выполняем: подключение к щитку лучше доверить электрику, а мы подскажем, что для этого нужно.</p>
 </div>
</div></section>

<section class="s" id="faq"><div class="wrap" style="max-width:820px">
 <div class="label rv">FAQ</div><h2 class="rv">Частые <em>вопросы</em></h2>{faq}
</div></section>

<section class="s" style="padding-top:20px" id="order"><div class="wrap">
 <div class="lead-bar rv">
  <div><h3>Оставьте номер — <em style="font-style:normal;color:var(--o)">перезвоним</em></h3><p>Ответим по цене и наличию. Работаем {B.HOURS}.</p></div>
  <form class="form" id="lead" novalidate>
   <input type="text" name="name" placeholder="Ваше имя" autocomplete="name" maxlength="60">
   <input type="tel" name="phone" placeholder="Телефон" autocomplete="tel" inputmode="tel" required maxlength="25">
   <input type="hidden" name="comment" value="Стабилизатор 10 кВт">
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
{VP_JS}
</script>
</body>
</html>
"""


def main():
    d = pathlib.Path(__file__).parent / "preview" / "10kvt-beacon"
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(render(), encoding="utf-8")
    print("OK", d / "index.html")


if __name__ == "__main__":
    main()
