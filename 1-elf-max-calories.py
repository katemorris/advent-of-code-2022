with open("inputs/1.txt", "r") as cals:
    big_set = cals.readlines()
current_set = 0
max_set = 0
for line in big_set:
    if line == "\n":
        if current_set > max_set:
            max_set = current_set
        current_set = 0
    else:
        current_set += int(line)
print(max_set)
