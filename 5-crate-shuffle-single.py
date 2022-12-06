with open("inputs/5.txt", "r") as file:
    diagram, instructions = file.read().split("\n\n")
    diagram = [x.split(" ") for x in diagram.split("\n")]
    instructions = [
        x.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")
        for x in instructions.strip().split("\n")
    ]

    # diagram
    # get letter and placement and put in dictionary. [letter:coordinates]
    # might need limit of x axis
    # print(diagram)
    y_length = len(diagram) - 1
    for_x_length = len(diagram[y_length]) - 2  # bc of extra space
    x_line = diagram.pop(y_length)
    x_length = int(x_line[for_x_length])
    crate_map = {}
    for index, contents in enumerate(diagram):
        y = index + 1
        spaces_count = 0
        x = 1
        print(f"contents: {contents}\n crates:{crate_map}")
        for character in contents:
            if spaces_count == 4 and character == "":
                x += 1
                spaces_count = 1
            elif character == "":
                spaces_count += 1
                continue
            else:
                if spaces_count == 4:
                    x += 1
                    spaces_count = 0
                crate = character.replace("[", "").replace("]", "")
                if x in crate_map.keys() and type(crate_map[x]) is list:
                    crate_map[x].insert(0, crate)
                else:
                    crate_map[x] = [crate]
                x += 1
    print(crate_map)

    # instructions 0-number to move, 1-from column, 2-to column
    print(instructions)
    for set in instructions:
        num = int(set[0])
        from_col = int(set[1])
        to_col = int(set[2])
        while num >= 1:
            crate_to_move = crate_map[from_col].pop()
            crate_map[to_col].append(crate_to_move)
            num -= 1

    print(crate_map)
    message_list = []
    while x_length > 0:
        last_item = crate_map[x_length].pop()
        message_list.insert(0, last_item)
        x_length -= 1
    message = "".join(message_list)
    print(message)
