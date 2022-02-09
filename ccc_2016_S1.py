def ragaman(a, b):
  a = list(a)
  b = list(b)
  for i in reversed(range(len(a))):
    for j in reversed(range(len(b))):
      if a[i] == b[j]:
        a.pop(i)
        b.pop(j)
        break

  for i in reversed(range(len(b))):
    if b[i] == '*':
      b.pop(i)
      a.pop()

  print('A') if len(a) == 0 and len(b) == 0 else print('N')

ragaman(input(), input())