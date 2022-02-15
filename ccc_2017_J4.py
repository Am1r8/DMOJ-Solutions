day_c = 31
h_c = 720

d = int(input())
h = 12
m = 0
cnt = 0
for i in range(d % h_c):
    m += 1
    if m == 60:
        h += 1
        m = 0
    if h == 13:
        h = 1
    clock = str(h) + '%02d' % m
    dif = int(clock[1]) - int(clock[0])
    for j in range(1, len(clock)):
        if int(clock[j]) - int(clock[j - 1]) != dif:
            break
    else:
        cnt += 1
print(cnt + day_c * (d // h_c))