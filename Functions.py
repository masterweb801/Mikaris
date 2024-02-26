from main import speak
from db import json
import webbrowser
import wikipedia
import datetime
from Model import getKnowledge, answerQuestion

def main(query: str):
    query = query.lower()
    if query=="none":
        pass
    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google.com")
        webbrowser.open("https://www.google.com")

    elif 'open stackoverflow' in query:
        speak("Opening StackOverflow")
        webbrowser.open("https://www.stackoverflow.com")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
    elif "get knowledge about" in query:
        subject = query.replace("get knowlwdge about ", "")
        speak(f'give me some time to gather knowledge about {subject} from internet')
        getKnowledge(subject)
        speak(f"Knowledge gain complete. Now you can ask me any questions about {subject}")
    else:
        result = json.get(query)
        if result:
            speak(result)
        else:
            answerQuestion(query)