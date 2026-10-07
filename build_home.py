# -*- coding: utf-8 -*-
"""Главная страница oasis.com.ru: WebGL-шейдер «полёт сквозь огни» + карточки с анимированной рамкой (в духе UIverse).
Запуск через make_all.py (кладёт результат в site/index.html)."""
import html
import pathlib

import build as B
from build_wow import COMMON_JS
from catalog import STOCK, money, power_text

ROOT = pathlib.Path(__file__).parent


def e(s):
    return html.escape(s, quote=True)


CARDS = [
    dict(slug="resanta", title="Стабилизатор Ресанта", sub="СПН-3600 и СПН-13500: для квартиры и частного дома", price="от 12 490 ₽", img="/img/rs-spn-3600.webp", tag="Ресанта"),
    dict(slug="10kvt", title="Стабилизатор для дома 10 кВт", sub="Модели с запасом мощности: 13,5 и 15 кВт", price="от 28 990 ₽", img="/img/rs-spn-13500.webp", tag="10 кВт"),
    dict(slug="spn-13500", title="Ресанта СПН-13500", sub="13,5 кВт, вход 90–260 В, гарантия 3 года", price="28 990 ₽", img="/img/rs-spn-13500-g3.webp", tag="13,5 кВт"),
    dict(slug="exegate", title="Стабилизатор Exegate для дома", sub="AST-500, AST-2000, AVS-2000 и AST-15000", price="от 3 190 ₽", img="/img/ex-ast-2000.webp", tag="Exegate"),
    dict(slug="exegate-15kvt", title="Стабилизатор Exegate 15 кВт", sub="Expert Turbo AST-15000 с байпасом", price="31 990 ₽", img="/img/ex-ast-15000.webp", tag="15 кВт"),
]
PAGE_OF = {"ast-500": "exegate", "ast-2000": "exegate", "avs-2000": "exegate", "ast-15000": "exegate-15kvt", "spn-3600": "resanta", "spn-13500": "spn-13500"}

