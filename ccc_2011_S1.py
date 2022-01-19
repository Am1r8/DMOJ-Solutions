num_l = int(input())

stri = []

for i in range(num_l):
    stri.append(input())

stri = " ".join(stri)

t_T = stri.count("t") + stri.count("T")
s_S = stri.count("s") + stri.count("S")

if t_T > s_S:
    print("English")
elif t_T < s_S:
    print("French")
elif t_T == s_S:
    print("French")