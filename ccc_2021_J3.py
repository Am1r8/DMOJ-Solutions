t = True
w = []
while t:
    num = input()
    if num == "99999":
        t = False
    else:
        num = list(num)
        num = [int(i) for i in num]
        if sum(num[:2]) % 2 != 0:
            num = [str(i) for i in num]
            k = "".join(num[2:])
            print("left", k)
            w.append("left")
        elif sum(num[:2]) % 2 == 0 and sum(num[:2]) != 0:
            num = [str(i) for i in num]
            k = "".join(num[2:])
            print("right", k)
            w.append("right")
        elif sum(num[:2]) == 0:
            num = [str(i) for i in num]
            k = "".join(num[2:])
            print(w[-1], k)