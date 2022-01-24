num = int(input())

yes = list(input())
tod = list(input())
    
count = 0    

for i in range(num):
    if yes[i] == tod[i] and yes[i] != ".":
        count += 1
    else:
        continue

print(count)