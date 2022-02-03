stri = input("").split(" ")

false = 0
true = 0

for i in range(len(stri)):
    if stri[i] == "not" or stri[i] == "False":
        false += 1
    elif stri[i] == "True":
        true += 1

if false % 2 == 0:
    false = 0
    true += 1
elif true % 2 == 0:
    true = true
elif false % 2 != 0:
    false = false
    true = 0


if true > false:
    print("True")
elif true < false:
    print("False")
else:
    print("")