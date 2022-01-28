k = int(input())

#create friends array [1...k]
friends = []
for i in range (k):
    friends.append(i+1)

m = int(input())

for round in range(m):
    r = int(input())

    # eliminate every rth friend
    newfriends = []
    for i in range(len(friends)):
        if (i+1) % r != 0:
            newfriends.append (friends[i])

    # copy the new friends back into the old one
    friends = []
    for f in newfriends:
        friends.append(f)

for f in friends:
    print (f)