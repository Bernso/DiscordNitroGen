try:
    import random
    import requests
    import tkinter as tk
    import webbrowser
except ImportError as e:
    print(e)
    exit()

app = tk.Tk()
app.geometry("300x300")
app.title("Nitro Gen by Bernso")


def open_nitro(num1):
    if statusLabel.cget('text') == f"BEANS {num1}": # USING THIS METHOD DOES NOT WORK
        for i in range(1, 2):
            webbrowser.open_new(f"https://discord.gift/{num1}") # USING THIS METHOD DOES NOT WORK
    else:
        print("No current code found, please wait and try again...")


def startCode(): # change label
    num1 = 0
    while num1 != 70:
        num1 = random.randint(1, 100)
        if num1 == 70:
            statusLabel.configure(text=f"BEANS {num1}")
            open_nitro(num1)
        else:
            print("Invalid num1 value")

statusLabel = tk.Label(app, text="Code has not been found yet.")
statusLabel.bind("<Button-1>", open_nitro)
statusLabel.pack(padx = 20, pady = 20)

startButton = tk.Button(app, text="Start", command=startCode)
startButton.pack(padx = 20)


app.mainloop()