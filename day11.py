## Part 1

# Read input
with open("day11input.txt", "r", encoding="utf-8") as f:
    monkey_input = f.readlines()


def build_monkey_list():
    internal_monkeys = []
    entering_monkey = False
    monkey_index = 0
    new_monkey = {"index": monkey_index, "number_inspected": 0}

    # build monkey list
    for line in monkey_input:
        line = line.split()
        if line == []:
            internal_monkeys.append(new_monkey)
            entering_monkey = False
            monkey_index += 1
            new_monkey = {"index": monkey_index, "number_inspected": 0}
        elif line[0] == "Monkey":
            entering_monkey = True
        elif entering_monkey:
            if line[0] == "Starting":
                items = line[2:]
                new_monkey["items"] = []
                for item in items:
                    item = item.strip(",")
                    new_monkey["items"].append(int(item))
            elif line[0] == "Operation:":
                operators = line[4:6]
                new_monkey["operators"] = []
                for operator in operators:
                    if operator.isdigit():
                        new_monkey["operators"].append(int(operator))
                    else:
                        new_monkey["operators"].append(operator)
            elif line[0] == "Test:":
                new_monkey["divisible_by"] = int(line[3])
            elif line[0] == "If":
                if line[1] == "true:":
                    new_monkey["true"] = int(line[5])
                elif line[1] == "false:":
                    new_monkey["false"] = int(line[5])
    # add final monkey
    internal_monkeys.append(new_monkey)
    return internal_monkeys


monkeys = build_monkey_list()

# run monkey simulations
for round in range(20):
    for monkey in monkeys:
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            monkey["number_inspected"] += 1
            modifier = monkey["operators"][1]
            if modifier == "old":
                modifier = item
            if monkey["operators"][0] == "*":
                item = (item * modifier) // 3
            else:
                item = (item + modifier) // 3
            if item % monkey["divisible_by"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)

# generate list of items inspected
items_inspected = []
for monkey in monkeys:
    items_inspected.append(monkey["number_inspected"])
    monkey["number_inpsected"] = 0
items_inspected.sort(reverse=True)

# print monkey business
print(f"Monkey business: {items_inspected[0] * items_inspected[1]}")

## Part 2

new_monkeys = build_monkey_list()

# run new monkey simulations
for round in range(10000):
    for monkey in new_monkeys:
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            monkey["number_inspected"] += 1
            modifier = monkey["operators"][1]
            if modifier == "old":
                modifier = item
            if monkey["operators"][0] == "*":
                item = (
                    item * modifier
                ) % 223092870  # product of primes up to 23 -- all tests are divisible by a prime number <= 23!
            else:
                item = (item + modifier) % 223092870
            if item % monkey["divisible_by"] == 0:
                new_monkeys[monkey["true"]]["items"].append(item)
            else:
                new_monkeys[monkey["false"]]["items"].append(item)

# generate list of items inspected
items_inspected = []
for monkey in new_monkeys:
    items_inspected.append(monkey["number_inspected"])
    monkey["number_inpsected"] = 0
items_inspected.sort(reverse=True)

# print monkey business
print(f"Monkey business part 2: {items_inspected[0] * items_inspected[1]}")
