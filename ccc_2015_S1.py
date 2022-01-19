num = int(input())

numbers = []

for i in range(num):
    k = int(input())
    if k == 0:
        numbers.pop()
    else:
        numbers.append(k)
    
print(sum(numbers))