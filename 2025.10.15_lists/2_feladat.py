"""
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, 
a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, 
és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!"""
import random

def DeleteNumb(numbers, delete):
    return [x for x in numbers if x != delete]

numbers = [] 
for i in range(10): 
    numbers.append(random.randint(1,3))

print("Eredeti lista:", numbers)
delete = int(input("Kérlek adj meg egy számot, amit törölni szeretnél a listából: "))

print("Törlés után:", DeleteNumb(numbers, delete))