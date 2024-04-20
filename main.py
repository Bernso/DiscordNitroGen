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
    print(code)
    # 18 charcters
    
    url = f'https://www.discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application'
    requests.get(url)
    if requests.status_codes == 200:
        print(f'Code {code} is valid!')
        print(f'https://discord.gift/{code}')
        return False
    else:
        print(f'Code {code} is not valid!')
    
while True:
    main()  