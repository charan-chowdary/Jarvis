from sys import excepthook
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 & hour<=12 :
        speak('Good Morning!')
    elif hour>=12 & hour<=18 :
        speak('Good Afternoon!')
    else :
        speak('Good Evening!')
    
    speak('Hi I am jarvis your personal assistant!, how can I help you sir?')

def takeCommand() :
    #uses microphone to take as input and converts it to the string text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again..")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        
        elif 'open my projects' in query:
            pj_dir = "C:\\Users\\Lenovo\\PROJECTS"
            projects = os.listdir(pj_dir)
            print(projects)
            projects = os.listdir(pj_dir, projects[0])

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
            print(strtime)

        elif 'open code' in query:
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'email to kc' in query:
            webbrowser.open("gmail.com")