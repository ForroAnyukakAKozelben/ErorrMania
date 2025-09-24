"""Készítsünk programot, amely segíti a burkoló mesterek munkáját.
A szükséges csempe mennyiségének a kiszámításához a program kérje be a terület szélességét és a magasságát centiméterben,
valamint, hogy hány darab csempét vásároltunk már, majd számolja ki a területét (a*b), és
hogy a 20cm*20cm méretű csempék esetén hány darabra van szükség a munka elvégzéséhez (a plusz 10%-ot az illesztések miatt illik rászámolnunk).
A program azt is állapítsa meg, és közölje a felhasználóval, hogy kell-e még vásárolnunk csempét!"""


hossz = int(input("Kérlek add meg a hosszúságot! (centiméter)\n"))
szelesseg = int(input("Kérlek add meg a szélességet!(centiméter)\n"))
csempek = int(input("Kérlek add meg hogy van-e már csempe megvásárolva! (Ha igen, akkor írd be hogy hány darab van! \n")) *400

terulet = hossz * szelesseg 
cs_darab = terulet / 400 * 1.1 *-1
szukseges = cs_darab - csempek

if terulet != csempek:
    print(f"Nincsen elegendő csempéje, mivel az ön csempéjének összterülete az {csempek} cm2 és az összerület amit le kell fednie az {terulet} cm2! \n")
else: 
    print(f"Önnek már nem kell csempét vásárolnia, mivel már van elég!")