CSS = r"""
@property --ang{syntax:'<angle>';initial-value:0deg;inherits:false}
:root{--bg:#04060a;--fg:#eef4f8;--muted:#8d9db0;--line:rgba(255,255,255,.1);--cy:#38f0ff;--am:#ffb347;--gr:#44ff9a;--font:'Manrope','Segoe UI',system-ui,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--fg);font-family:var(--font);font-size:16px;line-height:1.6;overflow-x:hidden;padding-bottom:70px}
a{color:inherit}
#fx{position:fixed;inset:0;width:100%;height:100%;z-index:-2;display:block;background:radial-gradient(900px circle at 50% 30%,#0b1623,#04060a)}
.veil{position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(1200px circle at 50% 40%,rgba(4,6,10,.15),rgba(4,6,10,.72) 70%),linear-gradient(rgba(4,6,10,.0),rgba(4,6,10,.55))}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}
h1,h2,h3{font-weight:800;letter-spacing:-.035em;line-height:1.04}
h2{font-size:clamp(30px,5vw,54px);margin-bottom:14px}
h2 em,h1 em{font-style:normal;background:linear-gradient(90deg,var(--cy),var(--gr));-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{color:var(--muted);max-width:38em;margin-bottom:38px;font-size:17px}
.eyebrow{display:inline-flex;align-items:center;gap:9px;padding:7px 15px;border-radius:99px;border:1px solid var(--line);background:rgba(255,255,255,.05);backdrop-filter:blur(10px);font-size:13px;font-weight:600;margin-bottom:22px}
.eyebrow::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--gr);box-shadow:0 0 12px var(--gr);animation:blink 2s infinite}
@keyframes blink{50%{opacity:.35}}
/* шапка */
.nav{position:fixed;left:0;right:0;top:0;z-index:60;display:flex;justify-content:center;padding:14px 16px}
.nav-in{display:flex;align-items:center;gap:22px;width:100%;max-width:1160px;padding:9px 10px 9px 20px;border-radius:99px;background:rgba(8,12,18,.55);border:1px solid var(--line);backdrop-filter:blur(16px)}
.logo{font-weight:800;letter-spacing:-.02em;display:flex;align-items:center;gap:8px;margin-right:auto;white-space:nowrap}
.logo i{color:var(--cy);font-style:normal}
.nav a.l{font-size:14px;color:var(--muted);text-decoration:none;transition:.2s}.nav a.l:hover{color:#fff}
@media(max-width:820px){.nav a.l{display:none}.logo{font-size:14px}}
.nav .btn{white-space:nowrap}
@media(max-width:480px){.logo span{display:none}.nav-in{padding-left:16px}}
/* кнопки (shine) */
.btn{position:relative;overflow:hidden;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:15px 28px;border-radius:99px;font-family:inherit;font-weight:700;font-size:15px;text-decoration:none;border:0;cursor:pointer;line-height:1.2;transition:transform .25s,box-shadow .25s;isolation:isolate}
.btn:hover{transform:translateY(-2px)}
.btn-main{background:linear-gradient(135deg,var(--cy),#7dffd0);color:#02161c;box-shadow:0 0 0 0 rgba(56,240,255,.5),0 10px 40px -8px rgba(56,240,255,.55);animation:pulse 2.6s infinite}
.btn-main::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.65),transparent);transform:skewX(-20deg);animation:shine 3.4s infinite;z-index:-1}
@keyframes shine{0%,55%{left:-60%}100%{left:130%}}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(56,240,255,.45),0 10px 40px -8px rgba(56,240,255,.55)}70%{box-shadow:0 0 0 16px rgba(56,240,255,0),0 10px 40px -8px rgba(56,240,255,.55)}100%{box-shadow:0 0 0 0 rgba(56,240,255,0),0 10px 40px -8px rgba(56,240,255,.55)}}
.btn-ghost{background:rgba(255,255,255,.06);color:#fff;border:1px solid var(--line);backdrop-filter:blur(10px)}
.btn-ghost:hover{border-color:var(--cy);box-shadow:0 0 30px -6px rgba(56,240,255,.5)}
.cta{display:flex;flex-wrap:wrap;gap:12px}
/* hero */
.hero{min-height:100svh;display:flex;align-items:center;padding:120px 0 90px}
.hero h1{font-size:clamp(40px,8vw,104px);max-width:11em;margin-bottom:22px;text-shadow:0 4px 60px rgba(0,0,0,.6)}
.lead{font-size:clamp(17px,2.2vw,21px);color:#c4d0dc;max-width:34em;margin-bottom:30px;text-shadow:0 2px 24px rgba(0,0,0,.7)}
.hint{margin-top:18px;font-size:13px;color:var(--muted)}
.scrollhint{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.scrollhint i{width:1.5px;height:34px;background:linear-gradient(var(--cy),transparent);animation:drip 1.8s infinite}
@keyframes drip{0%{transform:scaleY(0);transform-origin:top}50%{transform:scaleY(1);transform-origin:top}51%{transform-origin:bottom}100%{transform:scaleY(0);transform-origin:bottom}}
section.s{padding:96px 0;position:relative}
/* карточки с анимированной рамкой */
.cards{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.gc{position:relative;display:flex;flex-direction:column;border-radius:26px;padding:2px;text-decoration:none;background:conic-gradient(from var(--ang),transparent 0 70%,var(--cy) 85%,var(--gr) 92%,transparent 100%);animation:spin 5s linear infinite;transition:transform .35s cubic-bezier(.2,.7,.2,1),filter .35s}
.gc:nth-child(2n){animation-duration:6.5s;animation-direction:reverse}
.gc:nth-child(3n){--c1:var(--am);background:conic-gradient(from var(--ang),transparent 0 70%,var(--am) 86%,#ff7a45 94%,transparent 100%)}
@keyframes spin{to{--ang:360deg}}
.gc:hover{transform:translateY(-6px) scale(1.01);filter:drop-shadow(0 18px 40px rgba(56,240,255,.28))}
.gc-in{position:relative;flex:1;display:flex;flex-direction:column;border-radius:24px;padding:22px;background:linear-gradient(180deg,rgba(14,22,32,.92),rgba(8,12,18,.94));backdrop-filter:blur(12px);overflow:hidden}
.gc-in::before{content:"";position:absolute;width:300px;height:300px;left:var(--mx,50%);top:var(--my,0%);transform:translate(-50%,-50%);background:radial-gradient(closest-side,rgba(56,240,255,.22),transparent);opacity:0;transition:opacity .3s;pointer-events:none}
.gc:hover .gc-in::before{opacity:1}
.gc-tag{align-self:flex-start;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:5px 11px;border-radius:99px;background:rgba(56,240,255,.12);color:var(--cy);border:1px solid rgba(56,240,255,.3)}
.gc-pic{position:relative;height:190px;margin:8px 0 6px;display:block;perspective:800px;flex:0 0 190px}
.gc-pic::before{content:"";position:absolute;inset:10% 12%;border-radius:50%;background:radial-gradient(closest-side,rgba(56,240,255,.28),transparent 72%);filter:blur(10px)}
.gc-pic img{position:relative;display:block;height:190px;width:100%;max-width:100%;object-fit:contain;filter:drop-shadow(0 18px 18px rgba(0,0,0,.65));transform:rotateY(var(--ry,0deg)) rotateX(var(--rx,0deg)) scale(var(--s,1));transition:transform .3s cubic-bezier(.2,.7,.2,1)}
.gc:hover .gc-pic img{--s:1.06}
.gc h3{font-size:22px;margin-bottom:6px}
.gc p{color:var(--muted);font-size:14.5px;flex:1}
.gc-bot{display:flex;align-items:center;justify-content:space-between;margin-top:16px;padding-top:14px;border-top:1px solid var(--line)}
.gc-price{font-size:22px;font-weight:800;letter-spacing:-.02em}
.gc-go{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.07);border:1px solid var(--line);transition:.3s}
.gc:hover .gc-go{background:var(--cy);color:#02161c;transform:translateX(4px)}
/* модели */
.models{display:flex;gap:14px;overflow-x:auto;padding:6px 4px 18px;scroll-snap-type:x mandatory;scrollbar-width:thin}
.mc{flex:0 0 min(78vw,230px);scroll-snap-align:start;text-decoration:none;border-radius:20px;padding:16px;background:rgba(255,255,255,.04);border:1px solid var(--line);backdrop-filter:blur(10px);transition:.3s;display:flex;flex-direction:column}
.mc:hover{border-color:var(--cy);transform:translateY(-4px);box-shadow:0 20px 50px -20px rgba(56,240,255,.45)}
.mc img{display:block;height:120px;width:100%;max-width:100%;flex:0 0 120px;object-fit:contain;filter:drop-shadow(0 12px 12px rgba(0,0,0,.6));margin-bottom:10px}
.mc b{font-size:15px;line-height:1.25;display:block;min-height:2.5em}
.mc small{color:var(--muted);font-size:12.5px}
.mc em{font-style:normal;font-size:20px;font-weight:800;margin-top:8px;color:var(--cy)}
/* гармошка моделей */
.acc{display:flex;gap:12px;height:480px}
.ac{position:relative;flex:1 1 0;min-width:0;border-radius:26px;overflow:hidden;text-decoration:none;color:inherit;background:linear-gradient(180deg,rgba(16,24,34,.9),rgba(8,12,18,.94));border:1px solid var(--line);backdrop-filter:blur(12px);transition:flex-grow .7s cubic-bezier(.2,.8,.2,1),border-color .4s,box-shadow .4s}
.ac.on{flex-grow:8;border-color:rgba(56,240,255,.55);box-shadow:0 30px 70px -30px rgba(56,240,255,.5)}
.ac-rail{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:24px 4px 22px;transition:opacity .35s}
.ac.on .ac-rail{opacity:0;pointer-events:none}
.ac-n{font-size:26px;font-weight:800;color:var(--cy);letter-spacing:-.02em;text-shadow:0 0 18px rgba(56,240,255,.55);line-height:1}
.ac-v{writing-mode:vertical-rl;transform:rotate(180deg);font-size:21px;font-weight:800;letter-spacing:-.01em;white-space:nowrap}
.ac-p{writing-mode:vertical-rl;transform:rotate(180deg);font-size:27px;font-weight:800;color:#ffb21e;letter-spacing:-.02em;white-space:nowrap;padding:10px 0 2px;text-shadow:0 0 22px rgba(255,170,30,.6),0 0 2px rgba(255,200,80,.8)}
.ac:not(.on):hover{border-color:rgba(56,240,255,.35)}
.ac-body{position:absolute;inset:0;display:grid;grid-template-columns:1.05fr 1fr;gap:10px;align-items:center;padding:26px 30px;opacity:0;transform:translateX(24px);transition:opacity .5s .25s,transform .6s .2s cubic-bezier(.2,.8,.2,1)}
.ac.on .ac-body{opacity:1;transform:none}
.ac-pic{position:relative;height:100%;max-height:380px;display:grid;place-items:center}
.ac-glow{position:absolute;inset:8% 6%;border-radius:50%;background:radial-gradient(closest-side,rgba(56,240,255,.3),transparent 72%);filter:blur(14px)}
.ac-pic img{position:relative;display:block;max-width:100%;max-height:360px;width:auto;height:auto;object-fit:contain;filter:drop-shadow(0 24px 22px rgba(0,0,0,.65));animation:acfloat 6s ease-in-out infinite}
@keyframes acfloat{50%{transform:translateY(-8px)}}
.ac-brand{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--cy);padding:5px 11px;border-radius:99px;background:rgba(56,240,255,.12);border:1px solid rgba(56,240,255,.3)}
.ac-info h3{font-size:clamp(30px,3.4vw,46px);margin:12px 0 4px}
.ac-mount{color:var(--muted);font-size:14px;margin-bottom:16px}
.ac-info ul{list-style:none;margin-bottom:16px}
.ac-info li{display:flex;justify-content:space-between;gap:14px;padding:9px 0;border-top:1px solid var(--line);font-size:14.5px}
.ac-info li span{color:var(--muted)}.ac-info li b{font-weight:600;text-align:right}
.ac-bot{display:flex;align-items:center;justify-content:space-between;gap:12px}
.ac-price{font-size:clamp(30px,3.4vw,44px);font-weight:800;letter-spacing:-.03em;white-space:nowrap;color:#ffb21e;text-shadow:0 0 26px rgba(255,170,30,.45)}
.ac-go{font-size:14px;font-weight:700;padding:11px 18px;border-radius:99px;background:linear-gradient(135deg,var(--cy),#7dffd0);color:#02161c;white-space:nowrap}
.ac-bar{position:absolute;left:0;bottom:0;height:3px;width:0;background:linear-gradient(90deg,var(--cy),var(--gr));box-shadow:0 0 12px var(--cy)}
.ac.on .ac-bar{animation:acbar var(--dur,4.2s) linear forwards}
.acc.paused .ac.on .ac-bar{animation:none;width:100%}
@keyframes acbar{from{width:0}to{width:100%}}
@media(max-width:820px){
 .acc{flex-direction:column;height:auto}
 .ac{flex:0 0 auto;height:74px;transition:height .6s cubic-bezier(.2,.8,.2,1),border-color .4s}
 .ac.on{height:610px}
 .ac-rail{flex-direction:row;padding:0 20px;align-items:center;justify-content:flex-start;gap:14px}
 .ac-v,.ac-p{writing-mode:horizontal-tb;transform:none}
 .ac-v{font-size:21px;flex:1}
 .ac-n{font-size:24px}
 .ac-p{font-size:24px;padding:0}
 .ac-body{grid-template-columns:1fr;grid-template-rows:190px auto;padding:18px 20px 22px;min-width:0;align-items:start;transform:translateY(16px)}
 .ac-pic{max-height:200px}.ac-pic img{max-height:190px}
 .ac-info h3{font-size:28px;margin-top:8px}
}
/* преимущества */
.feat{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.fc{border-radius:24px;padding:26px;background:rgba(255,255,255,.04);border:1px solid var(--line);backdrop-filter:blur(10px);position:relative;overflow:hidden;transition:.3s}
.fc:hover{border-color:rgba(56,240,255,.5);transform:translateY(-4px)}
.fc::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;background:linear-gradient(90deg,transparent,var(--cy),transparent)}
.fc i{width:48px;height:48px;border-radius:15px;display:grid;place-items:center;background:rgba(56,240,255,.12);border:1px solid rgba(56,240,255,.3);color:var(--cy);margin-bottom:18px}
.fc i svg{width:24px;height:24px;stroke:currentColor;fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.fc h3{font-size:20px;margin-bottom:6px}.fc p{color:var(--muted);font-size:15px}
/* заявка */
.lead-box{display:grid;gap:26px;align-items:center;padding:clamp(24px,4vw,46px);border-radius:30px;background:linear-gradient(130deg,rgba(56,240,255,.13),rgba(255,255,255,.03));border:1px solid rgba(56,240,255,.35);backdrop-filter:blur(14px)}
@media(min-width:900px){.lead-box{grid-template-columns:1fr 1.15fr}}
.lead-box h2{font-size:clamp(28px,4vw,42px)}.lead-box p{color:#b6c4d2}
.form{display:grid;gap:10px}
@media(min-width:620px){.form{grid-template-columns:1fr 1fr}.form .full{grid-column:1/-1}}
.form input{width:100%;padding:16px 20px;border-radius:99px;border:1px solid var(--line);background:rgba(0,0,0,.45);color:#fff;font:inherit;font-size:16px}
.form input:focus{outline:0;border-color:var(--cy);box-shadow:0 0 0 4px rgba(56,240,255,.15)}
.form .hp{position:absolute;left:-9999px;opacity:0}
.form-msg{min-height:1.3em;font-weight:600;font-size:14px}
.form-note{font-size:12px;color:var(--muted)}.form-note a{color:#c4d0dc}
footer{padding:36px 20px 24px;text-align:center;color:var(--muted);font-size:13px;border-top:1px solid var(--line);background:rgba(4,6,10,.7);backdrop-filter:blur(10px)}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:70;display:flex;gap:8px;padding:10px 12px;background:rgba(4,6,10,.9);backdrop-filter:blur(12px);border-top:1px solid var(--line)}
.bar .btn{flex:1;padding:14px 10px}
@media(min-width:820px){body{padding-bottom:0}.bar{display:none}}
.rv{opacity:0;transform:translateY(30px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}.rv.d1{transition-delay:.1s}.rv.d2{transition-delay:.2s}.rv.d3{transition-delay:.3s}
@media(prefers-reduced-motion:reduce){.gc,.btn-main,.btn-main::after,.scrollhint i,.eyebrow::before{animation:none}.rv{opacity:1;transform:none;transition:none}}
"""

