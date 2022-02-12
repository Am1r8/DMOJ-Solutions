cr = input("").split(" ")
cr = [int(item) for item in cr]

ax = 0
ay = 0
while True:
    rxry = input("").split(" ")
    rxry = [int(item) for item in rxry]
    if rxry[0] == 0 and rxry[1] == 0:
        break
    else:
        ax = int(ax) + rxry[0]
        ay = int(ay) + rxry[1]
    if int(ax) < 0:
        ax = 0
    elif int(ax) > cr[0]:
        ax = cr[0]
    if int(ay) < 0:
        ay = 0
    elif int(ay) > cr[1]:
        ay = cr[1]

    print(ax, ay)