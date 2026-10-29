from pathlib import Path
from PIL import Image
import shutil

base = Path(__file__).parent
website = base.parent
names = ['fajr','dhuhr','asr','maghrib','isha']
screens = []
provenance = []
size = (390,844)
for name in names:
    real = website/'assets/screenshots'/f'home-{name}.png'
    source = real if real.exists() else website/'assets/images'/f'{name}.png'
    provenance.append(str(source.relative_to(website)))
    img = Image.open(source).convert('RGBA').resize(size, Image.Resampling.LANCZOS)
    background = Image.new('RGBA', size, '#FBFBFD')
    background.alpha_composite(img)
    screens.append(background.convert('RGB'))

# A shared palette prevents shimmer across the five sky states.
palette_sheet = Image.new('RGB', (size[0]*5,size[1]))
for i,img in enumerate(screens):
    palette_sheet.paste(img,(i*size[0],0))
palette = palette_sheet.quantize(colors=192, method=Image.Quantize.MEDIANCUT)
frames = []
durations = []
for i,img in enumerate(screens):
    frames.append(img.quantize(palette=palette,dither=Image.Dither.NONE))
    durations.append(1000)
    following = screens[(i+1)%len(screens)]
    for t in [.2,.4,.6,.8]:
        frames.append(Image.blend(img,following,t).quantize(palette=palette,dither=Image.Dither.NONE))
        durations.append(80)

output = base/'prayerlock-sky.gif'
frames[0].save(output, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True, disposal=1)
(website/'assets/media').mkdir(parents=True,exist_ok=True)
shutil.copy2(output,website/'assets/media/prayerlock-sky.gif')
print(f'Wrote {output.stat().st_size:,} bytes, {len(frames)} frames, {sum(durations)/1000:.2f}s, sources: {provenance}')
