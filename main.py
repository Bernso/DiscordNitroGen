import random
import requests
import threading

def send_discord_webhook_message(webhook_url, message):
    data = {
        "content": message,
        "username": "Webhook Bot"  # Optional: set the username of the bot
    }
    
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print(f"Message sent successfully, status code: {response.status_code}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


    
    
    
def generate_code():
    allChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    code = ''.join(random.choice(allChars) for _ in range(18))
    return code

def check_code():
    code = generate_code()
    url = f'https://www.discordapp.com/api/v9/entitlements/gift-codes/{code}'
    try:
        decider = requests.get(url)
        if decider.status_code == 200:    
            print(f'Code {code} is valid!')
            print(f'https://discord.gift/{code}')
            send_discord_webhook_message(
                "https://discord.com/api/webhooks/1243216053052506213/EZ1uWXiylcXkkVUTkNMXD56aZPDxPO9steJvgNei9nNqA_0EG0orkXb5QXNuDz2-LS0K",
                f"https://discord.gift/{code}"
                )

            input()
        else:
            print(f'Code {code} is not valid!')
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def main():
    threads = []
    for _ in range(500):  # Number of threads to run concurrently
        thread = threading.Thread(target=check_code)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':

    while True:
        main()


