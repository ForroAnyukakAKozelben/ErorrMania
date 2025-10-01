import random
szam = random.randint(1,3)
x = int(input("Adj meg egy számot 1-3 között!"))
if x == szam:
    print(f"A nyertes szám a {szam} volt! Nyert!")
else:
    print(f"A nyertes szám a {szam} volt! Vesztett!")