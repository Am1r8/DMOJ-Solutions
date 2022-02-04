t1 = int(input())
t2 = int(input())

num = []
num.append(t1)
num.append(t2)


while t1 >= 0 and t2 >= 0 and t1 >= t2:
    k = t2
    t2 = t1 - t2
    t1 = k
    num.append(t2)

print(len(num))