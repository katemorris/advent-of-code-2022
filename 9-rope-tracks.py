with open("inputs/9.txt", "r") as file:
    commands = file.readlines()

H = {"X": 0, "Y": 0}
T = {"X": 0, "Y": 0}


def move_tail(num):
    # print(f"Pre Tail Move Head:{H}\nTail:{T}")

    x_diff = H["X"] - T["X"]
    y_diff = H["Y"] - T["Y"]
    if abs(x_diff) not in (0, 1) and y_diff == 0:
        T["X"] += num
    elif abs(y_diff) not in (0, 1) and x_diff == 0:
        T["Y"] += num
    elif abs(x_diff) > 1 and abs(y_diff) > 0:
        T["X"] += num
        T["Y"] += y_diff
    elif abs(y_diff) > 1 and abs(x_diff) > 0:
        T["X"] += x_diff
        T["Y"] += num
    if (T["X"], T["Y"]) not in tail_locations:
        tail_locations.append((T["X"], T["Y"]))
    # print(tail_locations)


def move_head(part, total_steps, num):
    while total_steps > 0:
        H[part] += num
        move_tail(num)
        print(f"Post Tail Move Head:{H}\nTail:{T}")
        total_steps -= 1
        print(total_steps)
        return move_head(part, total_steps, num)
    return ""


global tail_locations
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


# H(0,0) T(0,0)
# H(1,0) T(0,0)
# H(2,0) T(1,0)
# H(3,0) T(2,0)
# H(3,1) T(2,0)
# H(3,2) T(2,1)
# H(3,3) T(2,2)
# H(3,4) T(2,3)
# 6588 too high
