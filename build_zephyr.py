# -*- coding: utf-8 -*-
"""Страница «Zephyr-стиль» для запроса «стабилизатор Exegate для дома»: шалфейная дымка, Playfair + DM Sans,
парящий дом с тёплыми окнами, ряд из четырёх шагов. Запуск: python build_zephyr.py -> preview/exegate-warm/index.html"""
import pathlib

import build as B
from catalog import MODEL_IMG
from fx import pf, anatomy, PF_CSS
from widgets import series_tabs

TS_BODY, TS_CSS, TS_JS = series_tabs()
from build_wow import PAGES, COMMON_JS, e
from build_beacon import ico

P = PAGES["exegate"]

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Manrope:wght@500;600;700;800&display=swap');
:root{--pf-glow:rgba(255,217,160,.65);--pf-rim:rgba(40,50,38,.35);--pf-accent:#e8993f;--pf-floor:rgba(40,50,38,.4);--pf-hint-bg:rgba(36,44,32,.12);--pf-hint-fg:#242c20;--pf-hint-bd:rgba(36,44,32,.3);--sage:#7d8a78;--sage-d:#4f5b4b;--sage-dd:#3a4437;--cream:#f3f0e6;--card:#fbfaf4;--ink:#242c20;--muted:#6b7566;--line:rgba(36,44,32,.14);--amber:#e8993f;--glow:#ffd9a0;--head:'Manrope','DM Sans','Segoe UI',system-ui,sans-serif;--font:'DM Sans','Segoe UI',system-ui,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--cream);color:var(--ink);font-family:var(--font);font-weight:400;line-height:1.6;font-size:16px;overflow-x:hidden;padding-bottom:70px}
a{color:inherit}
.wrap{max-width:1160px;margin:0 auto;padding:0 22px}
h1,h2,h3{font-family:var(--head);font-weight:700;letter-spacing:-.035em;line-height:1.06}
h2{font-size:clamp(30px,4.6vw,56px);margin-bottom:18px}
em{font-style:normal;color:var(--amber)}
.eyebrow{font-size:12px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;margin-bottom:18px;display:flex;align-items:center;gap:10px}
.eyebrow::before{content:"";width:28px;height:1px;background:currentColor;opacity:.6}
/* шапка */
.nav{position:fixed;left:0;right:0;top:0;z-index:60;display:flex;justify-content:center;padding:16px}
.nav-in{display:flex;align-items:center;gap:26px;width:100%;max-width:1160px;padding:10px 12px 10px 20px;border-radius:99px;background:rgba(243,240,230,.14);border:1px solid rgba(255,255,255,.28);backdrop-filter:blur(14px);color:#f4f1e8}
.logo{display:flex;align-items:center;gap:10px;font-weight:500;margin-right:auto;white-space:nowrap}
.logo i{width:30px;height:30px;border-radius:50%;border:1px solid rgba(255,255,255,.5);display:grid;place-items:center;font-style:normal;font-size:14px}
.nav a.l{font-size:13px;text-decoration:none;opacity:.85;position:relative}
.nav a.l+a.l::before{content:"·";position:absolute;left:-15px;opacity:.6}
.nav a.l:hover{opacity:1}
.tel{font-weight:500;text-decoration:none;font-size:14px;padding:9px 18px;border-radius:99px;background:#f4f1e8;color:var(--ink);white-space:nowrap}
@media(max-width:820px){.nav a.l{display:none}}
@media(max-width:520px){.hs{display:none}.nav-in{padding-left:14px}.tel{padding:8px 14px;font-size:13px}}
/* hero */
.hero{position:relative;min-height:100svh;overflow:hidden;isolation:isolate;color:#f4f1e8;background:radial-gradient(900px circle at 72% 45%,#a9b3a3,transparent 60%),radial-gradient(700px circle at 8% 90%,#667260,transparent 60%),linear-gradient(135deg,#869281,#6a7666 60%,#5c6859)}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;opacity:.1;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.haze{position:absolute;border-radius:50%;filter:blur(70px);z-index:-1;animation:drift 18s ease-in-out infinite;will-change:transform}
.h1b{width:46vw;height:46vw;max-width:640px;max-height:640px;right:6%;top:12%;background:rgba(214,222,206,.35)}
.h2b{width:38vw;height:38vw;max-width:520px;max-height:520px;left:-6%;bottom:8%;background:rgba(255,217,160,.18);animation-delay:-8s}
@keyframes drift{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(24px,-20px) scale(1.1)}}
.hero-in{max-width:1160px;margin:0 auto;padding:104px 22px 168px;display:grid;gap:30px;align-items:center}
@media(min-width:960px){.hero-in{grid-template-columns:1fr 1fr;padding-top:110px}}
.proof{display:inline-flex;align-items:center;gap:12px;font-size:13px;margin-bottom:20px;opacity:.92}
.proof .av{display:flex}
.proof .av span{width:30px;height:30px;border-radius:50%;border:1.5px solid rgba(255,255,255,.7);background:rgba(244,241,232,.2);backdrop-filter:blur(4px);display:grid;place-items:center;margin-left:-8px;font-size:11px;font-weight:600}
.proof .av span:first-child{margin-left:0}
.hero h1{font-size:clamp(36px,5.3vw,70px);margin-bottom:18px;text-shadow:0 2px 30px rgba(40,50,38,.25)}
.hero h1 em{display:block;color:#ffd9a0}
.lead{font-size:clamp(16px,1.7vw,19px);opacity:.9;max-width:30em;margin-bottom:24px;font-weight:300}
.ghost{display:inline-flex;align-items:center;gap:14px;padding:6px 26px 6px 6px;border-radius:99px;border:1px solid rgba(255,255,255,.55);background:rgba(244,241,232,.1);backdrop-filter:blur(6px);text-decoration:none;font-size:13px;letter-spacing:.08em;text-transform:uppercase;font-weight:500;color:#f4f1e8;transition:background .3s,transform .3s}
.ghost:hover{background:rgba(244,241,232,.22);transform:translateY(-2px)}
.ghost b{width:42px;height:42px;border-radius:50%;background:var(--sage-dd);display:grid;place-items:center;color:#f4f1e8}
.ghost b svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.cta{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.cta .tgb{padding:15px 24px;border-radius:99px;border:1px solid rgba(255,255,255,.4);text-decoration:none;font-size:14px;color:#f4f1e8}
.note{margin-top:16px;font-size:13px;opacity:.75}
.art{position:relative;padding:0 0 9%;margin-right:-4%}
.art-house{position:relative;transform:translate3d(var(--hx,0px),var(--hy,0px),0);transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.art-glow{position:absolute;left:14%;right:8%;top:30%;bottom:8%;border-radius:50%;background:radial-gradient(closest-side,rgba(255,200,120,.55),transparent 72%);filter:blur(28px);animation:glowwin 6s ease-in-out infinite}
.house-img{position:relative;width:100%;height:auto;display:block;filter:drop-shadow(0 40px 30px rgba(30,40,28,.45));animation:float 8s ease-in-out infinite}
.art-unit{position:absolute;right:-3%;bottom:-6%;width:44%;z-index:3;transform:translate3d(var(--ux,0px),var(--uy,0px),0);transition:transform .35s cubic-bezier(.2,.7,.2,1)}
@media(max-width:959px){.art{margin-right:0;padding-bottom:16%}.art-unit{width:46%;right:-2%;bottom:-4%}}
.series .pf{margin:-14px -14px 6px}
.series .num{z-index:2}
.anat{color:var(--ink)}
.anat-txt h3{font-family:var(--head)}
.art svg{width:100%;max-width:560px;height:auto;filter:drop-shadow(0 40px 40px rgba(30,40,28,.35));animation:float 7s ease-in-out infinite;will-change:transform}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
.win{animation:breath 5s ease-in-out infinite}
@keyframes breath{0%,100%{opacity:.88}50%{opacity:1}}
/* ряд шагов */
.rail{position:absolute;left:0;right:0;bottom:34px;z-index:2}
.rail-in{max-width:1160px;margin:0 auto;padding:0 22px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
@media(min-width:960px){.rail-in{grid-template-columns:repeat(4,minmax(0,150px))}}
.step{display:flex;flex-direction:column;gap:8px}
.sq{height:78px;border-radius:14px;border:1px solid rgba(255,255,255,.4);background:rgba(244,241,232,.1);backdrop-filter:blur(8px);padding:12px 14px;display:flex;flex-direction:column;justify-content:space-between;font-size:12px;transition:background .3s,transform .3s}
.step:hover .sq{background:rgba(244,241,232,.24);transform:translateY(-4px)}
.sq svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;opacity:.9}
.step i{font-style:normal;font-size:11px;opacity:.75;display:flex;align-items:center;gap:8px}
.step i::before{content:"";width:18px;height:1px;background:currentColor;opacity:.6}
@media(max-width:620px){.sq{height:70px;font-size:11px;padding:10px}}
.scroll{position:absolute;right:24px;bottom:40px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;opacity:.7;writing-mode:vertical-rl;display:none}
@media(min-width:960px){.scroll{display:block}}
/* секции */
section.s{padding:110px 0}
.sub{color:var(--muted);max-width:38em;margin-bottom:46px;font-size:17px}
.dark{background:var(--sage-d);color:#f4f1e8}
.dark .sub{color:rgba(244,241,232,.75)}
.g2{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.series{background:var(--card);border:1px solid var(--line);border-radius:30px;padding:36px;position:relative;overflow:hidden;transition:transform .5s cubic-bezier(.2,.7,.2,1),box-shadow .5s}
.series:hover{transform:translateY(-6px);box-shadow:0 30px 60px -30px rgba(58,68,55,.4)}
.series .tag{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--sage-d);font-weight:500}
.series h3{font-size:36px;margin:12px 0 16px}
.series ul{list-style:none;margin-bottom:6px}
.series li{padding:11px 0;border-top:1px solid var(--line);display:flex;gap:12px;color:#3d4739}
.series li::before{content:"";flex:0 0 7px;height:7px;margin-top:9px;border-radius:50%;background:var(--amber)}
.pic{background:#fff;border-radius:22px;display:grid;place-items:center;overflow:hidden;padding:10px;margin:-10px -10px 20px;aspect-ratio:1/1;border:1px solid var(--line)}
.pic img{width:100%;height:auto;display:block}
.series .num{position:absolute;right:26px;top:6px;font-family:var(--head);font-weight:800;font-size:110px;line-height:1;color:rgba(79,91,75,.09)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px;text-align:left}
.stat{border-top:1px solid rgba(244,241,232,.3);padding-top:22px}
.stat b{display:block;white-space:nowrap;margin-bottom:12px;font-family:var(--head);font-weight:400;font-size:clamp(44px,6vw,80px);line-height:1;letter-spacing:-.03em}
.stat b em{color:var(--glow)}
.stat span{display:block;opacity:.8;font-size:15px;line-height:1.5}
.how{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.how div{padding:30px 26px;border-radius:26px;background:var(--card);border:1px solid var(--line)}
.how b{font-family:var(--head);font-weight:800;font-size:58px;line-height:1;color:var(--amber);display:block;margin-bottom:14px}
.how h3{font-size:24px;margin-bottom:8px}
.how p{color:var(--muted);font-size:15px}
table{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:24px;overflow:hidden}
th,td{text-align:left;padding:18px 26px;border-bottom:1px solid var(--line);vertical-align:top}
th{width:36%;font-weight:500;color:var(--muted);font-size:15px}
tr:last-child th,tr:last-child td{border-bottom:0}
.deliv{display:grid;gap:30px;align-items:center;padding:clamp(30px,5vw,56px);border-radius:32px;background:var(--sage-d);color:#f4f1e8}
@media(min-width:900px){.deliv{grid-template-columns:1.2fr .8fr}}
.deliv p{opacity:.85;max-width:34em}
.deliv p+p{margin-top:10px}
.deliv .big{font-family:var(--head);font-weight:800;font-size:clamp(40px,5.2vw,68px);line-height:1;color:var(--glow)}
details{border-bottom:1px solid var(--line);padding:22px 2px}
summary{cursor:pointer;font-family:var(--head);font-weight:600;font-size:20px;list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-family:var(--font);font-size:26px;line-height:1;color:var(--amber)}
details[open] summary::after{content:"–"}
details p{color:var(--muted);margin-top:12px;max-width:46em}
/* заявка */
.lead-sec{background:radial-gradient(800px circle at 80% 0,#9aa594,transparent 60%),linear-gradient(135deg,#7d8a78,#5c6859);color:#f4f1e8;padding:110px 0 80px}
.lead-bar{display:grid;gap:26px;align-items:center}
@media(min-width:900px){.lead-bar{grid-template-columns:1fr 1.2fr}}
.lead-bar h2{margin-bottom:10px}
.lead-bar p{opacity:.85}
.form{display:grid;gap:10px}
@media(min-width:620px){.form{grid-template-columns:1fr 1fr}.form .full{grid-column:1/-1}}
.form input{width:100%;padding:16px 20px;border-radius:99px;border:1px solid rgba(255,255,255,.45);background:rgba(244,241,232,.14);color:#fff;font:inherit;font-size:16px;backdrop-filter:blur(6px)}
.form input::placeholder{color:rgba(244,241,232,.7)}
.form input:focus{outline:0;border-color:#fff;background:rgba(244,241,232,.24)}
.form .hp{position:absolute;left:-9999px;opacity:0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:16px 30px;border-radius:99px;font-weight:500;font-size:15px;border:0;cursor:pointer;font-family:inherit;text-decoration:none;transition:transform .3s}
.btn:hover{transform:translateY(-2px)}
.btn-c{background:#f4f1e8;color:var(--ink)}
.form-msg{min-height:1.3em;font-size:14px}
.form-note{font-size:12px;opacity:.75;grid-column:1/-1}
footer{background:var(--sage-dd);color:rgba(244,241,232,.75);padding:34px 20px 24px;text-align:center;font-size:13px}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:70;display:flex;gap:8px;padding:10px 12px;background:rgba(58,68,55,.94);backdrop-filter:blur(10px)}
.bar .btn{flex:1;padding:14px 10px}
.bar .btn-o{background:transparent;border:1px solid rgba(255,255,255,.4);color:#f4f1e8}
@media(min-width:820px){body{padding-bottom:0}.bar{display:none}}
.rv{opacity:0;transform:translateY(28px);transition:opacity 1.1s cubic-bezier(.2,.7,.2,1),transform 1.1s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}.rv.d1{transition-delay:.12s}.rv.d2{transition-delay:.24s}.rv.d3{transition-delay:.36s}
@media(prefers-reduced-motion:reduce){.haze,.art svg,.win{animation:none}.rv{opacity:1;transform:none;transition:none}}
"""

HOUSE = """<svg viewBox="0 0 560 440" role="img" aria-label="Парящий дом с тёплым светом в окнах">
<defs>
 <linearGradient id="body" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#eceedf"/><stop offset="1" stop-color="#c3c9b4"/></linearGradient>
 <linearGradient id="body2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e2e5d2"/><stop offset="1" stop-color="#b3baa1"/></linearGradient>
 <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe3b3"/><stop offset="1" stop-color="#f0a24c"/></linearGradient>
 <radialGradient id="lamp" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e8e2c8"/></radialGradient>
 <radialGradient id="spill" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ffc878" stop-opacity=".55"/><stop offset="1" stop-color="#ffc878" stop-opacity="0"/></radialGradient>
</defs>
<ellipse cx="280" cy="408" rx="190" ry="20" fill="rgba(30,40,28,.28)"/>
<ellipse cx="280" cy="372" rx="170" ry="34" fill="url(#spill)"/>
<rect x="116" y="326" width="320" height="16" rx="8" fill="#9aa388"/>
<rect x="176" y="331" width="34" height="6" rx="3" fill="#ffb55a" class="win"/><rect x="224" y="331" width="34" height="6" rx="3" fill="#ffb55a" class="win"/>
<rect x="104" y="214" width="316" height="116" rx="38" fill="url(#body)"/>
<rect x="132" y="236" width="262" height="74" rx="16" fill="url(#glass)" class="win"/>
<g stroke="#8d7a55" stroke-opacity=".5" stroke-width="2"><path d="M198 236v74M262 236v74M326 236v74"/></g>
<rect x="150" y="268" width="26" height="42" rx="4" fill="#fff" opacity=".35"/><rect x="278" y="276" width="34" height="34" rx="4" fill="#fff" opacity=".28"/><rect x="342" y="262" width="22" height="48" rx="4" fill="#fff" opacity=".3"/>
<rect x="408" y="222" width="40" height="108" rx="16" fill="#9ca58a"/>
<g fill="#ffb55a" class="win"><rect x="418" y="238" width="20" height="8" rx="2"/><rect x="418" y="252" width="20" height="8" rx="2"/><rect x="418" y="266" width="20" height="8" rx="2"/></g>
<rect x="92" y="204" width="282" height="14" rx="7" fill="#a9b196"/>
<circle cx="112" cy="196" r="16" fill="url(#lamp)"/><circle cx="112" cy="196" r="30" fill="url(#spill)"/>
<rect x="150" y="128" width="278" height="88" rx="34" fill="url(#body2)"/>
<rect x="174" y="148" width="230" height="52" rx="14" fill="url(#glass)" class="win"/>
<g stroke="#8d7a55" stroke-opacity=".5" stroke-width="2"><path d="M232 148v52M290 148v52M348 148v52"/></g>
<rect x="138" y="116" width="302" height="16" rx="8" fill="#d6dac6"/>
<path d="M352 116V76" stroke="#6f7a68" stroke-width="3" stroke-linecap="round"/><circle cx="352" cy="72" r="4" fill="#6f7a68"/>
<circle cx="440" cy="204" r="12" fill="url(#lamp)"/>
</svg>"""

RAIL = [("phone", "Звонок", "01"), ("gauge", "Подбор", "02"), ("shield", "Заказ", "03"), ("truck", "Доставка", "04")]


def render():
    specs = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in P["specs"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in P["faq"])
    series = ""
    for i, (name, tag, items) in enumerate(P["models"]):
        lis = "".join(f"<li>{e(x)}</li>" for x in items)
        img = MODEL_IMG.get(name)
        pic = pf(img, name) if img else ""
        series += f'<div class="series rv d{i % 3}"><span class="num">0{i + 1}</span>{pic}<span class="tag">{e(tag)}</span><h3>{e(name)}</h3><ul>{lis}</ul></div>'
    rail = "".join(f'<div class="step"><div class="sq">{ico(n) if n != "phone" else ico("bolt")}<span>{e(t)}</span></div><i>{num}</i></div>' for n, t, num in RAIL)
    how = [("Позвоните или напишите", "Назовите, что хотите защитить, — подберём модель."), ("Подберём модель", "AST-500, AST-2000, AVS-2000 или AST-15000 — под вашу нагрузку и место установки."),
           ("Согласуем заказ", "Уточним цену и наличие, договоримся о способе и сроках доставки."), ("Отправим по Крыму", "Транспортной компанией — по всему Крыму и на новые территории.")]
    how_html = "".join(f'<div class="rv d{i % 4}"><b>0{i + 1}</b><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(how))
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#6a7666">
<title>Стабилизатор Exegate для дома — Симферополь, доставка по Крыму</title>
<meta name="description" content="{e(P['desc'])}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%236a7666'/%3E%3Cpath d='M36 8 18 36h12l-4 20 20-30H34z' fill='%23ffd9a0'/%3E%3C/svg%3E">
<style>{CSS}
{PF_CSS}
{TS_CSS}</style>
</head>
<body>
<nav class="nav"><div class="nav-in">
 <div class="logo"><i>⚡</i> Стабилизаторы<span class="hs"> · Симферополь</span></div>
 <a class="l" href="#top">Главная</a><a class="l" href="#series">Модели</a><a class="l" href="#how">Как заказать</a><a class="l" href="#specs">Характеристики</a><a class="l" href="#faq">Вопросы</a>
 <a class="tel" href="tel:{B.PHONE_HREF}" data-goal="call">{B.PHONE_TEXT}</a>
</div></nav>

<header class="hero" id="top">
 <div class="haze h1b"></div><div class="haze h2b"></div>
 <div class="hero-in">
  <div>
   <div class="proof"><span class="av"><span>E</span><span>M</span><span>T</span></span>Модели AST и AVS · {B.HOURS}</div>
   <h1>Стабилизатор Exegate <em>для дома</em></h1>
   <p class="lead">Свет в доме не мигает, а техника спокойна: релейное переключение менее 7 мс, КПД 98%. Модели от 3 190 ₽ до 31 990 ₽, доставка по Крыму.</p>
   <div class="cta">
    <a class="ghost" href="tel:{B.PHONE_HREF}" data-goal="call"><b>{ico("bolt")}</b>Позвонить {B.PHONE_TEXT}</a>
    <a class="tgb tg" href="#" target="_blank" rel="noopener" data-goal="tg">Написать в Telegram</a>
   </div>
   <div class="note">Цену и наличие назовём по телефону · установку не выполняем</div>
  </div>
  <div class="art"><div class="art-house"><span class="art-glow"></span><img class="house-img" src="/img/house.webp" alt="Современный дом с тёплым светом в окнах" width="1500" height="900" fetchpriority="high" draggable="false"></div><div class="art-unit">{pf("/img/ex-ast-15000.webp", "Стабилизатор Exegate Expert Turbo AST-15000")}</div></div>
 </div>
 <div class="rail"><div class="rail-in">{rail}</div></div>
 <div class="scroll">листайте</div>
</header>

{TS_BODY}

<section class="s dark"><div class="wrap">
 <div class="eyebrow rv">В цифрах</div>
 <h2 class="rv">Что получает ваш <em style="color:var(--glow)">дом</em></h2>
 <div class="stats" style="margin-top:40px">
  <div class="stat rv"><b>80–265</b><span>В — вход (по моделям): стабилизатор принимает «плавающую» сеть</span></div>
  <div class="stat rv d1"><b data-count="98">98</b><span>% КПД — минимум потерь и нагрева</span></div>
  <div class="stat rv d2"><b>&lt;7</b><span>мс — время переключения релейной схемы</span></div>
  <div class="stat rv d3"><b>±<span data-count="8" style="font-size:inherit;opacity:1">8</span><em>%</em></b><span>точность выходных 220 В</span></div>
 </div>
</div></section>

<section class="s" id="how"><div class="wrap">
 <div class="eyebrow rv">Как заказать</div>
 <h2 class="rv">Четыре шага — и свет <em>ровный</em></h2>
 <p class="sub rv">Без лишних звонков: мы подскажем модель и организуем доставку.</p>
 <div class="how">{how_html}</div>
</div></section>

<section class="s" id="specs" style="padding-top:20px"><div class="wrap">
 <div class="eyebrow rv">Характеристики</div>
 <h2 class="rv">Общие данные <em>серий</em></h2>
 <table class="rv">{specs}</table>
</div></section>

<section class="s" style="padding-top:20px"><div class="wrap">
 <div class="deliv rv">
  <div><div class="eyebrow" style="color:var(--glow)">Доставка</div><h2>По всему Крыму и на новые территории</h2>
  <p>Отправляем заказы транспортными компаниями — логистика налажена.</p>
  <p>Установку мы не выполняем: подключение к щитку лучше доверить электрику, а мы подскажем, что для этого нужно.</p></div>
  <div class="big">Весь Крым<br>и новые территории</div>
 </div>
</div></section>

<section class="s" id="faq" style="padding-top:20px"><div class="wrap" style="max-width:860px">
 <div class="eyebrow rv">Вопросы</div><h2 class="rv">Частые <em>вопросы</em></h2>{faq}
</div></section>

<section class="lead-sec" id="order"><div class="wrap"><div class="lead-bar">
 <div class="rv"><div class="eyebrow">Заявка</div><h2>Оставьте номер — <em>перезвоним</em></h2><p>Ответим по цене и наличию. Работаем {B.HOURS}.</p></div>
 <form class="form rv d1" id="lead" novalidate>
  <input type="text" name="name" placeholder="Ваше имя" autocomplete="name" maxlength="60">
  <input type="tel" name="phone" placeholder="Телефон" autocomplete="tel" inputmode="tel" required maxlength="25">
  <input type="hidden" name="comment" value="Стабилизатор Exegate для дома">
  <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button class="btn btn-c full" type="submit">Перезвоните мне</button>
  <div class="form-msg full" id="lead-msg" role="status"></div>
  <div class="form-note">Нажимая кнопку, вы соглашаетесь на обработку персональных данных на условиях <a href="/privacy/">политики конфиденциальности</a>.</div>
 </form>
</div></div></section>

<footer>Симферополь · доставка по Крыму и на новые территории · {B.HOURS} · установку не выполняем<br>{B.OPERATOR_SHORT}, ИНН {B.INN}, ОГРНИП {B.OGRNIP} · <a href="/privacy/">Политика конфиденциальности</a></footer>

<div class="bar">
 <a class="btn btn-c" href="tel:{B.PHONE_HREF}" data-goal="call">Позвонить</a>
 <a class="btn btn-o tg" href="#" target="_blank" rel="noopener" data-goal="tg">Telegram</a>
</div>

<script>
// Настройки: ссылка на Telegram и номер счётчика Яндекс.Метрики
var TG_URL = "https://t.me/B2B_opt_simf";
var YM_ID = "113489938";
{COMMON_JS}
{TS_JS}
(function(){{
  // лёгкое смещение дымки и дома за курсором
  var art = document.querySelector('.art'), hz = document.querySelectorAll('.haze'), hero = document.querySelector('.hero');
  if (!REDUCE) hero.addEventListener('pointermove', function(e){{
    var x = (e.clientX/innerWidth-.5), y = (e.clientY/innerHeight-.5);
    art.style.setProperty('--hx', (x*-22)+'px'); art.style.setProperty('--hy', (y*-14)+'px'); art.style.setProperty('--ux', (x*26)+'px'); art.style.setProperty('--uy', (y*16)+'px');
    hz.forEach(function(h,i){{ h.style.marginLeft = (x*(i?30:-40))+'px'; h.style.marginTop = (y*(i?20:-30))+'px'; }});
  }});
}})();
</script>
</body>
</html>
"""


def main():
    d = pathlib.Path(__file__).parent / "preview" / "exegate-warm"
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(render(), encoding="utf-8")
    print("OK", d / "index.html")


if __name__ == "__main__":
    main()
