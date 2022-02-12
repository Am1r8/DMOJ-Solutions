n = int(input())

adj = [[] for x in range(n+1)]
dp = [0 for x in range(n+1)]
dp[n] = 1

while True:
  dank = list(map(int, input().split())) 
  if dank[0] == 0:
    break
  adj[dank[1]].append(dank[0])

for i in range(n, -1, -1):
  for j in range(len(adj[i])):
    dp[adj[i][j]] += dp[i]
    
print(dp[1])