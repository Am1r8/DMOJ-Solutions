n = int(input(""))

vil = []
dis = []

for i in range(n):
    vil_dis = int(input())
    vil.append(vil_dis)
    
vil.sort()

for i in range(1, n-1):
    distance = (vil[i+1] - vil[i]) / 2 + (vil[i] - vil[i-1]) / 2
    dis.append(distance)
    
print(min(dis))