def handling(key, value):
    
    try:
        number = float(value)
        if number.is_integer():
            thisdict[key] = int(number)
        else:
            thisdict[key] = number
        print(thisdict)
        return
    except:
        pass


    lower = value.lower()
    if lower in ("true", "igen"):
        thisdict[key] = True
    elif lower in ("false", "nem"):
        thisdict[key] = False
    else:
        thisdict[key] = value



thisdict = {
    "Int": 10,
    "String": "Idk",
    "Bool": True,
}


while thisdict["Bool"]:
    print(f"Eddig így néz ki a dict: {thisdict}")
    key = str(input("Kérlek adj meg egy úgyn. hívót "))
    value = str(input("Kérlek adj meg egy értéket neki! "))
    handling(key,value)
    if str(input("Szeretnél még adni hozzá? i/n ")) == "n":
        thisdict["Bool"] = False