SHADER_JS = r"""
(function(){
  var cv = document.getElementById('fx'); if (!cv) return;
  var gl = cv.getContext('webgl', {antialias:false, alpha:false, powerPreference:'low-power'}); if (!gl) return;
  var vs = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
  var fs = 'precision mediump float;uniform vec2 R;uniform float T;uniform vec2 M;uniform float S;uniform float S2;' +
  'float h(vec2 s){return fract(sin(dot(s,vec2(127.1,311.7)))*43758.5453);}' +
  'void main(){' +
  ' float k=min(R.y,R.x*.56); vec2 uv=(gl_FragCoord.xy-.5*R)/k; uv+= (M-.5)*vec2(.12,.09);' +
  ' float r=length(uv); vec2 dir=uv/max(r,1e-4);' +
  ' vec3 col=vec3(.012,.02,.035)+vec3(.02,.05,.09)*smoothstep(.9,.0,r);' +
  ' for(int i=0;i<6;i++){' +
  '  float fi=float(i); float z=fract(fi/6.-T*.07);' +
  '  float sc=mix(26.,2.2,z);' +
  '  vec2 q=uv*sc+vec2(fi*7.3,fi*3.1);' +
  '  vec2 c=floor(q); vec2 f=fract(q)-.5;' +
  '  float a=h(c+fi), b=h(c*1.7+fi*5.), k=h(c*2.3+fi*9.);' +
  '  if(a<S2) continue;' +
  '  vec2 d=f-(vec2(h(c+3.),h(c+7.))-.5)*.6;' +
  '  float al=dot(d,dir), pe=length(d-al*dir);' +
  '  float tail=al<0.?.16:1.4; float len=.5+S*.9;' +
  '  float dd=pe*pe*70.+al*al*tail*tail*mix(260.,40.,len*.5);' +
  '  float g=exp(-dd)*(.55+k*.9);' +
  '  float glow=exp(-dd*.18)*.07;' +
  '  float fade=smoothstep(0.,.18,z)*smoothstep(1.,.7,z);' +
  '  float tun=smoothstep(.03,.30,r);' +
  '  vec3 tint=mix(vec3(1.,.74,.38),vec3(.35,.92,1.),b);' +
  '  tint=mix(tint,vec3(.5,1.,.7),step(.93,k));' +
  '  col+=tint*(g+glow)*fade*tun*(1.2+1.6*(1.-z));' +
  ' }' +
  ' col+=vec3(.0,.05,.08)*exp(-r*3.)*(.5+.5*sin(T*.6));' +
  ' col=1.-exp(-col*1.25);' +
  ' gl_FragColor=vec4(col,1.);}';
  function sh(t,s){ var o = gl.createShader(t); gl.shaderSource(o,s); gl.compileShader(o); if (!gl.getShaderParameter(o, gl.COMPILE_STATUS)) { console.warn(gl.getShaderInfoLog(o)); return null; } return o; }
  var v = sh(gl.VERTEX_SHADER, vs), f = sh(gl.FRAGMENT_SHADER, fs); if (!v || !f) return;
  var pr = gl.createProgram(); gl.attachShader(pr,v); gl.attachShader(pr,f); gl.linkProgram(pr); if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) return; gl.useProgram(pr);
  var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1,1,-1,-1,1,1,1]), gl.STATIC_DRAW);
  var loc = gl.getAttribLocation(pr,'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc,2,gl.FLOAT,false,0,0);
  var uR = gl.getUniformLocation(pr,'R'), uT = gl.getUniformLocation(pr,'T'), uM = gl.getUniformLocation(pr,'M'), uS = gl.getUniformLocation(pr,'S'), uD = gl.getUniformLocation(pr,'S2');
  var scale = innerWidth < 700 ? .6 : .62, touch = matchMedia('(hover: none)').matches, moved = false, mx = .5, my = .5, tx = .5, ty = .5, boost = 0, last = scrollY, t0 = performance.now(), run = true;
  function size(){ cv.width = Math.max(2, Math.floor(innerWidth*scale)); cv.height = Math.max(2, Math.floor(innerHeight*scale)); gl.viewport(0,0,cv.width,cv.height); }
  size(); addEventListener('resize', size);
  addEventListener('pointermove', function(e){ moved = true; tx = e.clientX/innerWidth; ty = 1 - e.clientY/innerHeight; });
  document.addEventListener('visibilitychange', function(){ run = !document.hidden; if (run) requestAnimationFrame(frame); });
  function frame(now){
    if (!run) return; requestAnimationFrame(frame);
    var t = REDUCE ? 3 : (now - t0)/1000;
    if (touch && !moved && !REDUCE){ tx = .5 + Math.sin(t*.35)*.45; ty = .5 + Math.cos(t*.27)*.4; }
    mx += (tx-mx)*.05; my += (ty-my)*.05;
    var dv = Math.abs(scrollY - last); last = scrollY; boost = Math.min(1, boost*.94 + dv*.01);
    gl.uniform2f(uR, cv.width, cv.height); gl.uniform1f(uT, t + boost*0.0); gl.uniform2f(uM, mx, my); gl.uniform1f(uS, boost); gl.uniform1f(uD, touch ? .74 : .62);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
  }
  requestAnimationFrame(frame);
})();
(function(){
  var acc = document.getElementById('acc'); if (!acc) return;
  var items = [].slice.call(acc.querySelectorAll('.ac')), cur = 0, DUR = 4200, timer = null, hov = false;
  function set(i){ cur = i; items.forEach(function(el, k){ el.classList.toggle('on', k === i); if (k === i){ var b = el.querySelector('.ac-bar'); b.style.animation = 'none'; void el.offsetWidth; b.style.animation = ''; } }); }
  function schedule(){ clearTimeout(timer); if (hov || REDUCE) return; timer = setTimeout(function(){ if (visible(acc)) set((cur + 1) % items.length); schedule(); }, DUR); }
  acc.style.setProperty('--dur', (DUR/1000) + 's');
  items.forEach(function(el, k){
    el.addEventListener('pointerenter', function(e){ if (e.pointerType === 'mouse'){ hov = true; acc.classList.add('paused'); set(k); schedule(); } });
    el.addEventListener('focus', function(){ hov = true; acc.classList.add('paused'); set(k); });
    el.addEventListener('click', function(e){ if (!el.classList.contains('on')){ e.preventDefault(); hov = true; acc.classList.add('paused'); set(k); schedule(); } });
  });
  acc.addEventListener('pointerleave', function(e){ if (e.pointerType === 'mouse'){ hov = false; acc.classList.remove('paused'); set(cur); schedule(); } });
  schedule();
})();
(function(){
  // подсветка и наклон фото в карточках
  document.querySelectorAll('.gc').forEach(function(c){
    var img = c.querySelector('.gc-pic img'), inn = c.querySelector('.gc-in');
    c.addEventListener('pointermove', function(e){
      var r = c.getBoundingClientRect(), x = (e.clientX-r.left)/r.width, y = (e.clientY-r.top)/r.height;
      inn.style.setProperty('--mx', (x*100)+'%'); inn.style.setProperty('--my', (y*100)+'%');
      if (!REDUCE){ img.style.setProperty('--ry', ((x-.5)*22)+'deg'); img.style.setProperty('--rx', (-(y-.5)*16)+'deg'); }
    });
    c.addEventListener('pointerleave', function(){ img.style.setProperty('--ry','0deg'); img.style.setProperty('--rx','0deg'); });
  });
})();
"""


