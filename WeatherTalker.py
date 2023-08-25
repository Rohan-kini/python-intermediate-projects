import requests
import json
import pyttsx3

def get_weather_info(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    r = requests.get(url)
    return json.loads(r.text)

def speak_weather(city, temp, humidity):
    speaker = pyttsx3.init()
    speaker.say(f"The current temperature of {city} is {temp} degrees Celsius.")

    #The ranges are in general taken from chat gpt...
    #Humidity levels can vary based on factors such as precipitation, evaporation, city pollution, and more, which can influence the interpretation of humidity information.
    
    if humidity < 60:
        speaker.say(f"Moderate humidity around {humidity} with minimal difference between actual temperature and 'feels like' temperature. Suggests relatively comfortable conditions.")
    elif 60 <= humidity < 85:
        speaker.say(f"High humidity around {humidity}. Staying hydrated, wearing appropriate clothing, and taking precautions to avoid heat-related illnesses are essential in such conditions.")
    else:
        speaker.say(f"Very high humidity. Stay indoors.")
    
    speaker.runAndWait()

if __name__ == "__main__":
    api_key = input("Enter your WeatherAPI API key: ")
    city = input("Enter the name of the city: ")
    
    weather_data = get_weather_info(api_key, city)
    
    temp = weather_data['current']['temp_c']
    humidity = weather_data['current']['humidity']
    
    print(f"Temperature: {temp} degrees Celsius")
    print(f"Humidity: {humidity}")
    
    speak_weather(city, temp, humidity)

