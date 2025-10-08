x = str(input("Kérlek adj meg egy szöveget a blogomhoz! Jó lenne ha szerepelne benne a \"Python\" szó! "))
if x.count("Python") == 0:
    print("Sajna nem teszem ki mert nincsen benne az hogy Python.")
else:
    print("Köszi hogy beleírtad! Megy is a blogomba! ")