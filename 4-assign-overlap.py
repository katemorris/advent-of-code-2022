count = 0
sets = []
with open("inputs/4.txt", "r") as sacks:
    for pair in sacks.readlines():
        elf_1, elf_2 = [set.split("-") for set in pair.strip().split(",")]
        elf_1 = [int(x) for x in elf_1]
        elf_2 = [int(x) for x in elf_2]
        elf_1_list = list(range(elf_1[0], elf_1[1] + 1))
        elf_2_list = list(range(elf_2[0], elf_2[1] + 1))

        # print(elf_1, elf_2)
        if elf_1[0] in elf_2_list or elf_1[1] in elf_2_list:
            count += 1
            sets.append([elf_1, elf_2])
        elif elf_2[0] in elf_1_list or elf_2[1] in elf_1_list:
            count += 1
            sets.append([elf_1, elf_2])
        else:
            continue
print(count)
# print(sets)
# 2-4, 6-8 No
# 6-8, 2-4 No
# 5-7, 7-9 Yes
# 7-9, 5-7 Yes
# 4-8, 2-6 Yes
# 2-6, 4-8 Yes
