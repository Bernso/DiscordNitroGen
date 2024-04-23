import customtkinter as tk, requests, random, webbrowser, os

# Creates an icon folder
Icon = "Icon"
if os.path.exists(Icon):
    print("'Icon' folder already exists")
else:
    print("Creating Icon folder")
    os.makedirs(Icon)
    print("'Icon' folder created")

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
            for i in range(1, 15):
                print(f'Code {code} is valid!')
                print(f'https://discord.gift/{code}')
                statusLabel.configure(text=f"Code found!\nhttps://discord.gift/{code}", font=('helvetica', 14, 'bold'))
                webbrowser.open_new(f"https://discord.gift/{code}")
            return code
        
        else:
            print(f'Code {code} is not valid!')
            
def download_ico(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        if os.path.exists("Icon/Arhururan.ico"):
            print("Icon has already been downloaded")
        else:
            try:
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print("ICO file downloaded successfully!")
            except Exception as e:
                print(f"Failed to download ICO file.\nError: {e}")
                #errorReporting(e)
                input()
    else:
        print("Failed to download ICO file.")
        input()

ico_url = "https://raw.githubusercontent.com/Bernso/Icons/main/Arhururan.ico"
save_path = os.path.join(Icon, "Arhururan.ico")  # Full file path including directory
download_ico(ico_url, save_path)
print("ICO file download process completed.")
      
def startCode():
    startButton.destroy()
    main()


def open_nitro(event):
    for i in range(1, 11):
        webbrowser.open_new(f"https://www.youtube.com/watch?v=dQw4w9WgXcQ")


root = tk.CTk()
root.geometry("300x150")
root.title("Nitro Gen by Bernso")
root.iconbitmap("Icon/Arhururan.ico")

statusLabel = tk.CTkLabel(root, text="Code has not been found yet.")
statusLabel.bind("<Button-1>", open_nitro)
statusLabel.pack(padx = 20, pady = 20)

startButton = tk.CTkButton(root, text="Start", command=startCode)
startButton.pack(padx = 20)



if __name__ == "__main__":
    root.mainloop()