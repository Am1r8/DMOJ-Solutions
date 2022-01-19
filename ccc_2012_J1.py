spl = int(input())
yos = int(input())

if yos <= spl:
    print("Congratulations, you are within the speed limit!")
else:
    if yos >= spl:
        su = yos - spl
        if 0 < su and su  < 21:
            print("You are speeding and your fine is $100.")
        elif 20 < su and su < 31:
            print("You are speeding and your fine is $270.")
        elif 30<su:
            print("You are speeding and your fine is $500.")