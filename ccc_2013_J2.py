inp = list(input())

words = ["H", "I", "N", "O", "S", "X", "Z"]
count = 0

for i in range(len(inp)):
    if inp[i] in words:
        count += 1
    else:
        count -= 1
        
if count == 0:
    print("NO")
elif count == len(inp):
    print("YES")
else:
    print("NO")