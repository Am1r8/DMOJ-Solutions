N = input().split()

#first output line 
dist = [0]
sd = 0
for i in range(1, 5):
    sd += int(N[i-1])
    dist.append(sd)
print(*dist)

j = 1
while j < 5:
    current = dist[j]
    for i in range(5):
        if i < j:
            dist[i] += current
        else:
            dist[i] -= current
    print(*dist)
    j += 1