x = int(input("Kérlek adj meg 1 egész számot, és kiszámolja a program 1-től az ön számáig a számok összegét!"))
y = 0

for i in range(x):
    y += i

print(f"A számok összege: {y}")   