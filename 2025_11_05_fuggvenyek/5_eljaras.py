def Playground():
    print(nested_list[1])
    print(nested_list[1])
    print(nested_list[2])

nested_list = [["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"]]
coordinate1 = int(input("Kérlek adj meg 1 koórdinátát! Először 1-3 között (Ez utal a sorra!)\n"))
coordinate2 = int(input("Kérlek adj meg 1 koórdinátát! És most 1-6 között (Ez utal az oszlopra!)\n"))

nested_list[coordinate1-1][coordinate2-1] = "+"
Playground()