import random
import requests
import threading
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

WEBHOOK_URL = "https://discord.com/api/webhooks/1243216053052506213/EZ1uWXiylcXkkVUTkNMXD56aZPDxPO9steJvgNei9nNqA_0EG0orkXb5QXNuDz2-LS0K"
NUM_THREADS = 10  # Number of threads to run concurrently
RATE_LIMIT_DELAY = 0.3  # Delay in seconds to respect rate limits

def send_discord_webhook_message(webhook_url, message):
    data = {
        "content": message,
        "username": "Webhook Bot"  # Optional: set the username of the bot
    }

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        logging.info(f"Message sent successfully, status code: {response.status_code}")
    except requests.exceptions.HTTPError as err:
        logging.error(f"HTTP error occurred: {err}")
    except Exception as err:
        logging.error(f"Other error occurred: {err}")

def generate_code():
    allChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    code = ''.join(random.choice(allChars) for _ in range(18))
    return code

def check_code():
    code = generate_code()
    url = f'https://www.discordapp.com/api/v9/entitlements/gift-codes/{code}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f'Code {code} is valid!')
            logging.info(f'https://discord.gift/{code}')
            send_discord_webhook_message(WEBHOOK_URL, f'https://discord.gift/{code}')
            input()
        else:
            logging.info(f'Code {code} is not valid!')
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")

def main():
    while True:
        threads = []
        for _ in range(NUM_THREADS):
            thread = threading.Thread(target=check_code)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        logging.info(f"Completed batch of {NUM_THREADS} checks. Waiting to respect rate limits...")
        time.sleep(RATE_LIMIT_DELAY)

if __name__ == '__main__':
    main()
