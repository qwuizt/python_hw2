num = input("Введите число: ")
if num[0] == "-":
    num = num[1:]
sum = 0
numSplit = num.split(".")
numInt = int(numSplit[0])
numFract = int(numSplit[1])
 
while numInt > 0:
    digitInt = numInt % 10
    sum = sum + digitInt
    numInt = numInt // 10
while numFract > 0:
    digitFract = numFract % 10
    sum = sum + digitFract
    numFract = numFract // 10 
 
print("Сумма:", sum)
