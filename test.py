try:
    import random
    import requests
except ImportError as e:
    print(e)
    exit()

def main():
    num = int(random.randint(1, 20))
    
    if num == 19:
        print('Success!Success!Success!Success!Success!Success!Success!Success!')
        input()
    else:
        print('Failed!')
        
    
while True:
    main()  