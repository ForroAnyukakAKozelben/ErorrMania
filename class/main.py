from allat import Allat
from emlos import Emlos
from emlos import Macska
from nem_emlos import Madar
from nem_emlos import Keteltu
from nem_emlos import Hullo

allat1 = Allat("Bodri","kutya",5,"kert","nagy")
allat2 = Allat("Blöki","kutya",10,"lakás","kicsi")
print(allat1)
emlos1 = Emlos("Bodri","kutya",5,"kert","nagy","rozsaszin")
print(emlos1)
macska1 = Macska("Hubert",4,"ház","kicsi","fehér")
macska1.dorombol()