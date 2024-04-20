import tkinter as tk, requests, random, webbrowser

def main():
    while True:
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
            statusLabel.configure(text=f"Code found!\nhttps://discord.gift/{code}", font=('helvetica', 14, 'bold'))
            webbrowser.open_new(f"https://discord.gift/{code}")
            return code
        else:
            print(f'Code {code} is not valid!')
def startCode():
    startButton.destroy()
    main()

def open_nitro(event):
    for i in range(1, 11):
        webbrowser.open_new(f"https://www.youtube.com/watch?v=dQw4w9WgXcQ")



root = tk.Tk()
root.geometry("300x150")
root.title("Nitro Gen by Bernso")

statusLabel = tk.Label(root, text="Code has not been found yet.")
statusLabel.bind("<Button-1>", open_nitro)
statusLabel.pack(padx = 20, pady = 20)

startButton = tk.Button(root, text="Start", command=startCode)
startButton.pack(padx = 20)











if __name__ == "__main__":
    root.mainloop()