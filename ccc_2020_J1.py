S = int(input())
M = int(input())
L = int(input())

st = 1 * S + 2 * M + 3 * L

if st >= 10:
    print('happy')
elif st < 10:
    print('sad')