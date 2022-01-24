num = int(input())

k = []

for i in range(num):
    k.append(int(input()))

k.sort(reverse=True)

for i in range(len(k)):
    print(k.pop())