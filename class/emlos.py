from allat import Allat
class Emlos(Allat):
    def __init__(self,nev,faj,eletkor,elohely,meret,szorzet_szine,):
        super().__init__(nev,faj,eletkor,elohely,meret)
        self.szorzet_szine = szorzet_szine
    
    def __str__(self):
        return super().__str__() + f", szőrzete szine: {self.szorzet_szine}"

class Macska(Emlos):
    def __init__(self, nev, eletkor, elohely, meret, szorzet_szine):
        super().__init__(nev, "macska", eletkor, elohely, meret, szorzet_szine)
    
    def __str__(self):
        return super().__str__()   + f", szőrzete szine: {self.szorzet_szine}"
    def dorombol(self):
        print(f"{self.nev} jelenleg dorombol! Grrrr")
        
class Kutya(Emlos):
    def __init__(self, nev, eletkor, elohely, meret, szorzet_szine):
        super().__init__(nev, "kutya", eletkor, elohely, meret, szorzet_szine)
    def __str__(self):
        return super().__str__() + f", szőrzete szine: {self.szorzet_szine}"
    def ugat(self):
        return f"{self.nev} jelenleg ugat!"
