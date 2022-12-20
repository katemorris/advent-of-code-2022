with open("inputs/10.txt", "r") as file:
    commands = file.readlines()

cycle = 1
total_amount = 0
register = 1
for com in commands:
    parts = com.split(" ")
    command = parts[0]
    if len(parts) == 2:
        amount = int(parts[1])
        print(f"checking amount {amount}")
    if command == "addx":
        cycle += 1
        print(f"cycle is {cycle}")
        if cycle in (20, 60, 100, 140, 180, 220):
            print(f"cycle is {cycle}")
            print(f"total amount is {total_amount} and register is {register}")
            print(f"amount to be added {register * cycle}")
            total_amount += register * cycle
        cycle += 1
        print(f"cycle is {cycle}")
        register += amount
        print(f"register is now {register}")
    else:
        cycle += 1
        print(f"cycle is {cycle}, nothing added to register {register}")
    if cycle in (20, 60, 100, 140, 180, 220):
        print(f"cycle is {cycle}")
        print(f"total amount is {total_amount} and register is {register}")
        print(f"amount to be added {register * cycle}")
        total_amount += register * cycle
print(total_amount)
