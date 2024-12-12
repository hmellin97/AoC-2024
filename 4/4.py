list = []

file_name = "input.txt"

with open(file_name, 'r') as file:
    for line in file:
        list.append(line)

def silver():
    directions = [
        # Cardinal directions
        [[0, 0], [0, 1], [0, 2], [0, 3]],  # North
        [[0, 0], [0, -1], [0, -2], [0, -3]],  # South
        [[0, 0], [1, 0], [2, 0], [3, 0]],  # East
        [[0, 0], [-1, 0], [-2, 0], [-3, 0]],  # West

        # Diagonal directions
        [[0, 0], [1, 1], [2, 2], [3, 3]],  # Northeast
        [[0, 0], [-1, -1], [-2, -2], [-3, -3]],  # Southwest
        [[0, 0], [-1, 1], [-2, 2], [-3, 3]],  # Northwest
        [[0, 0], [1, -1], [2, -2], [3, -3]]  # Southeast
    ]
    xmas_count = 0
    for i,line in enumerate(list):
        for j, char in enumerate(line):
                for d in directions:
                    generatedString = ""
                    for dd in d:
                        ni, nj = i + dd[0], j + dd[1]
                        if 0 <= ni < len(list) and 0 <= nj < len(line.strip()):
                            generatedString += list[i+dd[0]][j+dd[1]]
                    if generatedString == "XMAS":
                        xmas_count += 1
    print(xmas_count)
def gold():
    directions = [
        # Order: M M A S S
        {
            "dir": "West",
            "coords": [[0, 0], [2, 0], [1, -1], [2, -2], [0, -2]],
        },
        {
            "dir": "East",
            "coords": [[0, 0], [2, 0], [1, 1], [0, 2], [2, 2]],
        },
        {
            "dir": "North",
            "coords": [[0, 0], [0, 2], [-1, 1], [-2, 0], [-2, 2]],
        },
        {
            "dir": "South",
            "coords": [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
        }
    ]
    xmas_count = 0
    for i,line in enumerate(list):
        for j, char in enumerate(line):
            for d in directions:
                generatedString = ""
                dir = d["dir"]
                for dd in d["coords"]:
                    ni, nj = i + dd[0], j + dd[1]
                    if 0 <= ni < len(list) and 0 <= nj < len(line.strip()):
                        generatedString += list[i+dd[0]][j+dd[1]]
                    if generatedString == "MMASS":
                        xmas_count += 1
                        #print(f"Found at {dir}")
    print(xmas_count)
silver()
gold()