rendeles_input = input("Add meg a rendelésed, viszont mivel nincsen alma, ezért ezeket átcseréljük körtére! (szavakat szóközzel elválasztva): ")
rendeles = rendeles_input.split()  

boltban_van_alma = False

if not boltban_van_alma:
    rendeles = ["körte" if etel == "alma" else etel for etel in rendeles]

print("Módosított rendelés:", ", ".join(rendeles))

email = input("Add meg a Gmail címed szállításhoz: ")

if email.endswith("@gmail.com"):
    print("Gmail-es email címet adtál meg. Szóval mindjárt szállítjuk a rendelesedet!")
else:
    print("Nem Gmail-es email címet adtál meg. Majd legközelebb!")
