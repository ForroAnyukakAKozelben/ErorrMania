while True:
    while True:
        try:
            x = int(input("Kérlek add meg azt a számot amit osztani szeretnél! "))
            y = int(input("\nKérlek add meg azt a számot amivel osztani szeretnéd a számot! "))
            print(f"Az osztás végeredménye: {round(x/y,3)}")
            break
        except (ZeroDivisionError, ValueError) as e:
            print("\nA hibakód:",e)
            print("Kérlek nullánál nagyobb, vagy kisebb SZÁMOT adj meg!\n")
    if input("Folytatod? i/n ").lower() == "n":
        print("Köszönjük a játékot!")
        break