from pathlib import Path
import json
import shutil
import subprocess

base = Path(__file__).parent
raw = base/'brag.raw.mp4'
poster = base/'brag.jpg'
final = base/'brag.mp4'
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','2.4','-i',str(raw),'-frames:v','1','-q:v','2',str(poster)],check=True)
# Replace exactly frame zero so social thumbnail grabbers see the chosen hero.
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(raw),'-i',str(poster),'-filter_complex',"[0:v][1:v]overlay=0:0:enable='eq(n,0)'[v]",'-map','[v]','-map','0:a?','-c:v','libx264','-crf','18','-preset','slow','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',str(final)],check=True)
media = base.parent/'assets/media'
media.mkdir(parents=True,exist_ok=True)
shutil.copy2(final,media/'prayerlock-film.mp4')
shutil.copy2(poster,media/'prayerlock-film-poster.jpg')
probe = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,width,height,nb_frames,r_frame_rate,pix_fmt','-of','json',str(final)],capture_output=True,text=True,check=True)
(base/'media-verification.json').write_text(probe.stdout,encoding='utf-8')
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(final),'-frames:v','1',str(base/'verified-frame-zero.png')],check=True)
print(probe.stdout)
print('Website MP4 and poster copied.')
