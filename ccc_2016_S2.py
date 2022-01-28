cmd = int(input())
N = int(input())
list1 = []
list2 = []

S1 = input().rstrip().split(" ")
S2 = input().rstrip().split(" ")

for i in range(N):
    list1.append(int(S1[i]))
    list2.append(int(S2[i]))

list1.sort()
list2.sort()
sum = 0
if cmd == 1:
    for i in range(N):
        sum += max(list1[i], list2[i])
else:
    for i in range(N):
        sum += max(list1[i], list2[N-i-1])
print(sum)