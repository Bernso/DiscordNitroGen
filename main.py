try:
    import random
    import requests
except ImportError as e:
    print(e)
    exit()

def main():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    nums = '1234567890'
    allChars = f'{nums}{chars}'
    code = ''
    for i in range(1, 19): # add 1 to the final value
        code.join(random.choice(allChars))
    print(code)
    #code = random.choice(allChars)
    #url = f'https://www.discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application'
    # 18 charcters
    #requests.get()
main()