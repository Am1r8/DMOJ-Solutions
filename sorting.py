num = int(input())

k = []

for i in range(num):
    k.append(int(input()))

s = sorted(k)

for i in range(num):
    print(s[i])