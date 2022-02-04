N = int(input())
name1 = input().split()
name2 = input().split()

pairtable = dict()


for i in range(N):
    pairtable[name1[i]] = name2[i]

result = True

for x in pairtable:
    if x == pairtable[x]:
        result = False
        break
    y = pairtable[x]
    z = pairtable[y]
    if z != x:
        result = False
        break
if result:
    print("good")
else:
    print("bad")
    
print(pairtable)