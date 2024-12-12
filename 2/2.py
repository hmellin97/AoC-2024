list = []

file_name = "sinput.txt"

with open(file_name, 'r') as file:
    for line in file:
        line = line.split()
        list.append(line)

def silver():
    def is_safe(line, direction):
        for i in range(len(line) - 1):
            current = int(line[i])
            next_value = int(line[i + 1])
            if direction == "up" and not (current > next_value and current - next_value <= 3):
                return False
            if direction == "down" and not (current < next_value and next_value - current <= 3):
                return False
        return True

    safe_count = 0

    for line in list:
        if is_safe(line, "up"):
            safe_count += 1
        if is_safe(line, "down"):
            safe_count += 1

    print(safe_count)

def gold():
    def is_safe(line, direction, usedProblemDampener):

        for i in range(len(line) - 1):
            current = int(line[i])
            next_value = int(line[i + 1])
            if direction == "down" and not (current > next_value and current - next_value <= 3):
                if not usedProblemDampener:
                    tryWithOutThatOne = line[:i+1] + line[i+1 + 1:]
                    if is_safe(tryWithOutThatOne, "down", True):
                        return True
                    elif i < len(line)-2:
                        continue
                    elif i == len(line)-2:
                        tryWithOutLastOne = line[:len(line)-1]
                        if is_safe(tryWithOutLastOne, "down", True):
                            return True
                    else:
                        return False
                return False
            if direction == "up" and not (current < next_value and next_value - current <= 3):
                if not usedProblemDampener:
                    tryWithOutThatOne = line[:i+1] + line[i+1 + 1:]
                    if is_safe(tryWithOutThatOne, "up", True):
                        return True
                    elif i < len(line)-2:
                        #print("GOt here")
                        continue
                    elif i == len(line)-2:
                        tryWithOutLastOne = line[:len(line)-1]
                        if is_safe(tryWithOutLastOne, "up", True):
                            return True
                    else:
                        #print("boi")
                        return False
                return False
        return True

    safe_count = 0

    for line in list:
        if is_safe(line, "up", False):
            print(f"Line {line} was safe GOING UP")
            safe_count += 1
        else:
            print(f"Line {line} was unsafe GOING UP")
        if is_safe(line, "down", False):
            print(f"Line {line} was safe GOING DOWN")
            safe_count += 1
        else:
            print(f"Line {line} was unsafe GOING DOWN")


    print(safe_count)



silver()
gold()