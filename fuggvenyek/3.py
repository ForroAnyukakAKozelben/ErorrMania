list = []
def harommal_oszthatok(list):
    occourances = 0
    
    for i in list:
        if i % 3 == 0:
            occourances += 1
    return occourances

for i in range(int(input("Kérlek add meg mennyi számod van amit tesztelnél hogy oszthatóak e hárommal!\n"))):
    
    list.append(int(input("\nKérlek adj meg egy pozitív számot!\n ")))
    
    if list[len(list)-1] < 0:
        list.pop()
        occoured = harommal_oszthatok(list)
        print(f"Összesen ennyi olyan szám volt ami 3-al volt osztható: {occoured} !\n Megszakítás oka: Negatív számot adtál meg.")
        break
    print(f"Összesen ennyi olyan szám volt ami 3-al volt osztható: {harommal_oszthatok(list)} !")