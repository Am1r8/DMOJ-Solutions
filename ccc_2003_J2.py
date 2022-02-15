from math import *
n = 1
le = []
wi = []
pe = []
while n > 0:
    n = int(input())
    if n == 0:
        break
    l = sqrt(n)
    w = n / int(l)
    le.append(int(l))
    wi.append(int(w))
    pe.append(int(l) * 2 + int(w) * 2)


for i in range(len(pe)):
    print("Minimum perimeter is", pe[i], "with dimensions", le[i], "x", wi[i])