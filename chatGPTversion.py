import random
import string
import requests

def generate_random_code(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def check_code(code):
    url = f"https://www.discordapp.com/api/v9/entitlements/gift-codes/{code}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Valid code found: {code}")
        return True
    else:
        print(f"Invalid code: {code}")
        return False

def main():
    while True:
        generated_code = generate_random_code(18)
        if check_code(generated_code):
            break

if __name__ == "__main__":
    main()
