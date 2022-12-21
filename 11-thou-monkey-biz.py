import code
import math

with open("inputs/11-short.txt", "r") as file:
    monkeys = file.read().split("\n\n")


monkey_list = {}
for mankey in monkeys:
    attributes = mankey.split("\n")
    for line in attributes:
        if "Monkey" in line:
            monkey_num = int(line.replace("Monkey ", "").replace(":", ""))
            # print(monkey_num)
        if "Starting items:" in line:
            items = line.replace("Starting items: ", "").strip().split(", ")
            items = [int(x) for x in items]
            # print(items)
        if "Operation" in line:
            operation, value = (
                line.replace("Operation: new = old ", "").strip().split(" ")
            )
            # print(operation, value)
        if "Test:" in line:
            test_divisor = int(line.replace("Test: divisible by ", ""))
            # print(test_divisor)
        if "If true" in line:
            true_monkey = int(line.replace("If true: throw to monkey ", ""))
            # print(true_monkey)
        if "If false" in line:
            false_monkey = int(line.replace("If false: throw to monkey ", ""))
            # print(false_monkey)
    # code.interact(local=dict(globals(), **locals()))

    monkey_list[monkey_num] = {
        "items": items,
        "operation": operation,
        "op_value": value,
        "test_divisor": test_divisor,
        "true_monkey": true_monkey,
        "false_monkey": false_monkey,
        "inspections": 0,
    }


def do_rounds(monkey_list, rounds):
    while rounds > 0:
        for monkey, att in monkey_list.items():
            item_list = [x for x in att["items"]]
            # print(f"starting monkey {monkey} with attributes {att}")
            for item in item_list:
                # check operation value
                if att["op_value"] == "old":
                    value = item
                else:
                    value = int(att["op_value"])
                # process new item value
                # print(f"item {item} value {value}")
                if att["operation"] == "+":
                    item += value
                    # print(f"item {item} post add")
                elif att["operation"] == "*":
                    item *= value
                    # print(f"item {item} post multiply")
                # test divisor
                if item % att["test_divisor"] == 0:
                    monkey_list[att["true_monkey"]]["items"].append(item)
                else:
                    monkey_list[att["false_monkey"]]["items"].append(item)
                # add reviewed item
                monkey_list[monkey]["inspections"] += 1
            monkey_list[monkey]["items"] = []
        return do_rounds(monkey_list, rounds - 1)
    return monkey_list


print(monkey_list)
rounds = 1000
final = do_rounds(monkey_list, rounds)
print(final)
inspections = [atts["inspections"] for atts in final.values()]
sorted_insp = sorted(inspections)
print(sorted_insp[-1] * sorted_insp[-2])
