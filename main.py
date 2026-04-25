import os
from send import send_to_discord
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather():

    api_key = os.getenv('API_KEY')
    city = os.getenv('CITY')
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")


    if not api_key:
        print('There is no API key in .env file.')
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pl"

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            temperature = round(data['main']['temp'], 1)
            description = data['weather'][0]['description']
            full_msg = f"🌤️ **Raport pogodowy dla: {city.upper()}**\n"
            full_msg += f"Temperatura: {temperature}°C\n"
            full_msg += f"Warunki: {description.capitalize()}\n"

            # Twoja logika alertów
            if temperature > 30:
                full_msg += "🔥 **UWAGA:** Możliwy upał, lepiej zostać w domu!"
            elif temperature < 0:
                full_msg += "❄️ **UWAGA:** Jest zimno, ubierz się ciepło!"

            # WYSYŁAMY!
            print(f"Próba wysłania: {full_msg}")
            send_to_discord(full_msg)
        else:
            print(f"Błąd API! Kod: {data.get('cod')}, Wiadomość: {data.get('message')}")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == '__main__':
    get_weather()





