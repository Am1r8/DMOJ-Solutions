def isPal(word):
  word = word.lower()
  return word == word[:: -1]
word = input()
pal = []
if len(word) == 1:
  print("1")
for i in range(len(word)):
  for j in range(i + 1, len(word)):
    if isPal(word[i:j+1]) == True:
      pal.append(j-i+1)
        
print(max(pal)) 