"""Turns a rendered carousel folder into a 9:16 Reel with a music track baked in.
Run: python3 reel.py <folder_dir> <music_file> [seconds_per_slide]
Writes <folder_dir>/reel.mp4 and <folder_dir>/reel_cover.jpg (1080×1920).
Slides (1080×1350) sit centred on a 1080×1920 canvas filled with the slide's own ground colour,
with a short crossfade between slides. Audio fades out over the last 1.5 s. Instagram-safe:
H.264 high, yuv420p, 30 fps, AAC 48 kHz stereo, faststart.
"""
import glob, os, subprocess, sys, tempfile
from PIL import Image

def pad(src, dst):
    im = Image.open(src).convert("RGB")
    ground = im.getpixel((6, im.height // 2))
    can = Image.new("RGB", (1080, 1920), ground)
    can.paste(im, (0, (1920 - im.height) // 2))
    can.save(dst, quality=95)

def build(folder, music, per=2.6, fade=0.4):
    slides = sorted(glob.glob(os.path.join(folder, "feed_*.jpg")))
    tmp = tempfile.mkdtemp()
    frames = []
    for i, s in enumerate(slides):
        p = os.path.join(tmp, f"f{i:02d}.jpg"); pad(s, p); frames.append(p)
    Image.open(frames[0]).save(os.path.join(folder, "reel_cover.jpg"), quality=92)
    durs = [per + 0.6] + [per] * (len(frames) - 1)         # hold the hook a little longer
    durs[-1] += 1.0                                          # and the CTA
    total = sum(durs) - fade * (len(frames) - 1)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for f, d in zip(frames, durs):
        cmd += ["-loop", "1", "-t", f"{d + fade:.2f}", "-framerate", "30", "-i", f]
    cmd += ["-i", music]
    chains, last, off = [], "[0:v]", 0.0
    for i in range(1, len(frames)):
        off += durs[i - 1] - fade
        out = f"[x{i}]"
        chains.append(f"{last}[{i}:v]xfade=transition=fade:duration={fade}:offset={off:.2f}{out}")
        last = out
    chains.append(f"{last}format=yuv420p,scale=1080:1920,setsar=1[v]")
    a = len(frames)
    chains.append(f"[{a}:a]atrim=0:{total:.2f},asetpts=PTS-STARTPTS,afade=t=in:d=0.3,"
                  f"afade=t=out:st={total - 1.5:.2f}:d=1.5,aresample=48000[a]")
    cmd += ["-filter_complex", ";".join(chains), "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-profile:v", "high", "-preset", "medium", "-crf", "20", "-r", "30",
            "-c:a", "aac", "-b:a", "192k", "-ac", "2", "-movflags", "+faststart", "-t", f"{total:.2f}",
            os.path.join(folder, "reel.mp4")]
    subprocess.run(cmd, check=True)
    return total

if __name__ == "__main__":
    print(f"{build(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 2.6):.1f}s")
