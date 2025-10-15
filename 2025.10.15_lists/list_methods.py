honapok = ["Január", "Február", "Március", "Április", "Május", "Június","Július", "Augusztus", "Szeptember", "Október", "November","December" ]
print("Ez az alap lista:", honapok)
honapok.pop(11)             #Kitörli a 11. elemet --> December
print("Pop-olt lista:", honapok)
honapok.append("December")
print("Appendelt lista:", honapok)
del honapok[2]
print("Del[2]-s element", honapok)
honapok.insert(2, "Március")
print("Insert 2-es indexre Márciust:", honapok)



honapok.clear()
print("Clear után:", honapok)