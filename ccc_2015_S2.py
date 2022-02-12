J = int(input())
A = int(input())

count1 = 0
sizes = []

while count1 < J:
  sizes.append(input())
  count1 = count1 + 1
  
count2 = 0
requests = []

while count2 < A:
  requests.append(input().split(" "))
  count2 = count2 + 1
  
jersey_inventory = []
number = J
while (J >= number and number > 0):
  jersey_inventory.append(sizes[J - number])
  number = number - 1

print(jersey_inventory)



final_tally = 0

for request in requests:
  for jersey in jersey_inventory:
    if (request[0] == "L" and jersey[1] == "L") and (request[1] == jersey[0]):
      final_tally = final_tally + 1
      jersey_inventory.remove(jersey)
    elif (request[0] == "M" and (jersey[1] == "L" or jersey[1] == "M")) and (request[1] == jersey[0]):
      final_tally = final_tally + 1
      jersey_inventory.remove(jersey)
    elif (request[0] == "S" and (jersey[1] == "L" or jersey[1] == "M" or jersey[1] == "S")) and (request[1] == jersey[0]):
      final_tally = final_tally + 1
      jersey_inventory.remove(jersey)

print(final_tally)
