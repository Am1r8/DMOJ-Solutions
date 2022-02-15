root = [0 for i in range(100001)]

#find the set this index belongs to
def find(x): 
    if x!=root[x]:
        root[x] = find(root[x])
    return root[x]

#merge index x into y
def merge(x,y): 
    root[find(x)] = find(y)

 
numGates = int(input())
numPlanes = int(input())
for i in range(1,numGates+1):
    root[i] = i
i = 0
keepgoing = True
while i < numPlanes and keepgoing:
    gateWanted = int(input())
    gateWantedRoot = find(gateWanted)
    if gateWantedRoot == 0:
        print(i)
        keepgoing = False 
    merge(gateWantedRoot,gateWantedRoot-1)
    i = i + 1
if keepgoing:    
    print(numPlanes)