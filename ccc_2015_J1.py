month = int(input())
day = int(input())


if month == 2:
    if day > 18:
        print("After")
    elif day < 18:
        print("Before")
    elif day == 18:
        print("Special")
elif month > 2:
    print("After")
elif month < 2:
    print("Before")