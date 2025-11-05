"""1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""
continue_playing = True
colors = ["Kék", "Piros", "Zöld", "Lila", "Sárga", "Fekete", "Fehér", "Fehér", "Fehér", "Fekete"]
while continue_playing:
    
    user_input = str(input("Kérlek adj meg 1 színt! (Nagy kezdőbetű és ékezetek!): "))

    if user_input in colors:
        print("A szined már szerepel a listában, méghozzá", colors.count(user_input), "x !")
        x = input("Attól függetlenól szeretnéd hogy hozzáadjuk a listához? i/n")
        if x == "i":
            colors.append(user_input)
            print("Akkor mostmár hozzá is van adva!")
    else:
        print("Még nem szerepel benne de most hozzá is adjuk rögvest!")
        
    continue_to_play = int(input("Kérlek add meg hogy szeretnéd e még folyatni! 1 ha igen, 2 ha nem! "))
    if continue_to_play == 1:
        print("Akkor jöjjön a következő kör!")
    else:
        continue_playing = False