num =int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
t = 0

for i in range(num):
    t += ((l1[i] + l1[i + 1]) * l2[i]) / 2

print(t)