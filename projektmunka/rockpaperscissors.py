import random
folytat = True
while folytat:
    rps = int(input("Add meg melyiket akarod (kő (1), papír (2), olló (3): "))
    x = random.randint(1,3)
    if x == rps:
        print("Döntetlen")
        cont = input("Folytatod a játékot(I/N):")
        if cont == 'N':
            folytatja = False
    elif x == 1 and rps == 2:
        print("A papír becsomagolja a követ, nyertél")
        cont = input("Folytatod a játékot(I/N):")
        if cont == 'n':
            folytatja = False
    elif x == 2 and rps == 3:
        print("Az olló elvágja a papírt, nyertél")
        cont = input("Folytatod a játékot(I/N):")
        if cont == 'n':
            folytatja = False
    elif x == 3 and rps == 1:
        print("A kő eltöri az olló élét, nyertél")
        cont = input("Folytatod a játékot(I/N):")
        if cont == 'n':
            folytatja = False
    elif rps == 1 and x == 2:
        print("A papír becsomagolja a követ, vesztettél")
        cont = input("Folytatod a játékot(I/N):")
        if cont == 'n':
            folytatja = False
    elif rps == 2 and x == 3:
        print("Az olló elvágja a papírt, vesztettél")
        cont = input("Folytatod a játékot(I/N):")
        if cont == 'n':
            folytatja = False
    elif rps == 3 and x == 1:
        print("A kő eltöri az olló élét, vesztettél")
        cont = input("Folytatod a játékot(I/N):")
        if cont == 'n':
            folytatja = False


