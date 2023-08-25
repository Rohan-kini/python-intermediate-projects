import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def title():
   title="Welcome to Rohandroid: Your Personal AI Companion "
   print(" * " * 15)
   print(title)
   print(" * " * 15)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def salutation():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am  Roh Android - rohan's personal AI . What  can  I  do  for you?") 

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1#pause of  more than one second means end of speech
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    title()
    salutation()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'live cricket score' in query:
            webbrowser.open("cricbuzz.com")

        elif 'play video' in query:
          video_name = query.replace('play video', '')
          speak(f"Playing {video_name} on YouTube")
          pywhatkit.playonyt(video_name) 

        elif 'search' in query:
            search_query = query.replace('search', '')
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day!")
            break 
