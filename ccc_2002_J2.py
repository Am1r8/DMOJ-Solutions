qui = True

word = []

while qui:
    k = input("")
    if k == "quit!":
        qui = False
    
    word.append(k)

word.pop(-1)


for i in range(len(word)):
    if len(word[i]) < 4:
        print(word[i])
    else:
        if "e" in word[i] or "i"  in word[i] or "o"  in word[i] or "u" in word[i] or "y" in word[i]:
            if "or" in word[i][-2:]:
                if "oo" in word[i][-2:] or "p" in word[i]:
                    print(word[i])
        else:
            print(word[i].replace("or", "our"))
        
