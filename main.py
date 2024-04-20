try:
    import random
    import requests
except ImportError as e:
    print(e)
    exit()
def main():
    allChars = f'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    code = ''
    for i in range(1, 19): # add 1 to the final value
        code += random.choice(allChars)
    # 18 charcters
    url = f'https://www.discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application'
    decider = requests.get(url)
    if decider.status_code == 200:
        print(f'Code {code} is valid!')
        print(f'https://discord.gift/{code}')
        input()
    else:
        print(f'Code {code} is not valid!')
if __name__ == '__main__':
    while True:
        main()  