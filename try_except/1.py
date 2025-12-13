list = []

def isItNumber(number):
    x = isinstance(number, int)
    if x == True:
        list.append(number)
    else:
        print("Kérlek szépen egy számot adj már meg! Lehetőleg egészet, mert ez nem egy egész szám!")

while True:
    try:
        isItNumber(int(input("\nKérlek adj meg egy számot aztán hozzáadjuk egy listához! ")))
    except ValueError as e:
        print(e)
    print(f"A jelenlegi lista így néz ki: {list}")
    if input("Folytatnád? i/n ").lower() == "n":
        print("Köszönjük hogy ezt a programot használtad, bye!")
        break