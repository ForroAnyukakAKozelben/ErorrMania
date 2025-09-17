x = int(input("Adj meg egy számot pusza! Erről megmondom hogy pozitív e vagy negatív vagy esetleg "))

print()

if x < 0:
    print("Ez a szám negatív te lüke!")

elif x > 0:
    print("Pozitív YAAAY")
    
else:
    print("Ez nulla halo")
    
szam = int(input("Itt meg leccike adj eegy szamot osztashoz puszi a pocidra picirigó "))

while szam == 0:
    if szam == 0:
        szam = int(input("HE NE LEGYEN MAR NULLAAAAA "))

print("Ez lesz a kimaradás az osztásból: ", x%szam)