num = int(input())

while True:
    for i in range(2, num):
        if (num % i) == 0:
            num += 1
        else:
            print(num)
            exit()