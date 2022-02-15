n = int(input())

triangle = []
for x in range(n):
  triangle.append(list(map(int, input().split())))
  triangle[x].append(0)
  triangle[x].insert(0, 0)
  

for x in range(1, n):
  for y in range(1, len(triangle[x])-1):
    if triangle[x][y] + triangle[x-1][y] > triangle[x][y] + triangle[x-1][y-1]:
      triangle[x][y] += triangle[x-1][y]
    else:
      triangle[x][y] += triangle[x-1][y-1]

result = 0
for x in range(len(triangle[n-1])):
  if triangle[n-1][x] > result:
    result = triangle[n-1][x]
    
print(result)