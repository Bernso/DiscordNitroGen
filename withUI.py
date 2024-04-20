import tkinter as tk, requests, random

def main():
    allChars = f'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    code = ''
    for i in range(1, 19): # add 1 to the final value
        code += random.choice(allChars)
    # 18 charcters
    url = f'https://www.discordapp.com/api/v9/entitlements/gift-codes/{code}'
    decider = requests.get(url)
    if decider.status_code == 200:
        print(f'Code {code} is valid!')
        print(f'https://discord.gift/{code}')
        input()
    else:
        print(f'Code {code} is not valid!')



root = tk.Tk()
root.geometry("300x300")
root.title("Nitro Gen by Bernso")

statusLabel = tk.Label(root, text="Code has not been found yet.")
statusLabel.pack(padx = 20, pady = 20)












if __name__ == "__main__":
    root.mainloop()