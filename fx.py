# -*- coding: utf-8 -*-
"""Интерактивные фото для всех страниц.
 pf(...)       — вырезанное фото: парит, наклоняется за курсором, под ним свечение и тень, по клику открывается крупно;
 anatomy(...)  — «по полочкам»: настоящие ракурсы товара как слои-карусель с глубиной, управляется прокруткой.
Цвета берутся из CSS-переменных страницы: --pf-glow (свечение), --pf-rim (контурная тень), --pf-accent (акцент)."""
import html


def _e(s):
    return html.escape(s, quote=True)


PF_CSS = r"""
.pf{position:relative;display:grid;place-items:center;aspect-ratio:1/1;cursor:zoom-in;perspective:1000px;-webkit-tap-highlight-color:transparent;touch-action:pan-y}
.pf-glow{position:absolute;left:8%;right:8%;top:10%;bottom:10%;border-radius:50%;background:radial-gradient(closest-side,var(--pf-glow,rgba(255,255,255,.22)),transparent 72%);filter:blur(10px);opacity:.9;transition:transform .6s cubic-bezier(.2,.7,.2,1),opacity .6s;pointer-events:none}
.pf-floor{position:absolute;left:18%;right:18%;bottom:7%;height:8%;border-radius:50%;background:radial-gradient(closest-side,var(--pf-floor,rgba(0,0,0,.5)),transparent);filter:blur(7px);transition:transform .4s,opacity .4s;pointer-events:none}
.pf-in{position:relative;width:100%;height:100%;display:grid;place-items:center;transform-style:preserve-3d;animation:pf-float 7s ease-in-out infinite}
.pf:nth-child(2n) .pf-in{animation-delay:-2.3s}.pf:nth-child(3n) .pf-in{animation-delay:-4.1s}
@keyframes pf-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-2.2%)}}
.pf img{position:relative;width:84%;height:84%;object-fit:contain;display:block;transform:rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg)) scale(var(--s,1));transition:transform .28s cubic-bezier(.2,.7,.2,1),filter .4s;filter:drop-shadow(0 22px 20px var(--pf-rim,rgba(0,0,0,.4)));will-change:transform;user-select:none;-webkit-user-drag:none}
.pf-shine{position:absolute;inset:8%;border-radius:18px;pointer-events:none;opacity:0;transition:opacity .35s;background:radial-gradient(260px circle at var(--gx,50%) var(--gy,30%),rgba(255,255,255,.22),transparent 60%);mix-blend-mode:soft-light}
.pf:hover .pf-shine{opacity:1}
.pf:hover{--s:1.05}
.pf:hover .pf-glow{transform:scale(1.12);opacity:1}
.pf:hover .pf-floor{transform:scale(.9);opacity:.7}
.pf-hint{position:absolute;right:6%;bottom:4%;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;font-size:14px;background:var(--pf-hint-bg,rgba(255,255,255,.12));color:var(--pf-hint-fg,#fff);border:1px solid var(--pf-hint-bd,rgba(255,255,255,.3));opacity:.0;transform:scale(.8);transition:.3s;pointer-events:none;backdrop-filter:blur(6px)}
.pf:hover .pf-hint{opacity:1;transform:none}
@media(hover:none){.pf-hint{opacity:.85;transform:none}}
.pf.lg{aspect-ratio:1/1;max-width:560px;margin:0 auto}
/* лайтбокс */
.lb{position:fixed;inset:0;z-index:200;display:none;align-items:center;justify-content:center;background:rgba(6,8,10,.82);backdrop-filter:blur(14px);padding:24px;cursor:zoom-out}
.lb.on{display:flex;animation:lbin .3s ease}
@keyframes lbin{from{opacity:0}to{opacity:1}}
.lb-stage{position:relative;width:min(92vw,860px);height:min(78vh,860px);display:grid;place-items:center;overflow:hidden;border-radius:26px;background:radial-gradient(closest-side,rgba(255,255,255,.12),transparent 85%)}
.lb img{max-width:100%;max-height:100%;object-fit:contain;transform:scale(var(--z,1)) translate(var(--tx,0),var(--ty,0));transition:transform .25s ease-out;filter:drop-shadow(0 30px 40px rgba(0,0,0,.6));will-change:transform}
.lb.zoom img{--z:1.9}
.lb-cap{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:14px;color:#fff;opacity:.85;pointer-events:none}
.lb-x{position:absolute;top:18px;right:20px;width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.35);background:rgba(255,255,255,.1);color:#fff;font-size:22px;line-height:1;cursor:pointer;display:grid;place-items:center}
/* «по полочкам» */
.anat{position:relative}
.anat .sticky{position:sticky;top:0;height:100svh;overflow:hidden;display:grid;grid-template-rows:1fr auto;padding:84px 0 24px}
@media(max-width:819px){.anat .sticky{padding-bottom:84px}.al{height:min(44vh,400px);margin-top:calc(min(44vh,400px) / -2)}.al img{max-height:min(44vh,400px)}}
.anat-stage{position:relative;perspective:1400px;display:grid;place-items:center;min-height:0}
.anat-glow{position:absolute;left:50%;top:50%;width:min(80vw,760px);height:min(60vh,520px);transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(closest-side,var(--pf-glow,rgba(255,255,255,.2)),transparent 70%);filter:blur(24px);pointer-events:none}
.al{position:absolute;left:50%;top:50%;width:min(74vw,520px);height:min(52vh,440px);margin:calc(min(52vh,440px) / -2) 0 0 calc(min(74vw,520px) / -2);display:grid;place-items:center;will-change:transform,opacity;transform-style:preserve-3d;cursor:zoom-in}
.al img{max-width:min(74vw,520px);max-height:min(52vh,440px);width:auto;height:auto;object-fit:contain;filter:drop-shadow(0 26px 24px var(--pf-rim,rgba(0,0,0,.45)));transform:rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));transition:transform .25s ease-out;user-select:none;-webkit-user-drag:none}
.anat-hud{max-width:1160px;width:100%;margin:0 auto;padding:0 22px;display:grid;gap:14px;grid-template-columns:1fr;align-items:end}
@media(min-width:860px){.anat-hud{grid-template-columns:auto 1fr auto}}
.anat-num{font-size:clamp(46px,7vw,92px);line-height:.9;font-weight:700;letter-spacing:-.04em;color:var(--pf-accent,#fff);opacity:.9;font-variant-numeric:tabular-nums}
.anat-num small{font-size:.3em;opacity:.6;font-weight:500;letter-spacing:0}
.anat-txt h3{font-size:clamp(22px,3vw,34px);margin-bottom:6px}
.anat-txt p{opacity:.8;max-width:42em;font-size:15px}
.anat-dots{display:flex;gap:8px;align-items:center}
.anat-dots i{width:9px;height:9px;border-radius:50%;background:currentColor;opacity:.25;cursor:pointer;transition:.3s}
.anat-dots i.on{opacity:1;transform:scale(1.5);background:var(--pf-accent,currentColor)}
.anat-top{position:absolute;left:0;right:0;top:78px;text-align:center;font-size:12px;letter-spacing:.2em;text-transform:uppercase;opacity:.7;pointer-events:none}
@media(prefers-reduced-motion:reduce){.pf-in{animation:none}}
"""

