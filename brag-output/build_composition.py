from pathlib import Path
import shutil
import xml.etree.ElementTree as ET

base = Path(__file__).resolve().parent
website = base.parent
repo = website.parent
project = base / 'composition'
assets = project / 'assets'
for sub in ['fonts', 'screens', 'vendor']:
    (assets/sub).mkdir(parents=True, exist_ok=True)
source = repo/'App/prayerlock/app/src/main'
site_font = website/'assets/fonts/plus-jakarta-variable.ttf'
shutil.copy2(site_font if site_font.exists() else source/'res/font/plus_jakarta_sans.ttf', assets/'fonts/plus-jakarta-sans.ttf')
if (website/'assets/fonts/OFL.txt').exists():
    shutil.copy2(website/'assets/fonts/OFL.txt',assets/'fonts/OFL.txt')
if not (assets/'vendor/gsap.min.js').exists():
    raise FileNotFoundError('The shipped local GSAP runtime assets/vendor/gsap.min.js is required.')
root = ET.parse(source/'res/drawable/ic_lock_logo_vector.xml').getroot()
ns = '{http://schemas.android.com/apk/res/android}'
paths = ''.join(f'<path d="{p.attrib[ns+"pathData"]}" fill="{p.attrib[ns+"fillColor"]}" fill-rule="{p.attrib.get(ns+"fillType", "nonzero")}"/>' for p in root)
(assets/'logo.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108"><rect width="108" height="108" rx="25" fill="#1b2646"/>'+paths+'</svg>', encoding='utf-8')
screens = website/'assets/screenshots'
fallbacks = website/'assets/images'
for name, fallback in [('home-fajr','fajr'),('home-dhuhr','dhuhr'),('home-maghrib','maghrib'),('home-isha','isha'),('qibla','asr'),('adhkar','maghrib'),('prayer-shield','maghrib')]:
    candidate = screens/(name+'.png')
    shutil.copy2(candidate if candidate.exists() else fallbacks/(fallback+'.png'), assets/'screens'/(name+'.png'))

(project/'index.html').write_text('''<!doctype html>
<html lang="en" data-composition-variables='[{"id":"color-ground","type":"color","label":"Stage","default":"#FBFBFD"},{"id":"color-ink","type":"color","label":"Ink","default":"#1D1D1F"},{"id":"color-accent","type":"color","label":"Accent","default":"#FFDF85"},{"id":"font-display","type":"string","label":"Font","default":"Plus Jakarta Sans"}]'>
<head><meta charset="utf-8"><script src="assets/vendor/gsap.min.js"></script>
<style>*{box-sizing:border-box;margin:0}html,body{width:1920px;height:1080px;overflow:hidden;background:#FBFBFD}#root{position:absolute;inset:0}.clip{position:absolute;inset:0}</style></head>
<body><div id="root" data-composition-id="main" data-start="0" data-duration="18" data-width="1920" data-height="1080">
<div id="room" class="clip" data-composition-id="room" data-composition-src="compositions/room.html" data-start="0" data-duration="4.8" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>
<div id="attention" class="clip" data-composition-id="attention" data-composition-src="compositions/attention.html" data-start="4.8" data-duration="5.6" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>
<div id="closer" class="clip" data-composition-id="closer" data-composition-src="compositions/closer.html" data-start="10.4" data-duration="4.4" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>
<div id="identity" class="clip" data-composition-id="identity" data-composition-src="compositions/identity.html" data-start="14.8" data-duration="3.2" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>
</div><script>window.__timelines=window.__timelines||{};window.__timelines.main=gsap.timeline({paused:true});</script></body></html>''', encoding='utf-8')

