n = int(input())
swifts = input()
sem = input() 

swifts = swifts.split()
sem = sem.split() 

sumSwifts = 0 
sumSem =  0 
instWhenEqual = [0]

for x in range (n):
  sumSwifts += int(swifts[x])
  sumSem += int(sem[x])
  if sumSwifts == sumSem:
    instWhenEqual.append(x + 1)
    
print(max(instWhenEqual))