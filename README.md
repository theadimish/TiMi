# TiMi
🤖 TiMi – Your Personal AI Desktop Assistant
TiMi (short for Tendentious Intrinsic Modus Inference) is a smart AI-powered voice assistant for Windows. Designed as a desktop application with a sleek PyQt5 GUI, TiMi listens to your voice commands and performs a wide range of useful tasks — from opening apps and playing music to checking the weather and battery status.

Developed by Solo Coder Aditya — a creative mind passionate about AI, automation, and voice-powered systems.

👤 Creator
Aditya Mishra

🚀 Features & Capabilities
🎙️ Voice-Controlled Commands

Speak naturally, TiMi listens and responds.

Trigger tasks with simple phrases like "open YouTube", "what's the time", or "take a screenshot".

🧠 Smart Wikipedia Search

Ask factual questions, and TiMi will summarize answers from Wikipedia.

🌤️ Weather Updates

Instantly fetches the current temperature in Bengaluru (or modifiable to other locations).

🔋 Battery Status Monitor

Announces battery percentage and gives power-saving advice.

📸 Screenshot Capture

Takes and saves screenshots via voice prompt with custom names.

📂 App & Browser Automation

Open/close:

Google (Edge)

YouTube

IntelliJ IDEA

VS Code

WhatsApp

🎵 Music Playback

Plays random songs from your local music directory.

🔉 System Volume Control

Voice-controlled volume up/down, mute, and unmute.

🖼️ Modern GUI with Animation

Built using PyQt5

Animated background and wave effects

Custom buttons for starting and terminating the assistant

🖥️ System Commands

Restart or shut down your PC with your voice.

🧱 Project Structure
bash
Copy
Edit
TiMi/
├── TiMi.py         # Main logic and voice assistant functionality
├── TiMiUi.py       # PyQt5 UI file (auto-generated from TiMiUi.ui)
├── designer.exe    # Qt Designer tool to edit the UI visually (optional)
└── assets/         # Referenced images (e.g., AIbg.png, AIwave1.gif)
💡 Tech Stack
Tech	Purpose
Python	Core programming language
PyQt5	GUI development
pyttsx3	Text-to-speech voice engine
speech_recognition	Voice input handling
OpenCV	Camera input (webcam)
BeautifulSoup + requests	Web scraping (weather)
pyautogui	GUI automation (volume, screenshot, etc.)
Wikipedia API	Knowledge fetching
psutil	Battery monitoring

📥 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/TiMi.git
cd TiMi
2️⃣ Install Dependencies
Make sure you have Python 3.8+ and pip installed. Then run:

bash
Copy
Edit
pip install -r requirements.txt
Required Python packages (if requirements.txt is not present):

bash
Copy
Edit
pip install pyttsx3 SpeechRecognition wikipedia pyautogui psutil opencv-python pyqt5 requests beautifulsoup4 pywhatkit
3️⃣ Run the App
bash
Copy
Edit
python TiMi.py
🎬 How It Works
Launch the PyQt5 GUI.

Click Invoke to activate TiMi.

Speak your command (e.g., "open YouTube", "play music").

TiMi listens, processes your voice, and performs the task.

Click Terminate to close the application.

📌 Future Improvements
Add wake-word detection (e.g., "Hey TiMi") using Vosk or Snowboy

Support for multiple languages

Add authentication and personalized profiles

Expand to mobile version using Kivy

Deploy as a cross-platform assistant (Windows, Linux)

Replace hardcoded paths with user-configurable settings

📝 License
This project is for educational and demonstration purposes only.

📬 Contact
Have ideas, questions, or want to collaborate?
Reach out or open an issue.

Made with ❤️ by Aditya Mishra

Let me know if you want me to also generate:

requirements.txt

GitHub banner or screenshots

.exe packaging instructions (via PyInstaller)
