f, m, b = input().split(" ")
tf, tm, tb = input().split(" ")

s = (int(f) * int(tf)) + (int(m) * int(tm)) + (int(b) * int(tb))
k = int(tf) + int(tm) + int(tb)

print(k, s)