import re

input = ""

file_name = "input.txt"

with open(file_name, 'r') as file:
    for line in file:
        input += line


def silver():
    pattern = r"mul\(\d+,\d+\)"  # Match one or more digits
    matches = re.findall(pattern, input)
    #print("Numbers found:", matches)
    res = 0
    for m in matches:
        m = m.split(",")
        #print(m)
        factor1 = int(m[0][4:])
        factor2 = int(m[1].replace(")", ""))
        #print(factor1)
        #print(factor2)
        res += (factor1 * factor2)
    print(res)


def gold():
    pattern = r"don\'t\(\)|do\(\)|mul\(\d+,\d+\)"
    matches = re.findall(pattern, input)
    res = 0
    products = {}  # position and res
    startstopinstructions = {}
    for m in matches:
        for i in range(len(input)):
            searched_string = input[i:i + len(m)]
            if m == searched_string:
                if m == "do()":
                    startstopinstructions[i] = "do()"
                elif m == "don't()":
                    startstopinstructions[i] = "don't()"
                else:
                    m = m.split(",")
                    factor1 = int(m[0][4:])
                    factor2 = int(m[1].replace(")", ""))
                    products[i] = factor1 * factor2

    enabled = True
    for i in range(len(input)):
        if i in startstopinstructions:
            if startstopinstructions[i] == "do()":
                enabled = True
            elif startstopinstructions[i] == "don't()":
                enabled = False
        if i in products and enabled:
            res += products[i]
    print(res)


silver()
gold()
