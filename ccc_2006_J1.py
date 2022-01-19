bur = int(input())
side = int(input())
drink = int(input())
des = int(input())

cal = 0

if bur == 1:
    cal += 461
elif bur == 2:
    cal += 431 
elif bur == 3:
    cal += 420
else:
    cal += 0

if side == 1:
    cal += 100
elif side == 2:
    cal += 57
elif side == 3:
    cal += 70
else:
    cal += 0

if drink == 1:
    cal += 130
elif drink == 2:
    cal += 160
elif drink == 3:
    cal += 118
else:
    cal += 0
    
if des == 1:
    cal += 167
elif des == 2:
    cal += 266
elif des == 3:
    cal += 75
else:
    cal += 0
    

print("Your total Calorie count is ",cal, ".", sep="")