def icon(path):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{path}</svg>'


def render():
    cards = "".join(
        f'<a class="gc rv d{i % 3}" href="/{c["slug"]}/"><div class="gc-in"><span class="gc-tag">{e(c["tag"])}</span>'
        f'<div class="gc-pic"><img src="{c["img"]}" alt="{e(c["title"])}" loading="lazy" width="380" height="380" draggable="false"></div>'
        f'<h3>{e(c["title"])}</h3><p>{e(c["sub"])}</p>'
        f'<div class="gc-bot"><span class="gc-price">{e(c["price"])}</span><span class="gc-go">→</span></div></div></a>'
        for i, c in enumerate(CARDS))
    models = ""
    for k, m in enumerate(STOCK):
        spec = [("Мощность", power_text(m)), ("Вход", m["vin"] + " В"), ("Макс. ток", m["amp"] + " А"), ("Монтаж", m["mount"])]
        spec_html = "".join(f"<li><span>{e(a)}</span><b>{e(b)}</b></li>" for a, b in spec)
        brand = "Exegate" if m["brand"] == "exegate" else "Ресанта"
        models += (f'<a class="ac{" on" if k == 0 else ""}" href="/{PAGE_OF[m["id"]]}/" data-i="{k}" aria-label="{e(m["name"])}">'
                   f'<div class="ac-rail"><span class="ac-n">0{k + 1}</span><span class="ac-v">{e(m["short"])}</span><span class="ac-p">{money(m["price"])}</span></div>'
                   f'<div class="ac-body"><div class="ac-pic"><span class="ac-glow"></span><img src="{m["img"]}" alt="{e(m["name"])}" loading="lazy" draggable="false"></div>'
                   f'<div class="ac-info"><span class="ac-brand">{brand}</span><h3>{e(m["short"])}</h3><p class="ac-mount">{e(m["name"])}</p>'
                   f'<ul>{spec_html}</ul><div class="ac-bot"><span class="ac-price">{money(m["price"])}</span><span class="ac-go">Подробнее →</span></div></div>'
                   f'<i class="ac-bar"></i></div></a>')
    feats = [
        ("M13 2 4 14h7l-1 8 9-12h-7z", "Реальные характеристики", "Данные берём с сайтов производителей Exegate и Ресанта. Без выдуманных цифр."),
        ("M2 6h11v10H2zM13 9h4l3 3v4h-7M6.5 17.5a1.5 1.5 0 1 0 0 .01M16.5 17.5a1.5 1.5 0 1 0 0 .01", "Доставка по Крыму", "Отправляем транспортными компаниями по всему Крыму и на новые территории."),
        ("M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z", "Защита всего дома", "Релейные стабилизаторы с защитой от перенапряжения, перегрева и короткого замыкания."),
        ("M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z", "Подскажем по телефону", f"Позвоните или напишите в Telegram: подберём модель под вашу нагрузку. Работаем {B.HOURS}."),
    ]
    feat_html = ""
    for i, (path, t, d) in enumerate(feats):
        svg = icon('<path d="' + path + '"/>')
        feat_html += f'<div class="fc rv d{i % 4}"><i>{svg}</i><h3>{e(t)}</h3><p>{e(d)}</p></div>'
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#04060a">
<title>Стабилизаторы напряжения в Симферополе — Ресанта и Exegate, доставка по Крыму</title>
<meta name="description" content="Стабилизаторы напряжения Ресанта и Exegate для дома от 3 190 ₽. Доставка по Крыму и на новые территории. Звоните: {B.PHONE_TEXT}">
<link rel="canonical" href="{B.DOMAIN}/">
<meta property="og:title" content="Стабилизаторы напряжения в Симферополе — Ресанта и Exegate">
<meta property="og:description" content="Цены, фото и характеристики. Доставка по Крыму и на новые территории.">
<meta property="og:type" content="website">
<meta property="og:url" content="{B.DOMAIN}/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2304060a'/%3E%3Cpath d='M36 8 18 36h12l-4 20 20-30H34z' fill='%2338f0ff'/%3E%3C/svg%3E">
<style>{CSS}</style>
</head>
<body>
<canvas id="fx" aria-hidden="true"></canvas><div class="veil"></div>
<nav class="nav"><div class="nav-in">
 <div class="logo"><i>⚡</i> Стабилизаторы<span>&nbsp;· Симферополь</span></div>
 <a class="l" href="#catalog">Каталог</a><a class="l" href="#models">Цены</a><a class="l" href="#why">Почему мы</a><a class="l" href="#order">Заявка</a>
 <a class="btn btn-main" href="tel:{B.PHONE_HREF}" data-goal="call" style="padding:10px 18px;font-size:14px">{B.PHONE_TEXT}</a>
