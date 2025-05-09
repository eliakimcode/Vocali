from flask import Flask, request, jsonify
import whisper
import pyttsx3

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/api/stt', methods=['POST'])
def speech_to_text():
    audio = request.files['audio']
    audio.save("temp.wav")
    result = model.transcribe("temp.wav")
    return jsonify({"text": result['text']})

@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get('text')
    engine = pyttsx3.init()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    return jsonify({"message": "Audio created", "audio_path": "output.mp3"})

if __name__ == '__main__':
    app.run(debug=True)
