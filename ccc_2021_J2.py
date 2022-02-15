num = int(input())
number = 0
per = 0

for i in range(num):
    k = input()
    s = int(input())
    
    if s > number:
        number = s
        per = k

print(per)