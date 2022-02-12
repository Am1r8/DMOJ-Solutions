m, am, bm = input().split(" ")
count_a = 0
count_t = 0

for i in range(int(m)):
    k = input().split(" ")
    if k[0] >= am:
        count_a += 2
    if k[1] >= bm:
        count_t += 2
    if k[0] < am:
        count_a += 1
    if k[1] < bm:
        count_t += 1

if count_a > count_t:
    print("Andrew wins!")
elif count_a < count_t:
    print("Tommy wins!")
elif count_a == count_t:
    print("Tie!")