common = '''@font-face{font-family:"Plus Jakarta Sans";src:url('assets/fonts/plus-jakarta-sans.ttf') format('truetype');font-weight:100 900}*{box-sizing:border-box;margin:0}#root{position:absolute;inset:0;font-family:"Plus Jakarta Sans";color:#1D1D1F;background:#FBFBFD;overflow:hidden}.stage{position:absolute;inset:0;background:#FBFBFD}.eyebrow{font-size:28px;font-weight:600;letter-spacing:.01em;color:#5A6370}.headline{font-size:84px;line-height:1.09;font-weight:600;letter-spacing:-4px}.support{font-size:32px;line-height:1.5;font-weight:400;color:#5A6370}.phone{position:absolute;border:7px solid #20232B;border-radius:49px;background:#1B2646;box-shadow:0 28px 64px #1B26462B;overflow:hidden}.phone img{display:block;width:100%;height:100%;object-fit:cover}.phone::after{content:"";position:absolute;width:74px;height:7px;top:10px;left:calc(50% - 37px);border-radius:6px;background:#20232B}.logo{width:70px;height:70px;border-radius:18px}.wordmark{display:flex;gap:20px;align-items:center;font-size:31px;font-weight:600;letter-spacing:-1px}.copy{position:absolute}.scene-wrap{position:absolute;inset:0}.label{position:absolute;font-size:32px;font-weight:600;color:#5A6370}'''

def scene(name, markup, css, timeline):
    (project/'compositions'/f'{name}.html').write_text(f'''<template><style>{common}{css}</style>
<div id="root" data-composition-id="{name}" data-width="1920" data-height="1080"><div class="stage"></div>{markup}</div>
<script>const tl=gsap.timeline({{paused:true}});{timeline}window.__timelines=window.__timelines||{{}};window.__timelines['{name}']=tl;</script></template>''', encoding='utf-8')

scene('room','''<div id="room-wrap" class="scene-wrap">
<div id="room-copy" class="copy" data-hold><div id="room-brand" class="wordmark"><img class="logo" src="assets/logo.svg" alt=""><span>PrayerLock</span></div><h1 id="room-title" class="headline">Make room<br>for prayer.</h1><p id="room-sub" class="support">A quieter rhythm. For Android.</p></div>
<div id="room-phone" class="phone"><img src="assets/screens/home-isha.png" alt="PrayerLock Home screen"></div></div>''',
'''#room-copy{left:220px;top:278px}#room-title{margin-top:51px;margin-bottom:30px}#room-phone{left:1200px;top:112px;width:388px;height:840px}''',
'''tl.fromTo('#room-brand',{opacity:1},{opacity:1,duration:.5,ease:'power2.out'},0);
tl.fromTo('#room-title',{opacity:0,y:22},{opacity:1,y:0,duration:.7,ease:'power4.out'},.12);
tl.fromTo('#room-sub',{opacity:0},{opacity:1,duration:.6,ease:'power2.out'},.5);
tl.fromTo('#room-phone',{opacity:1,x:85,rotation:4},{opacity:1,x:0,rotation:0,duration:1,ease:'power4.out'},0);
tl.to('#room-wrap',{opacity:0,duration:.28,ease:'power2.in'},4.5);''')

