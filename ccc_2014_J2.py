num = int(input())
vote = list(input())

a = []
b = []

for i in range(num):
    if vote[i] == "A":
        a.append(vote[i])
    elif vote[i] == "B":
        b.append(vote[i])
        
if len(a) > len(b):
    print("A")
elif len(a) < len(b):
    print("B")
else:
    print("Tie")