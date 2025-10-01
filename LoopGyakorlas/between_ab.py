"""2. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket.
"""


x = int(input("Kérlek adj meg 1 számot! "))
y = int(input("Kérlek adj meg mégegy számot! "))


if x < y:
    for i in range(x+1, y): 
        print(i)
else:
    for i in range (x-1,y,-1):
        print(i)
        