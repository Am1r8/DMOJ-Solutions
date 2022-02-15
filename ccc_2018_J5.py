N = int(input())
book = []
book.append([])
visited = []
visited.append(1)
minPath = N+1
dist = [minPath]

for i in range(N):
    pp = input().split()
    if int(pp[0]) == 0:
        visited.append(0)
        book.append([0])
        dist.append(minPath)
        continue
    curlist = []
    for j in range(1, len(pp), 1):
        curlist.append(int(pp[j]))
    book.append(curlist)
    visited.append(0)
    dist.append(minPath)

stacklist = [1]
visited[1] = 1
dist[1] = 1

while len(stacklist) > 0:
    n = stacklist.pop()
    p = dist[n]
    for x in book[n]:
        if x == 0:
            if minPath > p:
                minPath = p
        else:
            if p+1 < dist[x]:
                dist[x] = p+1
                visited[x] = 0
            if visited[x] == 0:
                stacklist.append(x)
                visited[x] = 1

allvisited = True
for x in visited:
    if x == 0:
        allvisited = False
        break

if allvisited:
    print("Y")
else:
    print("N")
print(minPath)