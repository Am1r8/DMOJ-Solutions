rows = int(input())
cols = int(input())
num_lines = int(input())

row_swipes = [False] * (rows + 1)
col_swipes = [False] * (cols + 1)

for i in range(num_lines):
    line_info = input().split(" ")
    index = int(line_info[1])
    if line_info[0] == "R":
        row_swipes[index] = not row_swipes[index]
    else:
        col_swipes[index] = not col_swipes[index]

canvas = [[False for j in range(cols + 1)] for i in range(rows + 1)]

for i in range(1, rows + 1):
    if row_swipes[i]:
        for j in range(1, cols + 1):
            canvas[i][j] = not canvas[i][j]

for i in range(1, cols + 1):
    if col_swipes[i]:
        for j in range(1, rows + 1):
            canvas[j][i] = not canvas[j][i]

gold_count = 0
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if canvas[i][j]:
            gold_count += 1

print(gold_count)