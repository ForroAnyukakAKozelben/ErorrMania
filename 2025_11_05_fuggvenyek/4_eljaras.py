def WhichIsLonger(mylist):
    longest = min(mylist, key=len)
    return longest

list = list([])
for i in range (1,4):
    list.append(input(f"Kérlek add meg a(z) {i}. szót vagy mondatot!\n"))
longest = WhichIsLonger(list)
print(f"A legrövidebb szó a következő: {longest}!")