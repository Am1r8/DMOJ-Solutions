x = int(input())
a = int(input())
b = int(input())
c = int(input())

qui = True
count = 0

while x > 0 and qui:
    if x <= 0:
        qui = False
    x -= 1
    count += 1
    a += 1
    if x <= 0:
        qui = False
    if a == 35:
        a = 0
        x += 30
    
    if x <= 0:
        qui = False
    x -= 1
    count += 1
    b += 1
    if b == 100:
        b = 0
        x += 60
    
    if x <= 0:
        qui = False
    x -= 1
    count += 1
    c += 1
    if c == 10:
        c = 0
        x += 9
    
    if x <= 0:
        qui = False

print("Martha plays {} times before going broke.".format(count))
        
    