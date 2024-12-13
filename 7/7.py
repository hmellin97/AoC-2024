import datetime
import time

list = []
file_name = "input.txt"

with open(file_name, 'r') as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.split(":")
        t = line[0]
        n = line[1].split(" ")[1:]
        list.append([t]+n)


def silver():
    res = 0
    for l in list:
        target = l[0]
        numbers = l[1:]
        operationsCombinatinos = getOperationCombinations(len(numbers) - 1)
        #print("dogo")
        res += calculate(operationsCombinatinos, numbers, target)

    print(res)

def calculate(operationsCombinatinos, numbers, target):
    for cmb in operationsCombinatinos:
        res = int(numbers[0])
        for i, operation in enumerate(cmb):
            nxt = int(numbers[i + 1])
            if operation == "+":
                res += nxt
            elif operation == "*":
                res *= nxt
        if res == int(target):
            return res
    return 0

def getOperationCombinations(length):
    res = []
    cur = []

    def backtrack():
        if len(cur) == length:
            res.append(cur.copy())
            return
        cur.append("+")
        backtrack()
        cur.pop()
        cur.append("*")
        backtrack()
        cur.pop()

    backtrack()
    return res

def gold():
    res = 0
    for l in list:
        target = l[0]
        numbers = l[1:]
        operationsCombinatinos = getOperationCombinationsExtra(len(numbers)-1)
        #print("dogo")
        res += calculateExtra(operationsCombinatinos, numbers, target)

    print(res)
def getOperationCombinationsExtra(length):
    res = []
    cur = []

    def backtrack():
        if len(cur) == length:
            res.append(cur.copy())
            return
        cur.append("+")
        backtrack()
        cur.pop()
        cur.append("*")
        backtrack()
        cur.pop()
        cur.append("||")
        backtrack()
        cur.pop()

    backtrack()
    return res

def calculateExtra(operationsCombinatinos, numbers, target):
    for cmb in operationsCombinatinos:
        res = int(numbers[0])
        for i, operation in enumerate(cmb):
            nxt = int(numbers[i + 1])
            if operation == "+":
                res += nxt
            elif operation == "*":
                res *= nxt
            elif operation == "||":
                res = int(str(res)+str(nxt))
        if res == int(target):
            #print(f"{target}, {numbers} was valid")
            return res
    return 0




silver()
t1 = time.time()
gold()
t2 = time.time()
print(f"Execution Time: {t2-t1:.6f} seconds")
