day = int(input())
eve = int(input())
wee = int(input())

day_a = day - 100
day_a = day_a * 0.25
eve_a = eve * 0.15
wee_a = wee * 0.2

day_b = day - 250
day_b = day_b * 0.45
eve_b = eve * 0.35
wee_b = wee * 0.25

a = day_a + eve_a + wee_a
b = day_b + eve_b + wee_b

print("Plan A costs", a)
print("Plan B costs", b)

if a > b:
    print("Plan B is cheapest.")
elif a < b:
    print("Plan A is cheapest.")
elif a == b:
    print("Plan A is cheapest.")
    print("Plan B is cheapest.")