def osszegzo(list):
    sum = 0
    for i in list:
        sum += i
    return sum

list = [1,2,3,4,5,6,7,8,9,10]
sum = osszegzo(list)
print(sum)