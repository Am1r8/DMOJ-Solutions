num = []

for i in range(3):
    num.append(int(input()))

li = "9780921418"
li = list(li)

mer = li + num

mul = []

nol = 1

for i in range(len(mer)):
    if nol == 1:
        mul.append(int(mer[i]) * nol)
        nol = 3
    elif nol == 3:
        mul.append(int(mer[i]) * nol)
        nol = 1

print("The 1-3-sum is", sum(mul))