qui = True

city = []
temp = []

while qui:
    ci = input()
    if "Waterloo" in ci:
        city.append(ci.split(" "))
        qui = False
    else:
        city.append(ci.split(" "))

for i in range(len(city)):
    for k in range(1):
        city[i][1] = int(city[i][1])
        temp.append(city[i][1])


mv = min(temp)
f = temp.index(mv)
print(city[f][0])