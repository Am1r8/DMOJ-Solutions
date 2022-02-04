t = True
li = ["A", "B", "C", "D", "E"]

while t:
    b = int(input())
    n = int(input())
    
    if b  == 1:
        for i in range(n):
            li.append(li.pop(li.index(li[0])))
    if b == 2:
        for i in range(n):
            li = li[-1:] + li[:-1]
    if b == 3:
        for i in range(n):
            li[0], li[1] = li[1], li[0]
    if b == 4 and n == 1:
        print(" ".join(li))
        t = False