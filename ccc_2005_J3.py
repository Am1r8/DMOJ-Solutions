t = True

way = []
ste = []

while t:
    way.append(input(""))
    s = input("")
    if s == "SCHOOL":
        t = False
    else:
        ste.append(s)



way.reverse()
ste.reverse()
for i in range(len(way)-1):
    if way[i] == "R":
        print(f"Turn LEFT onto {ste[i]} street.")
    elif way[i] == "L":
        print(f"Turn RIGHT onto {ste[i]} street.")

if way[-1] == "R":
    print("Turn LEFT into your HOME.")
elif way[-1] == "L":
    print("Turn RIGHT into your HOME.")