scene('attention','''<div id="attention-wrap" class="scene-wrap">
<div id="attention-phone" class="phone"><img src="assets/screens/home-maghrib.png" alt="PrayerLock prayer schedule"><div id="attention-lock"><img src="assets/screens/prayer-shield.png" alt="PrayerLock Maghrib prayer shield"></div></div>
<div id="attention-copy" class="copy" data-hold><p class="eyebrow">A MOMENT TO RETURN</p><h1 class="headline">Give prayer<br>your attention.</h1><p class="support">Scheduled distraction lockouts.</p></div>
</div>''',
'''#attention-phone{left:260px;top:112px;width:388px;height:840px}#attention-copy{left:850px;top:303px}#attention-copy h1{margin-top:27px;margin-bottom:32px}#attention-lock{position:absolute;inset:0;background:#23355B;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff}#attention-lock-icon{width:100px;height:100px;margin-bottom:38px}.lock-eyebrow{font-size:28px;letter-spacing:2px;color:#FFDF85;font-weight:600}.lock-title{font-size:68px;letter-spacing:-3px;margin-top:18px;font-weight:600}.lock-description{font-size:28px;margin-top:20px}.lock-button{padding:22px 38px;margin-top:54px;border-radius:28px;background:#FFDF85;color:#1B2646;font-size:28px;font-weight:600}''',
'''tl.fromTo('#attention-phone',{opacity:0,x:100},{opacity:1,x:0,duration:.75,ease:'power4.out'},0);
tl.fromTo('#attention-copy',{opacity:0},{opacity:1,duration:.6,ease:'power2.out'},.18);
tl.fromTo('#attention-lock',{opacity:0,y:80},{opacity:1,y:0,duration:.7,ease:'power4.out'},1.35);
tl.to('#attention-wrap',{opacity:0,duration:.28,ease:'power2.in'},5.32);''')

scene('closer','''<div id="closer-wrap" class="scene-wrap"><div id="closer-copy" class="copy"><p class="eyebrow">DIRECTION &amp; REMEMBRANCE</p><h1 class="headline">A little closer.<br>Every day.</h1></div>
<div id="closer-qibla"><p class="label">Qibla</p><div class="phone"><img src="assets/screens/qibla.png" alt="PrayerLock Qibla screen"></div></div>
<div id="closer-adhkar"><p class="label">Adhkar</p><div class="phone"><img src="assets/screens/adhkar.png" alt="PrayerLock Adhkar screen"></div></div>
</div>''',
'''#closer-copy{left:180px;top:365px}#closer-copy h1{margin-top:28px;font-size:78px}#closer-qibla,#closer-adhkar{position:absolute;top:128px;width:322px;height:790px}#closer-qibla{left:1050px}#closer-adhkar{left:1445px}#closer-wrap .phone{top:65px;width:322px;height:697px;border-radius:43px}#closer-wrap .label{left:3px;top:0}''',
'''tl.fromTo('#closer-copy',{opacity:0},{opacity:1,duration:.55,ease:'power2.out'},0);
tl.fromTo('#closer-qibla',{opacity:0,y:55},{opacity:1,y:0,duration:.7,ease:'power4.out'},.08);
tl.fromTo('#closer-adhkar',{opacity:0,y:55},{opacity:1,y:0,duration:.7,ease:'power4.out'},.33);
// Adapted from the installed fade-through registry recipe; the stage stays white.
tl.to('#closer-wrap',{opacity:0,duration:.32,ease:'power2.inOut'},4.08);''')

scene('identity','''<div id="identity-wrap" class="scene-wrap" data-hold><img id="identity-logo" src="assets/logo.svg" alt="PrayerLock app icon"><h1 id="identity-title">PrayerLock</h1><p id="identity-tagline">Make room for prayer.</p><p id="identity-platform">For Android</p></div>''',
'''#identity-wrap{text-align:center}#identity-logo{position:absolute;left:879px;top:208px;width:162px;height:162px;border-radius:38px}#identity-title{position:absolute;top:420px;width:100%;font-size:82px;letter-spacing:-4px;font-weight:600}#identity-tagline{position:absolute;top:550px;width:100%;font-size:42px;letter-spacing:-1px}#identity-platform{position:absolute;top:656px;width:100%;font-size:28px;color:#5A6370}''',
'''tl.fromTo('#identity-logo',{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:'power4.out'},0);
tl.fromTo('#identity-title',{opacity:0},{opacity:1,duration:.55,ease:'power2.out'},.12);
tl.fromTo('#identity-tagline',{opacity:0},{opacity:1,duration:.5,ease:'power2.out'},.35);
tl.fromTo('#identity-platform',{opacity:0},{opacity:1,duration:.5,ease:'power2.out'},.5);''')
print('Composition built with current available screen sources.')
