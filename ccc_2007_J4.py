word1 = input()
word2 = input()



w1l = sorted([c for c in word1])
w2l = sorted([c for c in word2])
if w1l == w2l:
    print("Is an anagram.")
else:
    print("Is not an anagram.")