num = int(input("Введите количество элементов: "))
indexOne = int(input("Введите индекс одного из множителей: "))
indexTwo = int(input("Введите индекс одного из множителей: "))
listN = []
for i in range (-num, num+1):
    listN.append(i)
mult = listN[indexOne] * listN[indexTwo]
print(listN, 'произведение:', mult)
