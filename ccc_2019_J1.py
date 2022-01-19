num = []

for i in range(6):
    num.append(int(input()))
    

num[0] *= 3
num[1] *= 2
num[2] *= 1

a = num[0] + num[1] + num[2]

num[3] *= 3
num[4] *= 2
num[5] *= 1
b = num[3] + num[4] + num[5]

if a > b:
    print("A")
elif a < b:
    print("B")
elif a == b:
    print("T")