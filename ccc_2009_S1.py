a = int(input())
b = int(input())
count = 0
for n in range(1,22):
    i = n**6
    if (i >= a) and (i <= b):
        count+=1
print(count)