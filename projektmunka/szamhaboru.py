import random

game = True
wins = 0
loose = 0
tie = 0
print("Üdv a Számháború játékban!")

while game:
    
    x = random.randint(1,6)
    player = 0
    
    
    while True:
        try:
            player = int(input("Kérlek adj meg egy számot 1-6-ig! "))
            if 1 <= player <= 6:
                break
            else:
                print("Csak 1 és 6 közötti számot adhatsz meg!")
        except ValueError:
            print("EGY SZÁMOT ADJ MEG A MEGADOTT ÉRTÉKEN BELÜL!")
    
    print(f"A gép száma {x} \nA te számod pedig {player}! ")
    
    if x == player:
        tie += 1
        print("Döntetleeeen yaaay! Legalább nem vesztettél!")
    elif x > player:
        loose += 1
        print("Sajnos most vesztettél! Előfordul, bocseeesz!")
    elif player > x:
        wins += 1
        
    print(f"Eddigi eredmény: {wins} nyerés, {loose} vereség, {tie} döntetlen!")
    
    while True:
        leave = input("Szeretnél újra játszani? (i/n): ").lower()
        if leave == "i":
            break
        elif leave == "n":
            print("Köszi a játékot!")
            bool = False
            break
        else:
            print("Csak 'i' vagy 'n' lehet a válaszod!")
    
    print(f"Végső eredmény: {wins} nyerés, {loose} vereség, {tie} döntetlen!")