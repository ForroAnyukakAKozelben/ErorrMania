class Allat():
    def __init__(self,nev,faj,eletkor,elohely,meret):
        self.nev = nev
        self.faj = faj
        self.eletkor = eletkor
        self.elohely = elohely
        self.meret = meret
    
    def __str__(self):
        return f"{self.nev} egy {self.faj} ami {self.eletkor} éves és {self.elohely} -ben él. Jelenlegi mérete: {self.meret}"
    


