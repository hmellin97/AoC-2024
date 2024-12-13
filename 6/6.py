listx = []

file_name = "input.txt"

with open(file_name, 'r') as file:
    for line in file:
        listx.append(list(line.strip()))


def silver():
    map_width = len(listx[0])
    map_height = len(listx)
    guard_column = 0
    guard_row = 0
    for column in range(len(listx)):
        for row in range(len(listx[column])):
            if listx[column][row] == "^":
                print(f"found guard at {column}, {row}")
                guard_row = row
                guard_column = column
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # North, East, South, West
    turnCount = 1
    visited = 0
    while True:
        directionToGo = directions[(turnCount % 4) - 1]
        newX = guard_column + directionToGo[0]
        newY = guard_row + directionToGo[1]
        if newX < 0 or newX > map_height-1:
            break  # OOB
        if newY < 0 or newY > map_width-1:
            break # OOB
        tryNextSquare = listx[newX][newY]
        while tryNextSquare == "#":
            turnCount += 1
            directionToGo = directions[(turnCount % 4) - 1]
            tryNextSquare = listx[guard_column + directionToGo[0]][guard_row + directionToGo[1]]
        if listx[guard_column + directionToGo[0]][guard_row + directionToGo[1]] == "." or \
                listx[guard_column + directionToGo[0]][guard_row + directionToGo[1]] == "^":
            listx[guard_column + directionToGo[0]][guard_row + directionToGo[1]] = "X"
            visited += 1
        guard_column += directionToGo[0]
        guard_row += directionToGo[1]
    include_guard_initial_position = 1
    print(visited+include_guard_initial_position)
    #for l in listx:
    #    for ll in l:
    #        print(ll, end="")
    #    print("")


def gold():
    pass


silver()
gold()
