rules = {}
file_name = "input.txt"
updates = []
with open(file_name, 'r') as file:
    for line in file:
        if "|" in line:
            numbers = line.split("|")
            a = numbers[0]
            b = numbers[1].strip()
            if a not in rules:
                rules[a] = [b]
            else:
                rules[a].append(b)
        elif "," in line:
            line = line.strip()
            numbers = line.split(",")
            updates.append(numbers)
    print("cool")

def silver():
    sum = 0
    for u in updates:
        rightOrder = True
        for i, uu in enumerate(u):
            before = u[:i]
            rest = u[i+1:]
            pointsTo = []
            if uu not in rules:
                continue
            else:
                pointsTo = rules[uu]
            for b in before:
                if b in pointsTo:
                    rightOrder = False
            for r in rest:
                if r not in pointsTo:
                    rightOrder = False
        if rightOrder:
            v = int(u[len(u)//2])
            sum += v
            print(f"adding {v}")
    print(sum)


def gold():
    pass

silver()
gold()