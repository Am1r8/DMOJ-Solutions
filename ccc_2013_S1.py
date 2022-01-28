def distinct(y):
    s = str(y)
    for digit in s:
        if s.count(digit) > 1:
            return False
    return True

file = input()
year = int(file) + 1
while not distinct(year):
    year = year + 1
print(year)