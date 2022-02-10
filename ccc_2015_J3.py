consonant =     "bcdfghjklmnpqrstvwxyz"
closestVowel =  "aaeeeiiiiooooouuuuuuu"
nextConsonant = "cdfghjklmnpqrstvwxyzz"

word = input()
newword = ""
for x in word:
    j = consonant.find(x)
    newword += x
    if j > -1:
        newword = newword + closestVowel[j] + nextConsonant[j]
print(newword)