from re import findall

with open("./data.txt") as data:
    data = data.readlines()

def mul(x,y):
    return x*y

mul_sum =0

for each_row in data:
    all_row_pairs = findall(r"mul\((\d+),(\d+)\)", each_row)
    for pair in all_row_pairs:
        mul_sum += mul(int(pair[0]),int(pair[1]))

print(mul_sum)





