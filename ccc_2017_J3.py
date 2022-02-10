x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
t = int(input())
dist = abs(x1 - x2) + abs(y1 - y2)
if dist <= t and (t - dist) % 2 == 0:
    print('Y')
else:
    print('N')