</div></nav>

<header class="hero"><div class="wrap">
 <div class="eyebrow">Симферополь · доставка по всему Крыму</div>
 <h1>Ровные <em>220&nbsp;В</em> в вашем доме</h1>
 <p class="lead">Стабилизаторы напряжения Ресанта и Exegate: от компактных для техники до мощных на весь дом. Цены от 3 190 ₽, доставка транспортной компанией.</p>
 <div class="cta">
  <a class="btn btn-main" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить {B.PHONE_TEXT}</a>
  <a class="btn btn-ghost tg" href="#" target="_blank" rel="noopener" data-goal="tg">Написать в Telegram</a>
 </div>
 <div class="hint">Работаем {B.HOURS} · установку не выполняем</div>
</div><div class="scrollhint">листайте<i></i></div></header>

<section class="s" id="catalog"><div class="wrap">
 <div class="eyebrow rv">Каталог</div><h2 class="rv">Выберите <em>стабилизатор</em></h2>
 <p class="sub rv">Пять подборок под разные задачи: от квартиры до большого дома и мастерской.</p>
 <div class="cards">{cards}</div>
</div></section>

<section class="s" id="models"><div class="wrap">
 <div class="eyebrow rv">Модели и цены</div><h2 class="rv">Шесть моделей — <em>одним взглядом</em></h2>
 <p class="sub rv">Наведите мышь на модель или коснитесь её: панель раскроется. Сами тоже листаются по кругу.</p>
 <div class="acc rv" id="acc">{models}</div>