PF_JS = r"""
(function(){
  var coarse = matchMedia('(hover: none)').matches;
  function tilt(el, img){
    el.addEventListener('pointermove', function(e){
      if (REDUCE) return;
      var r = el.getBoundingClientRect(), nx = (e.clientX-r.left)/r.width-.5, ny = (e.clientY-r.top)/r.height-.5;
      img.style.setProperty('--ry', (nx*22)+'deg'); img.style.setProperty('--rx', (-ny*16)+'deg');
      el.style.setProperty('--gx', (nx+.5)*100+'%'); el.style.setProperty('--gy', (ny+.5)*100+'%');
    });
    el.addEventListener('pointerleave', function(){ img.style.setProperty('--ry','0deg'); img.style.setProperty('--rx','0deg'); });
  }
  document.querySelectorAll('.pf').forEach(function(el){ var img = el.querySelector('img'); if (img) tilt(el, img); });

  // лайтбокс
  var lb = document.createElement('div'); lb.className = 'lb';
  lb.innerHTML = '<div class="lb-stage"><img alt=""><div class="lb-cap"></div></div><button class="lb-x" aria-label="Закрыть">×</button>';
  document.body.appendChild(lb);
  var lbi = lb.querySelector('img'), lbc = lb.querySelector('.lb-cap');
  function open(src, cap){ lbi.src = src; lbi.alt = cap||''; lbc.textContent = cap||''; lb.classList.remove('zoom'); lb.style.setProperty('--tx','0'); lb.style.setProperty('--ty','0'); lb.classList.add('on'); document.documentElement.style.overflow='hidden'; }
  function close(){ lb.classList.remove('on','zoom'); document.documentElement.style.overflow=''; }
  document.addEventListener('click', function(e){
    var t = e.target.closest('[data-zoom]');
    if (t && !lb.classList.contains('on')){ var im = t.querySelector('img'); open(t.getAttribute('data-zoom'), im ? im.alt : ''); return; }
    if (lb.classList.contains('on')){
      if (e.target.closest('.lb-x') || e.target === lb) { close(); return; }
      lb.classList.toggle('zoom');
    }
  });
  lb.addEventListener('pointermove', function(e){
    if (!lb.classList.contains('zoom')) return;
    var r = lbi.getBoundingClientRect(), nx = (e.clientX-r.left)/r.width-.5, ny = (e.clientY-r.top)/r.height-.5;
    lb.style.setProperty('--tx', (-nx*40)+'%'); lb.style.setProperty('--ty', (-ny*40)+'%');
  });
  addEventListener('keydown', function(e){ if (e.key === 'Escape') close(); });

  // «по полочкам»
  document.querySelectorAll('.anat').forEach(function(sec){
    var layers = [].slice.call(sec.querySelectorAll('.al')), dots = [].slice.call(sec.querySelectorAll('.anat-dots i'));
    var elN = sec.querySelector('.anat-num'), elT = sec.querySelector('.anat-txt h3'), elD = sec.querySelector('.anat-txt p');
    var data = layers.map(function(l){ return {t:l.dataset.t, d:l.dataset.d}; }), n = layers.length, cur = 0, tgt = 0, last = -1;
    layers.forEach(function(l){ var im = l.querySelector('img'); tilt(l, im); });
    function frame(){
      requestAnimationFrame(frame);
      if (!visible(sec)) return;
      tgt = REDUCE ? 0 : sectionProgress(sec) * (n-1);
      cur += (tgt-cur) * (REDUCE ? 1 : .1);
      layers.forEach(function(l,i){
        var d = i-cur, a = Math.abs(d), c = Math.min(a,2.2);
        var x = d*(d<0 ? 46 : 34), s = 1 - c*.13, o = Math.max(0, 1 - c*.42);
        l.style.transform = 'translate3d('+x+'%,'+(c*-3)+'%,'+(-c*140)+'px) rotateY('+(Math.max(-1,Math.min(1,d))*-26)+'deg) scale('+s+')';
        l.style.opacity = o; l.style.zIndex = 100 - Math.round(a*10); l.style.pointerEvents = a < .5 ? 'auto' : 'none';
      });
      var idx = Math.max(0, Math.min(n-1, Math.round(cur)));
      if (idx !== last){
        last = idx; elN.innerHTML = '0'+(idx+1)+'<small> / 0'+n+'</small>'; elT.textContent = data[idx].t; elD.textContent = data[idx].d;
        dots.forEach(function(x,i){ x.classList.toggle('on', i===idx); });
      }
    }
    requestAnimationFrame(frame);
    dots.forEach(function(dot,i){ dot.addEventListener('click', function(){
      var r = sec.getBoundingClientRect(), total = sec.offsetHeight - innerHeight;
      scrollTo({top: scrollY + r.top + total * (i/(n-1)) , behavior:'smooth'});
    }); });
  });
})();
"""


