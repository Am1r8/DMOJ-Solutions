res = []

for i in range(6):
    res.append(input())
    
    
w = []
l = []

for i in range(6):
    if res[i] == "W":
        w.append(res[i])
    elif res[i] == "L":
        l.append(res[i])


if len(w) == 5 or len(w) == 6:
    print("1")
elif len(w) == 3 or len(w) == 4:
    print("2")
elif len(w) == 1 or len(w) == 2:
    print("3")
else:
    print("-1")
