inp_l = int(input())

studentResponses = []
for i in range (0, inp_l):
    studentResponses.append(input())
    
correctAnswers = []
for i in range (0, inp_l):
    correctAnswers.append(input())

# mark test
score = 0
for i in range (0, inp_l):
    if studentResponses[i] == correctAnswers[i]:
        score = score + 1
print (score)