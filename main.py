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
        code += random.choice(allChars)
    print(code)
    
    url = f'https://www.discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application'
    # 18 charcters
    requests.get(url)
    if requests.status_codes == 200:
        print(f'Code {code} is valid!')
        print(f'https://discord.gift/{code}')
    else:
        print(f'Code {code} is not valid!')
main()