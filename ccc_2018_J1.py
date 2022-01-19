num = []

for i in range(4):
    num.append(int(input()))

count = 0

if num[0] == 8 or num[0] == 9:
    count += 1
else:
    count -= 1
if num[1] == num[2]:
    count += 1
else:
    count -= 1
if num[3] == 8 or num[3] == 9:
    count += 1
else:
    count -= 1


if count > 1:
    print("ignore")
if count <= 1:
    print("answer")