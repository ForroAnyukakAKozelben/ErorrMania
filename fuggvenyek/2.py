def paros_e(list):
    for i in list:
        if i % 2 == 0:
            return True

list = [1,2,3,4,5,6,7,8,9,10]
paros_e = paros_e(list)
print(paros_e)