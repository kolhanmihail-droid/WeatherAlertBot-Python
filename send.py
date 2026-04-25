import requests
import os

def send_to_discord(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("Błąd: Brak DISCORD_WEBHOOK_URL w pliku .env")
        return

    # Przygotowujemy paczkę z wiadomością
    payload = {"content": message}

    # Wysyłamy POST do Discorda
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print("✅ Powiadomienie wysłane na Discorda!")
    else:
        print(f"❌ Nie udało się wysłać wiadomości: {response.status_code}")