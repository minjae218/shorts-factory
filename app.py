from flask import Flask, render_template, request, send_from_directory
from core.fetch_extra_topics import get_extra_topics
from core.video_generator_tts import generate_pro_video_with_voice
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    keywords = get_extra_topics()
    return render_template('index.html', keywords=keywords)

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['script']
    category = request.form['category']

    date_folder = datetime.now().strftime("%Y-%m-%d")
    output_dir = f"output/{category}/ko/{date_folder}"
    os.makedirs(output_dir, exist_ok=True)

    filename = f"{category}_{hash(text) % 9999}.mp4"
    output_path = os.path.join(output_dir, filename)

    generate_pro_video_with_voice(text, category, output_path)

    return f"✅ 생성 완료! <a href='/download/{category}/{date_folder}/{filename}'>다운로드</a>"

@app.route('/download/<cat>/<date>/<filename>')
def download(cat, date, filename):
    path = f"output/{cat}/ko/{date}"
    return send_from_directory(path, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
