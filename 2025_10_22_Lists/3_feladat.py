even = []

for i in range(1,41):
    if i % 2 == 0 and i % 3 == 0:
        even.append(i)
        
print("A páros számok a következők:\n", even)