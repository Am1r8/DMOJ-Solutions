first = int(input())
last = int(input())

for i in range(first,last):
    if (i - first)  % 60 == 0:
        print ("All positions change in year " + str(i))