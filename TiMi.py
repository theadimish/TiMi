import pyttsx3
import speech_recognition as sr
import datetime
import cv2
import psutil
import wikipedia
import webbrowser
import random
import os
import pywhatkit
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
from sys import path
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am TeeMi, Adddi's virtual assistant. Please tell me how may I help you")


def takeCommand(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    query = query.lower()
    return query

    def TaskExecution(self):
        if __name__ == "__main__":
            wishMe()
            while True:
                # if 1:
                self.query = self.takeCommand()

                if 'wikipedia' in self.query:
                    speak('Searching wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)

                elif 'your name' in self.query or 'full form' in self.query or 'stands for' in self.query:
                    speak("My name is TeeMi, which stands for Tendentious Intrinsic Modus Inference")

                elif "what's the time" in self.query or 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"My owner, the time is {strTime}")

                elif 'open camera' in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif 'battery' in self.query or 'power left' in self.query or 'how much power' in self.query:
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"your system have {percentage} percent battery")
                    if percentage >= 60:
                        speak("we have enough power to continue our work")
                    elif percentage >= 40 and percentage < 60:
                        speak("you should connect our system to charging point to charge our battery")
                    elif percentage >= 20 and percentage < 40:
                        speak("we don't have enough power to work, please connect to charging")
                    elif percentage < 20:
                        speak("we have very low power, please connect to charging the system will shutdown very soon")

                elif 'open google' in self.query:
                    speak("What should i search on google")
                    cm = self.takeCommand().lower()
                    webbrowser.open(f"{cm}")

                elif 'close google' in self.query:
                    speak("Okay, closing google")
                    os.system("taskkill /f /im msedge.exe")

                elif 'open youtube' in self.query:
                    speak("What should i play on youtube")
                    cm = self.takeCommand().lower()
                    pywhatkit.playonyt(f"{cm}")

                elif 'close youtube' in self.query:
                    speak("Okay, closing youtube")
                    os.system("taskkill /f /im brave.exe")

                elif 'play music' in self.query or 'play song' in self.query:
                    speak("playing music")
                    music_dir = 'D:\\songs'
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    print(songs)
                    os.startfile(os.path.join(music_dir, rd))

                elif 'open intellij idea code' in self.query or 'open idea code' in self.query:
                    speak("opening intellij idea code")
                    eclipsepath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2023.3.3\\bin\\idea64.exe"
                    os.startfile(eclipsepath)

                elif 'close intellij idea code' in self.query or 'close idea code' in self.query:
                    speak("Okay, closing intellij idea code")
                    os.system("taskkill /f /im idea64.exe")

                elif 'open vs code' in self.query:
                    speak("opening vs code")
                    vscodepath = "C:\\Users\\Govind\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(vscodepath)

                elif 'close vs code' in self.query:
                    speak("Okay, closing vs code")
                    os.system("taskkill /f /im code.exe")

                elif 'open whatsapp' in self.query:
                    speak("opening whatsapp")
                    whatsapppath = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2349.2.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"
                    os.startfile(whatsapppath)

                elif 'close whatsapp' in self.query:
                    speak("Okay, closing whatsapp")
                    os.system("taskkill /f /im whatsapp.exe")

                elif 'increase volume' in self.query:
                    pyautogui.press("volumeup")

                elif 'decrease volume' in self.query:
                    pyautogui.press("volumedown")

                elif 'unmute' in self.query or 'mute volume' in self.query:
                    pyautogui.press("volumemute")

                elif 'unmute' in self.query or 'unmute volume' in self.query:
                    pyautogui.press("volumeunmute")

                elif 'switch the window' in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
                    speak("please, tell me the name for this screenshot")
                    name = self.takeCommand().lower()
                    speak("please hold the screen for a while...")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"C:\\Users\\Govind\\Pictures\\Screenshots\\{name}.png")
                    speak("i'm done, your screenshot is saved")

                elif 'temperature' in self.query or 'weather' in self.query:
                    search = "temperature in Bengaluru"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"current {search} is {temp}")

                elif 'restart the system' in self.query:
                    speak("restarting the system")
                    os.system("shutdown /r /t 5")

                elif 'shutdown the system' in self.query:
                    speak("Shutting down the system")
                    os.system("shutdown /s /t 5")

                elif 'you can sleep' in self.query or 'you can leave' in self.query:
                    speak("Okay, thanks for using me, you can call me anytime...")
                    sys.exit()
