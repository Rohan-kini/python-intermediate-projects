import requests
import json
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def title():
    title = "Welcome to Quote Express: Where Words Come to Life!"
    border = "*" * len(title)  

    print(border)
    print(f"{title}")
    print(border)

def speak(quote,speed):
    engine.setProperty("rate", speed)
    engine.say(quote)
    engine.runAndWait()

def fetch_random_quote():
    url = "https://zenquotes.io/api/random"#gives a random quote do not require API_KEY...
    r = requests.get(url)
    quotedict =json.loads(r.text)
    if quotedict:
        return quotedict[0]['q']  
    return None

def main():
    input("Press Enter to fetch a random quote...")
    
    quote = fetch_random_quote()
    
    if quote:
        print("\nRandom Quote:")
        print(quote)
        speak(quote,175)
    else:
        print("Unable to fetch a quote at the moment.")

if __name__ == "__main__":
    title()
    main()

