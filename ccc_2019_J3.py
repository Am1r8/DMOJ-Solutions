new_encounter = -1
sequences = []
num_lines = int(input())

for i in range(num_lines):
    sequences.append(input())

for i in range(num_lines):
    for j in range(len(sequences[i])):
        if j < (len(sequences[i]) - 1):
            if sequences[i][j] != sequences[i][j+1]:
                print(j - new_encounter, sequences[i][j], end=" ")
                new_encounter = j
        else:
            print(j - new_encounter, sequences[i][j])
    new_encounter = -1