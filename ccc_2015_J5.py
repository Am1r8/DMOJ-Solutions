n = int(input())
k = int(input())
piemap = dict()
def pie(pieces, people):
    if pieces < people:
        return 0
    if people == 1 or pieces == people:
        return 1
    if (pieces, people) in piemap:
        return piemap[(pieces, people)]
    piemap[(pieces, people)] = pie(pieces - 1, people - 1) + pie(pieces - people, people)
    return piemap[(pieces, people)]


print(pie(n, k))