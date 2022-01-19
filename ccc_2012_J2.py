i1 = int(input())
i2 = int(input())
i3 = int(input())
i4 = int(input())

if i1 < i2 < i3 < i4:
    print("Fish Rising")
elif i1 > i2 > i3 > i4:
    print("Fish Diving")
elif i1 == i2 == i3 == i4:
    print("Fish At Constant Depth")
else:
    print("No Fish")