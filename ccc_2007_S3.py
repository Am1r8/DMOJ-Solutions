n = int(input())
students = []
friends = []

for i in range(n):
  s,f = input().split()
  students.append(s)
  friends.append(f)

while True:
  s,f = input().split()
  count = 0
  found = False
  if s == '0' and f == '0':
    break
  else:
    for i in range(n):
      if friends[students.index(s)] != f:
        s = friends[students.index(s)]
        count += 1
      else:
        print("Yes",count)
        found = True
        break
  if found == False:
    print("No")