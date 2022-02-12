num = int(input())
li = []

for i in range(num):
    li.append(int(input()))

li.sort()
for i in range(num):
    print(li[i])