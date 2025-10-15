honapok = ["Január", "Február", "Március", "Április", "Május", "Június","Július", "Augusztus", "Szeptember", "Október", "November","December" ]
print("Hónapok csak úgy kiprintelve\n")
print(honapok)
print("\n")
print("Hónapok index alapján printelve\n")
print(honapok[0])
print("\n")
print("Hónapok for loop-pal printelve\n")
for i in honapok:
    print(i)
print("\n")
print("Hónapok visszafele printelve for looppal\n")
for i in range(len(honapok)-1, 0, -1): 
    print(honapok[i])