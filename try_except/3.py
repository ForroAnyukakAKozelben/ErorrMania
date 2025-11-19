# Hozz létre egy szöveges állományt, amely tartalmaz két számot egymástól tabulátorral elválasztva! 
# Írj egy programot, amely beolvassa a fájl tartalmát, és a képernyőn megjeleníti a két szám hányadosát! 
# A programot készítsd fel az esetleges hibalehetőségekre, a felhasználó pedig kapjon a hibának megfelelő figyelmeztető üzenetet ilyen esetben!

f = open("H:\python_try_except_3.txt")
text = f.read()
num_list = []
sum = 0
for i in text:
    if isinstance(i, int):
        num_list.append(i)
        print("Ez lett berakva:", i)
for i in num_list:
    sum += i
print(i)
f.close("H:\python_try_except_3.txt")