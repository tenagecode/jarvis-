import pyttsx3
import speech_recognition as sr
import datetime
import os
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#speech to  texxt
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=2,phrase_time_limit=7 )


    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language= "en-in")
        print(f"user said: {query}")


    except Exception as e:
        speak('Say that again please')
        return "none"
    return query

#to wish the user
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak('Good morning sir')

    elif hour>12 and hour<=18:
        speak('Good afternoon sir')

    else :
        speak('Good evening sir ')
    speak('I am Jarvis sir Please tell me how may I help you')


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        #logic buliding for tasks

        if "open Notepad " in query:
            apath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"you IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak(results)
            print(results)

        elif"open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif"open google" in query:
            speak("speak, what should i search in google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif"open search bar" in query:
            webbrowser.open("www.google.com")

        elif"play song on youtube" in query:
            kit.playonyt("")

        elif"no thanks"in query:
            speak("Thanks  for using me sir, have a good day")
            sys.exit()

        speak("sir, do you have any other work")