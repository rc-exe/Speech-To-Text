import os
import whisper
import torch
import speech_recognition as sr
import warnings
import time
from flask import Flask, render_template, jsonify
warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load Whisper Model (Set to CUDA if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("tiny").to(device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()
    last_speech_time = time.time()  # Track last detected speech time

    try:
        with sr.Microphone() as source:
            print("🎙 Listening continuously... Speak anytime!")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            while True:
                try:
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)

                    # Update last detected speech time
                    last_speech_time = time.time()

                    # Define a writable directory for temp audio
                    temp_dir = os.path.join(os.getcwd(), "temp_audio")
                    os.makedirs(temp_dir, exist_ok=True)

                    temp_audio_path = os.path.join(temp_dir, "audio.wav")

                    # Save audio
                    with open(temp_audio_path, "wb") as f:
                        f.write(audio.get_wav_data())

                    result = model.transcribe(temp_audio_path)

                    return jsonify({"success": True, "text": result["text"]})

                except sr.WaitTimeoutError:
                    # Check if 10 seconds have passed without speech
                    if time.time() - last_speech_time > 10:
                        print("⏳ No speech detected for 10 seconds. Stopping...")
                        break  # Stop listening

                    print("⏳ No speech detected, still listening...")
                    continue  # Keep listening

    except Exception as e:
        return jsonify({"success": False, "error": f"Unexpected error: {str(e)}"})

    return jsonify({"success": False, "error": "No speech detected for 10 seconds. Stopping..."})

if __name__ == '__main__':
    app.run(debug=True)
