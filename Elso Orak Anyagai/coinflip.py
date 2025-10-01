import random

print("A fej vagy írás játék lényege az az hogy amennyiben 1-est ad a programnak, akkor fej, ha 2-est akkor írás")
x = int(input("Adj meg akkor egy számot! (1 vagy 2)"))
y = random.randint(1,2)

if y == x:
    print("ELATLÁLTAAAD! Tessék igyál te is vizet!")
else:
    print("NEN TALÁÁLT! Menj és feküdj le aludni!")
