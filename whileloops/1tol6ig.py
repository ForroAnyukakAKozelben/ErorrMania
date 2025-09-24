"""1. Feladat
Írj egy programot, amely kiírja a páros számokat 1 és 10 között!

2. Feladat
Írj egy programot, amely csökkenő sorrendben írja ki a számokat 1 és 10 között!

3. Feladat
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!

4. Feladat
Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!

5. Feladat
Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.

6. Feladat
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt."""
import random

"""Feladat 1"""
for i in range(0,10,+2):
    print(i)

"""Feladat 2"""
for i in range(10,0,-1):
    print(i)


"""Feladat 3"""
for i in range(9,0,-2):
    print(i)


"""Feladat 4"""

x = True
z = str(input("Kérlek adj meg egy mondatot! "))
y = int(input("Kérlek add meg hogy hányszor szeretnéd kiírni a mondatodat! "))

while x:
    for i in range(y):
        print(z)
        if i == y-1:
            x = False

"""Feladat 5"""

x2 = True
while x2:
    z2 = int(input("Kérlek adj meg egy páros számot! "))
    if z2 % 2 == 0:
        print("A szám amit megadtál tényleg páros! ")
        x2 = False
        
"""Feladat 6"""

print("Ez a program egy 1-12-ig terjedő intervallumon 20 véletlenszerű számot állít elő, és csak a 3-al oszthatókat írja ki!")
x3 = 0
for i in range(20):
    x4 = random.randint(1,12)
    if(x4 % 3 == 0):
        print(x4)
        x3 += 1
