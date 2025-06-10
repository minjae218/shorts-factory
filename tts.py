from gtts import gTTS
import os
import uuid

def generate_tts(text, lang='ko'):
    filename = f"temp_tts_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename
