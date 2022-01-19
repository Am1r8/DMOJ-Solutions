nums = int(input())

a = []
d = []

for i in range(nums):
    inp = input().split(" ")
    a.append(int(inp[0]))
    d.append(int(inp[1]))
    

point_a = 100
point_d = 100    

for i in range(nums):
    if a[i] == d[i]:
        point_a -= 0
    elif a[i] > d[i]:
        point_d -= a[i]
    elif a[i] < d[i]:
        point_a -= d[i]

print(point_a)
print(point_d)