adj = int(input())
noun = int(input())

adjs = []
ns = []

for i in range(adj):
    adjs.append(input())

for i in range(noun):
    ns.append(input())

for i in range(adj):
    for k in range(noun):
        print(adjs[i] + " as " + ns[k])