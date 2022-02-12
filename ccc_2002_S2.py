numerator = int(input())
denominator = int(input())
out = ""

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

factor = gcd(numerator, denominator)
numerator //= factor
denominator //= factor

if numerator < denominator:
    out += str(numerator) + "/" + str(denominator)
else:
    quotient = numerator // denominator
    rem = numerator % denominator
    out += str(quotient)
    if rem != 0:
        out += " " + str(rem) + "/" + str(denominator)

print(out)