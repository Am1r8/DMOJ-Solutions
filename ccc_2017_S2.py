import math
n = int(input())
tide = list(map(int, input().split()))

answer = [0] * n
output = ""

tide.sort()
for i in range(0, math.floor(n), 2):
  answer[i] = tide[math.ceil(n/2)-i]

for i in range(1, math.ceil(n), 2):
  answer[i] = tide[math.floor(n/2)+i]
  
for i in answer:
  output += (str(i) + " ")
print(output)