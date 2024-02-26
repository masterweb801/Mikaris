from main import speak
import datetime

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")
    else:
        speak("Good Evening,sir")

    speak("Hello sir, How can I help you ?")