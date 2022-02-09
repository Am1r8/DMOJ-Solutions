h = int(input())
m = int(input())
a = 0
touch = 0
for i in range(m + 1):
  a = (-6*(i**4)) + (h*(i**3)) + (2*(i**2)) + i
  if a > 0:
    touch = i
if a <= 0 and touch != 0:
  print("The balloon first touches ground at hour:\n" + str(touch + 1))
elif a > 0:
  print("The balloon does not touch ground in the given time.")