num = int(input())
count = 0
t = True

if num == 1:
    print(count+1)
    t = false
while t:
    count += 1
    if num % 2 == 0:
        num = num / 2
    else:
        num = (num * 3) + 1
    
    if num <= 1:
        t = False

print(count)