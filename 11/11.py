stones = []

file_name = "input.txt"

with open(file_name, 'r') as file:
    for line in file:
        stones = line.split(" ")


def silver():
    global stones
    for _ in range(0, 25):
        newList = []
        for i in range(len(stones)):
            if stones[i] == "0":
                newList.append("1")
            elif len(stones[i]) % 2 == 0:
                ele = stones[i]
                mid = len(stones[i]) // 2
                firstHalf = ele[:mid]
                secondHalf = ele[mid:]
                secondHalf = secondHalf.lstrip("0") or "0"
                newList.append(firstHalf)
                newList.append(secondHalf)
            elif len(stones[i]) % 2 == 1:
                newList.append(str(int(stones[i]) * 2024))
        stones = newList
    print(len(newList))


def gold():
    for i in range(0, 10):
        print(i)
        print(stones)
        newList = []
        for i in range(len(stones)):
            if stones[i] == "0":
                newList.append("1")
            elif len(stones[i]) % 2 == 0:
                ele = stones[i]
                mid = len(stones[i]) // 2
                firstHalf = ele[:mid]
                secondHalf = ele[mid:]
                secondHalf = secondHalf.lstrip("0") or "0"
                newList.append(firstHalf)
                newList.append(secondHalf)
            elif len(stones[i]) % 2 == 1:
                newList.append(str(int(stones[i]) * 2024))
        stones = newList
    print(len(stones))


#silver()
gold()
