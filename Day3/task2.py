from re import findall, split

with open("./data.txt") as data:
    data = data.readlines()

def mul(x,y):
    return x*y

mul_sum =0
calculate = True

for each_row in data:
    elements = findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", each_row)
    for element in elements:
        if element == "don't()":
            calculate = False
        elif element == "do()":
            calculate = True
        elif element.startswith("mul"):
            pair = findall(r"mul\((\d+),(\d+)\)", element)
            if pair and calculate:
               mul_sum += mul(int(pair[0][0]),int(pair[0][1]))

print(mul_sum)






