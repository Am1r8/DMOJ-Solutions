from datetime import date, timedelta

num = int(input())

age = []

for i in range(num):
    k = input("").split(" ")
    j = date(int(k[0]), int(k[1]), int(k[2]))
    n = date(2007, 2, 27)
    o = n.year - j.year - ((n.month, n.day) < (j.month, j.day))
    age.append(o)
for i in range(len(age)):
    if age[i] >= 18:
        print("Yes")
    elif age[i] < 18:
        print("No")