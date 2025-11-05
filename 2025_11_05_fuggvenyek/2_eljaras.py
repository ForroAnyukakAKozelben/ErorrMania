def IsItEven(num):
    if num == 0:
        print("Ez a szám 0!\n")
    elif num % 2 == 0:
        print("Ez a szám pozitív!\n")
    else:
        print("Ez a szám negatív!\n")
        

while True:
    number = int(input("Kérlek adj meg egy számot és a program eldönti hogy a szám pozitív vagy negatív vagy 0.\n"))
    IsItEven(number)
    if input("Ha szeretnéd folytatni akkor i/n \n") == "n":
        break
    else:
        print("Akkor további jó szórakozást!")