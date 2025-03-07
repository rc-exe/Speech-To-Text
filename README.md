 🎤 Speech-to-Text Web Application  

A real-time Speech-to-Text web application built with Flask, SpeechRecognition, and Pydub.  
It records continuous speech from the microphone and converts it into text accurately.

 🚀 Features  
- ✅ Real-time speech recognition  
- ✅ Continuous listening until silence is detected  
- ✅ High accuracy speech-to-text conversion  
- ✅ Beautiful UI with smooth animations  
- ✅ Flask-based backend for processing audio  
- ✅ Social media links & contact information  

---

 📌 Installation & Setup  

 1⃣ Clone the Repository
```sh
git clone https://github.com/rc-exe/Speech-to-Text-Web-App.git
cd Speech-to-Text-Web-App
```

 2⃣ Set Up a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate   For macOS/Linux
venv\Scripts\activate      For Windows
```

 3⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

 4⃣ Download and Set Up FFmpeg (Required for `pydub`)
1. Download FFmpeg from [FFmpeg Official Site](https://ffmpeg.org/download.html).  
2. Extract the downloaded FFmpeg zip file.  
3. Copy the path to the `ffmpeg.exe` file (inside the `bin` folder).  
4. Add the following line to your Flask script (`app.py`):
```python
from pydub import AudioSegment
AudioSegment.converter = r"C:\path\to\ffmpeg.exe"   Replace with actual path
```

 5⃣ Run the Flask Application
```sh
python app.py
```
After running, open your browser and go to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)  

---

 🎯 Usage  
1. Click "Start Recording"  
2. Speak into your microphone (It will continuously listen)  
3. Wait for silence detection (Once you stop speaking, it converts to text)  
4. Text appears in the textbox  
5. Copy or use the transcribed text 🎉  

---

 🔧 Troubleshooting  
 ⚠️ Microphone Not Detected?  
- Make sure your microphone is properly connected.  
- Try running Python as an administrator.  

 ⚠️ Audio File Error (PCM WAV, AIFF, FLAC)?  
- Ensure FFmpeg is correctly installed and its path is set in `app.py`.  

 ⚠️ FFmpeg Not Found?  
- Check if `ffmpeg.exe` is accessible via `cmd`:
```sh
ffmpeg -version
```
- If not, add its bin folder path to the system environment variables.

 ⚠️ Server Errors (500, 404)?  
- Check if `index.html` is inside a `templates/` folder.  
- Run Flask with debugging:
```sh
python app.py --debug
```

---

 🛠️ Technologies Used
- Python 🐍  
- Flask 🔥  
- SpeechRecognition 🗣️  
- Pydub 🎵  
- FFmpeg 🎧  
- HTML, CSS, JavaScript 🌐  

---

 💡 Future Enhancements
- 🔹 Support for multiple languages  
- 🔹 Save transcripts as text files  
- 🔹 Add speech command-based actions  
- 🔹 Cloud storage for transcripts  

---

 📞 Contact & Socials
- ✉ Email: riteshchakramani123@gmail.com  
- 🔗 GitHub: [rc-exe](https://github.com/rc-exe)  
- 📷 Instagram: [@_ritesh_rc_](https://www.instagram.com/_ritesh_rc_?igsh=Yzh1M2JyY3d0YmR0)  

---

 🐟 License
© 2025 Ritesh Chakramani. All rights reserved.  
This project is open-source for educational purposes.  

