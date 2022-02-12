nm = int(input())
high1 = 0
low1 = 0

high2 = 100
low2 = 100

for i in range(nm):
    k = input("").split(",")
    k = [int(item) for item in k]
    if k[0] > high1:
        high1 = k[0]
    if k[1] > low1:
        low1 = k[1]
    if k[0] < high2:
        high2 = k[0]
    if k[1] < low2:
        low2 = k[1]

print(str(high2-1) + "," + str(low2-1))
print(str(high1+1) + "," + str(low1+1))
