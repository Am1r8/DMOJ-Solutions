class Comp:
  def __init__(self, name, val):
    self.name = name
    self.val = val
compList = []

def compSort(c):
  return c.val


n = int(input())
for i in range(n):
  inS = input()
  inSL = inS.split()
  name = str(inSL[0])
  r = int(inSL[1])
  s = int(inSL[2])
  d = int(inSL[3])
  val = 2*r + 3*s + d
  c = Comp(name, val)
  compList.append(c)

compList.sort(key = compSort, reverse = True)
for i in range(min(len(compList), 3)):
  nextC = i+1;
  if nextC < len(compList):
    if compList[i] == compList[nextC]:
      if i.name.lower() > nextC.name.lower():
        temp = compList[i]
        compList[i] = compList[nextC]
        compList[nextC] = temp


for i in range(min(len(compList), 2)):
  print(compList[i].name)