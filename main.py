import sys
import pyttsx3
import speech_recognition 
from GreetMe import greetMe
from Functions import main

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

mode = "back" # if you want to give input without audio change it to "fore"

def speak(audio):
    if mode == "fore":
        pass
    elif mode == "back":
        engine.say(audio)
        engine.runAndWait()
    else:
        print("Wrong Input Mode!")
        sys.exit()

def takeCommand():
    if mode == "fore":
        usr = input("Type Here:-  ")
        return usr
    elif mode == "back":
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening ...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source,0,4)

        try:
            print("Recognizing ...")
            query  = r.recognize_google(audio,language='en-in')
            print(f"You Said: {query}\n")
        except Exception:
            print("Say that again please ...")
            return "None"
        return query
    else:
        print("Wrong Input Mode!")
        sys.exit()

if __name__ == "__main__":
    while True:
        try:
            query = takeCommand().lower()
            if "wake up" in query:
                greetMe()

                while True:
                    query = takeCommand().lower()
                    if "go to sleep" in query:
                        speak("Ok sir , You can me call anytime")
                        break
                    else:
                        main(query)
            elif "stop" in query:
                speak("Ok sir , You can call me anytime!")
                sys.exit()
        except Exception as e:
            print(e)