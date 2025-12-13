import random
import tkinter as tk

# Szóválasztó függvények
def easy():
    with open("C:/Users/ForroDominik/Documents/GitHub/ErorrMania/Akasztofa/konnyu.txt", "r", encoding="utf-8") as konnyu:
        words = konnyu.read().splitlines()
    return random.choice(words)

def medium():
    with open("C:/Users/ForroDominik/Documents/GitHub/ErorrMania/Akasztofa/kozepes.txt", "r", encoding="utf-8") as med:
        words = med.read().splitlines()
    return random.choice(words)

def hard():
    with open("C:/Users/ForroDominik/Documents/GitHub/ErorrMania/Akasztofa/nehez.txt", "r", encoding="utf-8") as nehez:
        words = nehez.read().splitlines()
    return random.choice(words)

def mixed():
    with open("C:/Users/ForroDominik/Documents/GitHub/ErorrMania/Akasztofa/vegyes.txt", "r", encoding="utf-8") as vegyes:
        words = vegyes.read().splitlines()
    return random.choice(words)

def book():
    with open("C:/Users/ForroDominik/Documents/GitHub/ErorrMania/Akasztofa/irodalom.txt", "r", encoding="utf-8") as irodalom:
        words = irodalom.read().splitlines()
    return random.choice(words)

# Ablak középre helyezése
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

# Gombnyomásra szó megjelenítése a Label-ben
def show_word(category):
    if category == "easy":
        word = easy()
    elif category == "medium":
        word = medium()
    elif category == "hard":
        word = hard()
    elif category == "mixed":
        word = mixed()
    elif category == "book":
        word = book()
    label.config(text=word)

# Főablak
root = tk.Tk()
root.title("Akasztófa")
root.geometry("1200x700")
center(root)

# Label a szavakhoz
label = tk.Label(root, text="Válassz egy kategóriát!", font=("Arial", 20))
label.pack(pady=50)

# Gombok
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

buttons = [
    ("Könnyű", "easy", "darkgreen"),
    ("Közepes", "medium", "orange"),
    ("Nehéz", "hard", "red"),
    ("Vegyes", "mixed", "gray"),
    ("Könyv", "book", "gray")
]

for i, (text, cat, color) in enumerate(buttons):
    b = tk.Button(
        button_frame,
        text=text,
        command=lambda c=cat: show_word(c),
        bg=color,
        fg="white",
        font=("Arial", 14),
        padx=10,
        pady=5
    )

root.mainloop()