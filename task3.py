n = int(input("Введите целое число n: "))
listN = []
sum = 0
for i in range (1, n+1):
    formula = (1 + 1 / i) ** i
    listN.append(round(formula))
    sum += round(formula)
print(listN, "->", sum)