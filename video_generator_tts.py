from moviepy.editor import *
from moviepy.video.fx import resize
from PIL import Image, ImageDraw, ImageFont
from core.tts import generate_tts
import numpy as np
import random
import os

def create_subtitle_image(text, size=(1080, 300), font_size=60):
    font_path = "assets/fonts/NotoSansKR-Bold.otf"
    font = ImageFont.truetype(font_path, font_size)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    text_w, text_h = draw.textsize(text, font=font)
    box = (
        size[0] // 2 - text_w // 2 - 30,
        size[1] // 2 - text_h // 2 - 20,
        size[0] // 2 + text_w // 2 + 30,
        size[1] // 2 + text_h // 2 + 20
    )
    draw.rectangle(box, fill=(0, 0, 0, 150), outline=(255, 255, 255, 100), width=2)
    draw.text((size[0] // 2 - text_w // 2, size[1] // 2 - text_h // 2), text, font=font, fill="white")
    return ImageClip(np.array(img))

def apply_camera_motion(clip):
    zoom_level = random.uniform(1.05, 1.15)
    return clip.fx(resize.resize, zoom_level).set_position("center")

def generate_pro_video_with_voice(script_text, category, output_path):
    # 랜덤 자산 경로
    img_dir = f"assets/images/{category}"
    music_dir = f"assets/music_generated/{category}"

    bg_img = os.path.join(img_dir, random.choice(os.listdir(img_dir)))
    bg_music = os.path.join(music_dir, random.choice(os.listdir(music_dir)))

    # TTS 음성 생성
    tts_path = generate_tts(script_text, lang='ko')
    voice = AudioFileClip(tts_path)

    # 음악 처리
    music = AudioFileClip(bg_music).volumex(0.4)
    final_audio = CompositeAudioClip([
        music.set_duration(voice.duration),
        voice.set_start(0)
    ])

    # 영상 + 카메라 무빙
    duration = voice.duration
    base_clip = ImageClip(bg_img, duration=duration).resize(height=1920)
    base_clip = apply_camera_motion(base_clip)

    # 자막
    subtitle = create_subtitle_image(script_text).set_duration(duration).set_position(("center", "bottom"))

    final = CompositeVideoClip([base_clip, subtitle]).set_audio(final_audio)
    final = final.fadein(1).fadeout(1)
    final.write_videofile(output_path, fps=30, audio_codec='aac')
