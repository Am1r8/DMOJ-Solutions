col1 = input().split(" ")
col2 = input().split(" ")
col3 = input().split(" ")
col4 = input().split(" ")

col1, col2, col3, col4 = map(int, col1), map(int, col2), map(int, col3), map(int, col4)

    
if sum(col1) == sum(col2) == sum(col3) == sum(col4):
    print("magic")
else:
    print("not magic")