</div></section>

<section class="s" id="why"><div class="wrap">
 <div class="eyebrow rv">Почему мы</div><h2 class="rv">Просто, понятно, <em>без сюрпризов</em></h2>
 <div class="feat" style="margin-top:34px">{feat_html}</div>
</div></section>

<section class="s" id="order"><div class="wrap">
 <div class="lead-box rv">
  <div><h2>Оставьте номер — <em>перезвоним</em></h2><p>Подберём модель, назовём цену и срок доставки. Работаем {B.HOURS}.</p></div>
  <form class="form" id="lead" novalidate>
   <input type="text" name="name" placeholder="Ваше имя" autocomplete="name" maxlength="60">
   <input type="tel" name="phone" placeholder="Телефон" autocomplete="tel" inputmode="tel" required maxlength="25">
   <input type="hidden" name="comment" value="Заявка с главной страницы">
   <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
   <button class="btn btn-main full" type="submit">Перезвоните мне</button>
   <div class="form-msg full" id="lead-msg" role="status"></div>
   <div class="form-note full">Нажимая кнопку, вы соглашаетесь на обработку персональных данных на условиях <a href="/privacy/">политики конфиденциальности</a>.</div>
  </form>
 </div>
</div></section>

<footer>Симферополь · доставка по Крыму и на новые территории · {B.HOURS} · установку не выполняем<br>{B.OPERATOR_SHORT}, ИНН {B.INN}, ОГРНИП {B.OGRNIP} · <a href="/privacy/">Политика конфиденциальности</a></footer>

<div class="bar">
 <a class="btn btn-main" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить</a>
 <a class="btn btn-ghost tg" href="#" target="_blank" rel="noopener" data-goal="tg">Telegram</a>
</div>

<script>
// Настройки: ссылка на Telegram и номер счётчика Яндекс.Метрики
var TG_URL = "https://t.me/B2B_opt_simf";
var YM_ID = "113489938";
{COMMON_JS}
{SHADER_JS}
</script>
</body>
</html>
"""


def main():
    out = ROOT / "site" / "index.html"
    from make_all import nbsp, MOBILE_CENTER
    fix = "<style>@media(max-width:420px){.hero>.wrap{width:100%;min-width:0}}</style>"
    out.write_text(nbsp(render().replace("</head>", fix + MOBILE_CENTER + "</head>", 1)), encoding="utf-8")
    print("OK", out)


if __name__ == "__main__":
    main()
