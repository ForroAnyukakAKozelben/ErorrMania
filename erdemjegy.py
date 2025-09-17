""" """ 
while True:
    try:
        points = int(input("Kérlek add meg a pontszámot! "))
        break
    except ValueError: 
        print("Kérlek egy SZÁMOT adj megy 0-100-ig. \n ")

while points < 0 or points > 100:
        points = int(input("Kérlek egy SZÁMOT adj megy 0-100-ig. \n"))
        
    

if points < 50:
    print("Elégtelen érdemjegy! ")
elif points < 65:
    print("Elégséges érdemjegy! ")
elif points < 80: 
    print("Közepes érdemjegy! ")
elif points < 90:
    print("Jó érdemjegy! ")
else:
    print("Jeles érdemjegy! ")