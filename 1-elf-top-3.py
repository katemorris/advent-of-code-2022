with open("inputs/1.txt", "r") as cals:
    big_set = cals.readlines()
# print(big_set)
current_set = 0
sets = []
for line in big_set:
    if line == "\n":
        sets.append(current_set)
        current_set = 0
    else:
        current_set += int(line)
if current_set != 0:
    sets.append(current_set)
    current_set = 0
sets.sort(reverse=True)
# print(sets)
print(sets[0:3])
print(sum(sets[0:3]))
