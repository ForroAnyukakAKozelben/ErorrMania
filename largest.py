"""
Ebben a kódsor az alábbiakat teszi: Bekér 3 számot, és azután pedig összehasonlítja őket, hogy melyik a legnagyobb a 3 közül.
"""

print("Ebben a kódsor az alábbiakat teszi: Bekér 3 számot, és azután pedig összehasonlítja őket, hogy melyik a legnagyobb a 3 közül. ")

while True:
    try:
        First = int(input("Add meg a legelső számot!\n "))
        Second = int(input("Kérlek add meg a második számot!\n "))
        Third = int(input("Kérlek add meg a harmadik számot!\n"))
        break
    except ValueError: 
        print("Kérlek egy valós számot adj meg! \n ")

if First > Second and First > Third:
    print("A legnagyobb szám: ", First)
elif Second > First and Second > Third:
    print("A legnagyobb szám: ", Second)
elif Third > First and Third > Second:
    print("A legnagyobb szám: ", Third)
    
