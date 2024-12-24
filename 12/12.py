list = []

file_name = "input.txt"
map_height = 0
map_width = 0
with open(file_name, 'r') as file:
    for line in file:
        map_height += 1
        list.append(line.strip())
        map_width = len(line)


class CropPatch:
    def __init__(self, category, width, height, coords, fences):
        self.category = category
        self.width = width
        self.height = height
        self.coords = coords
        self.fences = fences


def silver():
    def backtrack(x, y, crop):
        directions = [
            {"dir": "South", "coord": [1, 0]},  # South
            {"dir": "North", "coord": [-1, 0]},  # North
            {"dir": "East", "coord": [0, 1]},  # East
            {"dir": "West", "coord": [0, -1]},  # West
        ]
        for d in directions:
            newX = x + d["coord"][0]
            newY = y + d["coord"][1]
            #print(f"Going {d["dir"]}")
            if 0 <= newX < map_height and 0 <= newY < map_width:
                if list[newX][newY] != crop.category:
                    crop.fences += 1
                    continue
                #print(f"Looking at {list[newX][newY]}")
                if [newX, newY] not in visited:
                    #print(f"Appending at {list[newX][newY]}")
                    visited.append([newX, newY])
                    crop.coords.append([newX, newY])
                    backtrack(newX, newY, crop)
            else:
                crop.fences += 1

    visited = []
    croppas = []
    for i, l in enumerate(list):
        for j, ele in enumerate(l):
            if [i, j] not in visited:
                name = list[i][j]
                print(f"Trying {name}")
                crop = CropPatch(name, 0, 0, [[i, j]], 0)
                visited.append([i, j])
                backtrack(i, j, crop)
                minh = min(crop.coords, key=lambda point: point[0])[0]
                maxh = max(crop.coords, key=lambda point: point[0])[0]
                minw = min(crop.coords, key=lambda point: point[1])[1]
                maxw = max(crop.coords, key=lambda point: point[1])[1]
                crop.height += (maxh - minh) + 1
                crop.width += (maxw - minw) + 1
                croppas.append(crop)
    summa = 0
    for crop in croppas:
        perimeter = crop.fences
        cropCount = len(crop.coords)
        price = perimeter * len(crop.coords)
        summa += price
        print(f"A region of {crop.category} plants with price {cropCount} * {perimeter} = {price}.")
    print(summa)


def gold():
    pass


silver()
gold()
