list = []

file_name = "input.txt"
map_height = 0
map_width = 0
with open(file_name, 'r') as file:
    for line in file:
        map_height+=1
        list.append(line)
        map_width = len(line)

def silver():
    routes = 0
    def backtrack(x, y, number, found_nines):
        nonlocal routes
        directions = [
            {"dir": "South", "coord":[1, 0]},   # South
            {"dir": "North", "coord":[-1, 0]},  # North
            {"dir": "East", "coord":[0, 1]},    # East
            {"dir": "West", "coord":[0, -1]},   # West
        ]
        for d in directions:
            newX = x + d["coord"][0]
            newY = y + d["coord"][1]
            #print(f"Going {d["dir"]}")
            if 0 <= newX < map_height and 0 <= newY < map_width:
                targetNum = str(int(number) + 1)
                if list[newX][newY] == targetNum:
                    #print(f"Found {targetNum} at [{newX},{newY}]")
                    if targetNum == "9" and [newX, newY] not in found_nines:
                        #print(f"Found 9 at [{newX},{newY}]")
                        found_nines.append([newX,newY])
                        routes+=1
                    else:
                        backtrack(newX, newY, targetNum, found_nines)
                else:
                    pass
                    #print("Invalid next number")
            else:
                pass
                #print("Out of bounds")

    for i, l in enumerate(list):
        for j, ele in enumerate(l):
            if ele == "0":
                #print(f"found at {i} {j}")
                found_nines = []
                backtrack(i, j, 0, found_nines)
                #print(routes)
    print(routes)



def gold():
    routes = 0
    def backtrack(x, y, number):
        nonlocal routes
        directions = [
            {"dir": "South", "coord":[1, 0]},   # South
            {"dir": "North", "coord":[-1, 0]},  # North
            {"dir": "East", "coord":[0, 1]},    # East
            {"dir": "West", "coord":[0, -1]},   # West
        ]
        for d in directions:
            newX = x + d["coord"][0]
            newY = y + d["coord"][1]
            #print(f"Going {d["dir"]}")
            if 0 <= newX < map_height and 0 <= newY < map_width:
                targetNum = str(int(number) + 1)
                if list[newX][newY] == targetNum:
                    #print(f"Found {targetNum} at [{newX},{newY}]")
                    if targetNum == "9":
                        #print(f"Found 9 at [{newX},{newY}]")
                        found_nines.append([newX,newY])
                        routes+=1
                    else:
                        backtrack(newX, newY, targetNum)
                else:
                    pass
                    #print("Invalid next number")
            else:
                pass
                #print("Out of bounds")

    routes = 0
    for i, l in enumerate(list):
        for j, ele in enumerate(l):
            if ele == "0":
                #print(f"found at {i} {j}")
                found_nines = []
                backtrack(i, j, 0)
                #print(routes)
    print(routes)


silver()
gold()
