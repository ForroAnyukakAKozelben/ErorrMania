intervall = []
harom = []
ottel = []
harommal_ottel = []
# Ez a második feladat
for i in range(1,101):
    intervall.append(i)

print("Ez az intervallumunk:\n", intervall)

for i in intervall:
    if i % 3 == 0:
        harom.append(i)
    if i % 5 == 0:
        ottel.append(i)
    if i % 3 and i % 5:
        harommal_ottel.append(i)
print("\nEzek a számok oszthatóak csak 3-al az intervallumban:\n", harom)
print("\nEzek a számok oszthatóak csak 5-el az intervallumban:\n", ottel)

# Ez az első feladat
print("Most pedig jön az első feladat megoldása 1-40-es intervallumon!")

intervall = []
harom = []

for i in range(1,40):
    intervall.append(i)

for i in intervall:
    if i % 3 == 0:
        harom.append(i)

print("\nEz pedig a legelső feladat megoldása:\n", harom)