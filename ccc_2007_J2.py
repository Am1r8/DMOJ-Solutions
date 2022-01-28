qui = True

words = []

while qui:
    k = input("")
    if k == "TTYL":
        qui = False
    
    words.append(k)
    
for i in range(len(words)):
    if words[i] == "CU":
        print("see you")
    elif words[i] == ":-)":
        print("I'm happy")
    elif words[i] == ":-(":
        print("I'm unhappy")
    elif words[i] == ";-)":
        print("wink")
    elif words[i] == ":-P":
        print("stick out my tongue")
    elif words[i] == "(~.~)":
        print("sleepy")
    elif words[i] == "TA":
        print("totally awesome")
    elif words[i] == "CCC":
        print("Canadian Computing Competition")
    elif words[i] == "CUZ":
        print("because")
    elif words[i] == "TY":
        print("thank-you")
    elif words[i] == "YW":
        print("you're welcome")
    elif words[i] == "TTYL":
        print("talk to you later")
    else:
        print(words[i])