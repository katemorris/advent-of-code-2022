import code

with open("inputs/9.txt", "r") as file:
    commands = file.readlines()

H = {"X": 0, "Y": 0}
tails = {
    1: {"X": 0, "Y": 0},
    2: {"X": 0, "Y": 0},
    3: {"X": 0, "Y": 0},
    4: {"X": 0, "Y": 0},
    5: {"X": 0, "Y": 0},
    6: {"X": 0, "Y": 0},
    7: {"X": 0, "Y": 0},
    8: {"X": 0, "Y": 0},
    9: {"X": 0, "Y": 0},
}


def move_tail(prev, curr, num):
    # print(f"Pre Tail Move Head:{H}\nTail:{T}")
    if prev in range(10):
        prev = tails[prev]

    x_diff = prev["X"] - tails[curr]["X"]
    # this is the number of positions the next knot is from the previous knot
    y_diff = prev["Y"] - tails[curr]["Y"]
    if x_diff > 1 and y_diff == 0:
        tails[curr]["X"] = prev["X"] - 1
    elif x_diff < -1 and y_diff == 0:
        tails[curr]["X"] = prev["X"] + 1
    elif y_diff > 1 and x_diff == 0:
        tails[curr]["Y"] = prev["Y"] - 1
    elif y_diff < -1 and x_diff == 0:
        tails[curr]["Y"] = prev["Y"] + 1
    elif (x_diff > 1 and y_diff > 0) or (y_diff > 1 and x_diff > 0):
        tails[curr]["X"] += 1
        tails[curr]["Y"] += 1
    elif (x_diff > 1 and y_diff < 0) or (y_diff < -1 and x_diff > 0):
        tails[curr]["X"] += 1
        tails[curr]["Y"] -= 1
    elif (x_diff < -1 and y_diff < 0) or (y_diff < -1 and x_diff < 0):
        tails[curr]["X"] -= 1
        tails[curr]["Y"] -= 1
    elif (x_diff < -1 and y_diff > 0) or (y_diff > 1 and x_diff < 0):
        tails[curr]["X"] -= 1
        tails[curr]["Y"] += 1
    if abs(prev["X"] - tails[curr]["X"]) not in (0, 1) or abs(
        prev["Y"] - tails[curr]["Y"]
    ) not in (0, 1):
        code.interact(local=dict(globals(), **locals()))

    if curr == 9 and (tails[curr]["X"], tails[curr]["Y"]) not in tail_locations:
        tail_locations.append((tails[curr]["X"], tails[curr]["Y"]))
        # code.interact(local=dict(globals(), **locals()))
        return ""
    elif curr == 9:
        return ""
    elif curr != 9:
        next = curr + 1
        move_tail(curr, next, num)

    # print(tail_locations)


def move_head(part, total_steps, num):
    while total_steps > 0:
        H[part] += num
        move_tail(H, 1, num)
        print(f"Post Tail Move Head:{H}\nTails:{tails}")
        total_steps -= 1
        print(total_steps)
        return move_head(part, total_steps, num)
    return ""


tail_locations = [(0, 0)]
for x in commands:
    dir, num_str = x.strip().split(" ")
    steps = int(num_str)
    if dir == "R":
        part = "X"
        move_head(part, steps, 1)
    elif dir == "L":
        part = "X"
        move_head(part, steps, -1)
    elif dir == "U":
        part = "Y"
        move_head(part, steps, 1)
    elif dir == "D":
        part = "Y"
        move_head(part, steps, -1)
print(len(tail_locations))


# 3863 too high
# 2503 too high
