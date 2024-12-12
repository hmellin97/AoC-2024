list1 = []
list2 = []

file_name = "input.txt"

with open(file_name, 'r') as file:
    for line in file:
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))

def silver():
    distance = 0
    lengths1 = (getLengths(list1))
    lengths2 = (getLengths(list2))
    for i in range(len(lengths1)):
        distance += abs(lengths1[i] - lengths2[i])
    return distance


def getLengths(list):
    d = {}
    for i, l in enumerate(list):
        d[i] = l
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
    lengths = []
    for s in sorted_d:
        lengths.append(sorted_d[s])
    return lengths


def gold():
    freqs = {}
    for l in list2:
        if l not in freqs:
            freqs[l] = 1
        else:
            freqs[l] += 1
    similarity_score = 0
    for l in list1:
        if l in freqs:
            similarity_score += l * freqs[l]
    return similarity_score


print(silver())
print(gold())
