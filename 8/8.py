import operator

dct = {}

file_name = "input.txt"
map_height = 0
map_width = 0
with open(file_name, 'r') as file:
    for x, line in enumerate(file):
        map_height += 1
        line = line.replace("\n", "")
        for y, l in enumerate(line):
            map_width += 1
            if l != ".":
                if l not in dct:
                    dct[l] = [[x, y]]
                else:
                    dct[l].append([x, y])
    map_width //= map_height
    print("baba")


def silver():
    antinodes = []
    for d in dct:
        coords = dct[d]
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                startX = coords[i][0]
                startY = coords[i][1]
                endX = coords[j][0]
                endY = coords[j][1]
                diffX = abs(startX - endX)
                diffY = abs(startY - endY)

                def find_antinode(x, y, dx, dy, op1, op2):
                    echoX = op1(x, dx)
                    echoY = op2(y, dy)
                    if 0 <= echoX < map_height and 0 <= echoY < map_width:
                        if [echoX, echoY] not in antinodes:
                            antinodes.append([echoX, echoY])

                ops = []
                if startY >= endY:
                    ops = [[operator.sub, operator.add], [operator.add, operator.sub]]
                elif startY <= endY:
                    ops = [[operator.sub, operator.sub], [operator.add, operator.add]]
                find_antinode(startX, startY, diffX, diffY, ops[0][0], ops[0][1])
                find_antinode(endX, endY, diffX, diffY, ops[1][0], ops[1][1])
    print(len(antinodes))


def gold():
    antinodes = []
    for d in dct:
        coords = dct[d]
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                startX = coords[i][0]
                startY = coords[i][1]
                endX = coords[j][0]
                endY = coords[j][1]
                diffX = abs(startX - endX)
                diffY = abs(startY - endY)

                def find_antinode(x, y, dx, dy, op1, op2):
                    echoX = op1(x, dx)
                    echoY = op2(y, dy)
                    if 0 <= echoX < map_height and 0 <= echoY < map_width:
                        if [echoX, echoY] not in antinodes:
                            antinodes.append([echoX, echoY])
                        return True
                    return False

                ops = []
                if startY >= endY:
                    ops = [[operator.sub, operator.add], [operator.add, operator.sub]]
                elif startY <= endY:
                    ops = [[operator.sub, operator.sub], [operator.add, operator.add]]
                cnt = 0 # include diff=0
                while True:
                    if not find_antinode(startX, startY, diffX * cnt, diffY * cnt, ops[0][0], ops[0][1]):
                        break
                    cnt += 1
                cnt = 0
                while True:
                    if not find_antinode(endX, endY, diffX * cnt, diffY * cnt, ops[1][0], ops[1][1]):
                        break
                    cnt += 1
                print("gooda")
    print(len(antinodes))
    x = 1
    for i in range(12):
        for j in range(12):
            if [i,j] in antinodes:
                print("X", end="")
                x+=1
            else:
                print(".", end="")
        print("")


silver()
gold()