def pf(img, alt, zoom=None, big=False, cls=""):
    """Вырезанное интерактивное фото. zoom — крупная версия (по умолчанию то же изображение)."""
    z = zoom or img
    return (f'<div class="pf{" lg" if big else ""} {cls}" data-zoom="{_e(z)}" role="img" aria-label="{_e(alt)}">'
            f'<span class="pf-glow"></span><span class="pf-floor"></span><div class="pf-in"><img src="{_e(img)}" alt="{_e(alt)}" loading="lazy" width="560" height="560" draggable="false"></div>'
            f'<span class="pf-shine"></span><span class="pf-hint">⤢</span></div>')


def anatomy(layers, label="Разложим по полочкам", scroll_vh=95):
    """layers: список (img, заголовок, описание)."""
    n = len(layers)
    items = "".join(
        f'<div class="al" data-t="{_e(t)}" data-d="{_e(d)}" data-zoom="{_e(img)}"><img src="{_e(img)}" alt="{_e(t)}" loading="lazy" draggable="false"></div>'
        for img, t, d in layers)
    dots = "".join("<i></i>" for _ in layers)
    return (f'<section class="anat" id="anat" style="height:{100 + scroll_vh * (n - 1)}vh"><div class="sticky">'
            f'<div class="anat-top">{_e(label)} · листайте</div>'
            f'<div class="anat-stage"><div class="anat-glow"></div>{items}</div>'
            f'<div class="anat-hud"><div class="anat-num">01<small> / 0{n}</small></div>'
            f'<div class="anat-txt"><h3>{_e(layers[0][1])}</h3><p>{_e(layers[0][2])}</p></div>'
            f'<div class="anat-dots">{dots}</div></div></div></section>')
