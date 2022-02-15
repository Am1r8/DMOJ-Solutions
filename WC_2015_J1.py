num = int(input())

if num < 1:
    print("k")
    print("A long time ago in a galaxy", "far" * num, "away...", end="")
else:
    if num > 1:com = ","
    else: com = ""
    print("A long time ago in a galaxy", ("far" + com + " ") * (num - 1), "far", "away...", end=" ")