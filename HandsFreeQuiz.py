'''
Hands-Free Trivia Challenge: Test your knowledge with this interactive voice-driven 
trivia game. Choose from a variety of categories and tackle questions of varying
difficulty levels using just your voice. Listen to the questions, speak your answers, 
and watch your score grow as you engage in this captivating and fun-filled quiz experience.
'''

import requests
import json
import random
import speech_recognition as sr
import pyttsx3 
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def title():
    title = "Speak and Score: Voice-Driven Trivia Fun"
    border = "*" * len(title) 

    print(border)
    print(f"{title}")
    print(border)

def category():
    print("In which quiz category would you like to immerse yourself?")
    print('''1.Sports(only medium lvl questions)
2.History
3.General Knowledge
4.Geography
5.Entertainment: Anime and Manga(only medium lvl questions)''')
    time.sleep(5)
    while True:
        catinp = takeCommand().lower()
        if 'sports' in catinp:
            return 21
        elif 'history' in catinp:
            return 23
        elif 'knowledge' in catinp:
            return 9
        elif 'entertainment' in catinp:
            return 31
        elif 'geography' in catinp:
            return 22
        else:
            print("Please choose a valid category.")

def difficulty():
    print("At what level of difficulty would you like to tackle the questions?")
    print('''1.Easy
2.Medium
3.Hard''')
    time.sleep(3)
    while True:
        diffinput = takeCommand().lower()
        if 'easy' in diffinput:
            return 'easy'
        elif 'medium' in diffinput:
            return 'medium'
        elif 'hard' in diffinput:
            return 'hard'
        else:
            print("Please choose a valid difficulty level.")
    
def speak(audio, speed):
    engine.setProperty("rate", speed)
    engine.say(audio)
    engine.runAndWait()

def random_choice():
    return random.randint(1, 4)

def random_question(results):
    return random.randint(0, len(results) - 1)

def displayques(questions):
    quest = questions[random_question(questions)]
    print("Question:", quest.get('question', 'N/A'))

    correct_choice = random_choice()
    incorrect_choices = quest.get('incorrect_answers', ['N/A'])
    k = 0
    for i in range(1, 5):
        if i == correct_choice:
            print(f"{i}.{quest.get('correct_answer', 'N/A')}")
        else:
            print(f"{i}.{incorrect_choices[k]}")
            k = k + 1
    time.sleep(15)
    score = answer_analysis(correct_choice)
    return score

def answer_analysis(correct_choice):
    correc = str(correct_choice)
    print(correc)
    answer = takeCommand().lower()

    if 'one' in answer:
        answer = answer.replace('one', '1')
    if 'four' in answer:
        answer = answer.replace('four', '4')
    if 'for' in answer:
        answer = answer.replace('for', '4')

    if correc in answer:
        print("You got it right!")
        speak("You got it right!", 175)
        return 5
    else:
        print("You got it incorrect!")
        speak("You got it incorrect!", 175)
        return 0

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"

def main():
    chosen_category = category()
    chosen_difficulty = difficulty()

    url = f"https://opentdb.com/api.php?amount=50&category={chosen_category}&difficulty={chosen_difficulty}&type=multiple"
    r = requests.get(url)
    qsdict = json.loads(r.text)

    total_score = 0
    j = 0
    while j < 5:
        if qsdict['response_code'] == 0:
            results = qsdict['results']
            total_score += displayques(results)
            print("\n" + "-" * 40 + "\n") 
        else:
            print("Error fetching questions.")
        j += 1
    
    print("Your total score:", total_score)

if __name__ == "__main__":
    title()
    main()
