def Compare(num1,num2):
    if num1 == num2:
        print("Ezek egyenlőek!")
    elif num1 > num2:
        print(f"A {num1} az {num1-num2}-(v)el több!")
    elif num1 < num2:
        print(f"A {num2} az {num2-num1}-(v)el több!")

while True:
    number = int(input("Kérlek adj meg 2 számot\n"))
    number2 = int(input())
    Compare(number,number2)
    if input("Ha szeretnéd folytatni akkor i/n \n") == "n":
        break
    else:
        print("Akkor további jó szórakozást!")