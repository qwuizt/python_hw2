from random import randrange

listN = [0,1,2,3,4,5,6,7,8,9,10]
print(listN)
i = len(listN)
while i > 1:
        i = i - 1
        j = randrange(i)  
        listN[j], listN[i] = listN[i], listN[j]
print(listN)
