with open("inputs/6.txt", "r") as file:
    for line in file.readlines():
        letter_list = []
        for index, char in enumerate(line):
            # print(f"character {index+1}: {char} and list: {letter_list}")
            letter_list.append(char)
            # print(letter_list)
            list_len = len(letter_list)
            if list_len > 4 and list_len > 1:
                letter_list.pop(0)
                # print(f"after removal list {letter_list}")
            list_len = len(letter_list)
            # print(list_len, letter_list)
            if list_len == 4 and len(set(letter_list)) < list_len:
                # print(f"skipping, duplicates {set(letter_list)}")
                continue
            elif list_len == 4 and len(set(letter_list)) == list_len:
                print(f"success! {letter_list}")
                print(index + 1)
                break
            else:
                # print("do what?")
                continue
