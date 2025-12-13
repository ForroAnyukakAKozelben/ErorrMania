thisdict = {
    "Neve":"Macsek",
    "Kora": 2,
    }

print(f"A dict igy nez ki jelenleg: {thisdict}")

choice = str(input("\nKérlek add meg mit szeretnél változtatni! (Név, Kor) "))
choice = choice.lower()

if choice == "kor":
    thisdict["Kora"] = str(input("Kérlek add meg mire szeretnéd változtatni a korát!"))

if choice == "nev" or choice == "név":
    thisdict["Neve"] = str(input("Kérlek add meg mire szeretnéd változtatni a nevét!"))

print(f"Jelenleg ilyen a dict: {thisdict}")