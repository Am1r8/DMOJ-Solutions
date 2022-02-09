num = int(input())

numbers_in = []
h = []
numbers_co = []

for i in range(num):
    numbers_in.append(list(input()))

for i in range(len(numbers_in)):
    for k in range(len(numbers_in[i])):
        h.append(numbers_in[i][k])

for i in range(0, len(h)):
    # if i == 4 or i == 8:
    #     numbers_co.append('-')
    if h[i] == '1':
        numbers_co.append('1')
    elif h[i] == 'A' or h[i] == 'B' or h[i] == 'C' or h[i] == '2':
        numbers_co.append('2')
    elif h[i] == 'D' or h[i] == 'E' or h[i] == 'F' or h[i] == '3':
        numbers_co.append('3')
    elif h[i] == 'G' or h[i] == 'H' or h[i] == 'I' or h[i] == '4':
        numbers_co.append('4')
    elif h[i] == 'J' or h[i] == 'K' or h[i] == 'L' or h[i] == '5':
        numbers_co.append('5')
    elif h[i] == 'M' or h[i] == 'N' or h[i] == 'O' or h[i] == '6':
        numbers_co.append('6')
    elif h[i] == 'P' or h[i] == 'Q' or h[i] == 'R' or h[i] == 'S' or h[i] == '7':
        numbers_co.append('7')
    elif h[i] == 'T' or h[i] == 'U' or h[i] == 'V' or h[i] == '8':
        numbers_co.append('8')
    elif h[i] == 'W' or h[i] == 'X' or h[i] == 'Y' or h[i] == 'Z' or h[i] == '9':
        numbers_co.append('9')
    elif h[i] == '0':
        numbers_co.append('0')        

for i in range(len(numbers_co)):
    if i % 10 == 0:
        l = "".join(numbers_co[i:i+10])
        print(l)

print(numbers_co)
print(len(numbers_co))

# the dmoj link https://dmoj.ca/problem/ccc05s1