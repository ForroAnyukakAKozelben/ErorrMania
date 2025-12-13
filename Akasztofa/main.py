import random
import os
import time
import platform
def easy():
    with open("C:/Users/ForroDominik/Documents/GitHub/ErorrMania/Akasztofa/konnyu.txt", "r", encoding="utf-8") as konnyu:
        words = konnyu.read().splitlines()  
    return random.choice(words)

def medium():
    with open("C:/Users/ForroDominik/Documents/GitHub/ErorrMania/Akasztofa/kozepes.txt", "r", encoding="utf-8") as medium:
        words = medium.read().splitlines()  
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

welcome_text = """
                    Üdvözlünk az akasztófa játékunkban!
                
        Kis ismertető a témákról:
        - Van a könnyű téma (Egyszerű, gyakori szavak).
        - Van a közepes szavak listája.
        - Van a nehezebb, ritkábban használatos szavak listája.
        - Van a vegyes téma, amelyben országok és foglalkozások nevei találhatók.
        - És legvégül van az irodalmi téma, ahol művek és művek szereplői vannak.

        A szabályok nagyon egyszerűek:
        - Minden szó magyar szó, lehetnek ékezetek.
        - Az olyan betűket, mint gy, sz, ty és társait külön kell tippelni.
        - Ügyeljünk, hogy ne számot és ne speciális jelet tippeljünk.
        - A már használt betűk nem látszódnak, csak ha a felhasználó beírja: "szavak".
        - A hibázási lehetőségek száma: 6.

        A konzol 30 másodperc múlva törlődik.
"""

print(welcome_text)
word = ""
rnd_while = True
# Fél perc várakozás
for i in range(30, 0, -1):
    print(f"\rTörlés {i} másodperc múlva...", end="")
    time.sleep(1)

# Konzol törlése platformfüggően
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")


while True:
    guess = []
    while rnd_while:
        print("Témák: könnyű, közepes, nehéz, vegyes, irodalom")
        choice = str(input("Rendben van, eljött az ideje hogy kiválassza a témát: "))
        choice = choice.lower()
        if choice == "könnyű" or choice == "konnyu":
            word = easy()
            rnd_while = False
        elif choice == "közepes" or choice == "kozepes":
            word = medium()
            rnd_while = False
        elif choice == "nehéz" or choice == "nehez":
            word = hard()
            rnd_while = False
        elif choice == "vegyes":
            word = mixed()
            rnd_while = False
        elif choice == "irodalom":
            word = book()
            rnd_while = False
        else: 
            print("Kérlek ne jól írd be! ")
    
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
    for x in word:
        if x == " ":
            guess += " "
        elif x == "-":
            guess += "-"
        elif x == ":":
            guess += ":"
        else:
            guess.append("_")
    