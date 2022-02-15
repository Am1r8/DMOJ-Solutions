cases = int(input())

def move(y, x):
  global interCount
  c = city[y][x]
  if c == "-" or c == "+":
    if x > 0 and city[y][x-1] != "*":
      if interCount[y][x] + 1 < interCount[y][x-1]:
        interCount[y][x-1] = interCount[y][x] + 1
        move(y, x-1)
    if x < width-1 and city[y][x+1] != "*":
      if interCount[y][x] + 1 < interCount[y][x+1]:
        interCount[y][x+1] = interCount[y][x] + 1
        move(y, x+1)
    
  if c == "|" or c == "+":
    if y > 0 and city[y-1][x] != "*":
      if interCount[y][x] + 1 < interCount[y-1][x]:
        interCount[y-1][x] = interCount[y][x] + 1
        move(y-1, x)
    if y < height-1 and city[y+1][x] != "*":
      if interCount[y][x] + 1 < interCount[y+1][x]:
        interCount[y+1][x] = interCount[y][x] + 1
        move(y+1, x)

for case in range(cases):
  height = int(input())
  width = int(input())
  city = []
  for i in range(height):
    city.append(input())
  interCount = [[99999 for i in range(width)] for j in range(height)]
  interCount[0][0] = 1
  move(0, 0)
  if interCount[-1][-1] == 99999:
    print(-1)
  else:
    print(interCount[-1][-1])