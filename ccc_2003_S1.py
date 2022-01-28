k = 1
while True:
    n = int(input())
    if n < 2 or n > 12:
        print("You Quit!")
        quit()
    if k + n <= 100:
        k = k + n
        
        if k == 9:
            k = 34
        if k == 40:
            k = 64
        if k == 67:
            k = 86
        if k == 54:
            k = 19
        if k == 90:
            k = 48
        if k == 99:
            k = 77

    
    print("You are now on square "+ str(k))
    
    if k == 100:
        print("You Win!")
        quit()
        