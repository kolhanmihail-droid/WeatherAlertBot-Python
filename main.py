import os
import time

import requests
from dotenv import load_dotenv
load_dotenv()

def get_weather():
    api_key = os.getenv('API_KEY')
    city = os.getenv('CITY')


    if not api_key:
        print('There is no API key in .env file.')
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pl"

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            print(f"{city.upper()} - {temperature} - {description}")
        else:
            print('Error of the server')
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == '__main__':
    get_weather()





