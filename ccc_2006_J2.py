d1 = int(input())
d2 = int(input())

c = 0

for i in range(1,d1+1):
    for k in range(d2, -1, -1):
        if i == 10 or k == 0:
            continue
        p = i+k
        if p == 10:
            c += 1
        
    
if c > 1:
    print("There are",c,"ways to get the sum 10.")
elif c == 1:
    print("There is 1 way to get the sum 10.")
elif c == 0:
    print("There are 0 ways to get the sum 10.")