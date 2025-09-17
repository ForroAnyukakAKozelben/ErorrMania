
while True:
    try:
        Year = int(input("Adj meg egy évszámot! \n "))
        break
    except ValueError:
        print("Számot adj meg! ")


if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
        print("Szökőév, yay!")
else: 
        print("Nem szökőév!")