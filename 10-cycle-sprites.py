import code

with open("inputs/10.txt", "r") as file:
    commands = file.readlines()

cycle = 1
register = 1
line = []
lines = []
sprites = (register - 1, register, register + 1)
for com in commands:
    parts = com.split(" ")
    command = parts[0]
    # print(parts)
    if len(parts) == 2:
        amount = int(parts[1].strip())
    if command == "addx":
        print(f"s cycle: {cycle}| pos {cycle - 1} | sprites {sprites}\n line: {line}")
        if cycle - 1 in sprites:
            line.append("#")
        else:
            line.append(".")
        print(f"e cycle: {cycle} -- sprites {sprites}\n line: {line}")
        # end of cycle
        cycle += 1
        # start of cycle
        print(f"s cycle: {cycle}| pos {cycle - 1} | sprites {sprites}\n line: {line}")
        if cycle == 41:
            # code.interact(local=dict(globals(), **locals()))
            lines.append(line)
            line = []
            cycle = 1
        if cycle - 1 in sprites:
            line.append("#")
        else:
            line.append(".")
        register += amount
        sprites = (register - 1, register, register + 1)
        print(f"e cycle: {cycle} -- new sprites {sprites}\n line: {line}")
        # end of cycle
        cycle += 1
    else:
        print(f"s cycle: {cycle}| pos {cycle - 1} | sprites {sprites}\n line: {line}")
        if cycle - 1 in sprites:
            line.append("#")
        else:
            line.append(".")
        print(f"e cycle: {cycle} -- sprites {sprites}\n line: {line}")
        # end of cycle
        cycle += 1

    if cycle == 41:
        # code.interact(local=dict(globals(), **locals()))
        lines.append(line)
        line = []
        cycle = 1

for line in lines:
    print("".join(line))
