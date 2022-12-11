## Part 1

# Read input
with open("day5input.txt", "r", encoding="utf-8") as f:
    stack_input = f.readlines()

# Split into stacks and movements
stack_input_data = []
stack_input_movements = []

data_is_done = False

for line in stack_input:
    if line == "\n":
        data_is_done = True
        continue
    if not data_is_done:
        stack_input_data.insert(0, line.rstrip())
    else:
        stack_input_movements.append(line.strip())

# Generate actual stacks

stacks = []
part_two_stacks = []
# calculate number of columns
num_cols = int(stack_input_data[0].strip().split(" ")[-1])
for col_index in range(num_cols):
    col = []
    # loop over actual rows of stacks
    for row_index in range(1, len(stack_input_data)):
        row = stack_input_data[row_index]
        col_selector = col_index * 4
        item = row[col_selector : col_selector + 4].strip()
        if item != "":
            col.append(item)
    stacks.append(col)
    # col copy because otherwise part2Stacks and stacks would be identical
    part_two_stacks.append(col.copy())

# Move items in stacks

for movement in stack_input_movements:
    movement_components = movement.split(" ")
    num_to_move = int(movement_components[1])
    from_col = int(movement_components[3])
    to_col = int(movement_components[5])
    # move 1-by-1
    for i in range(num_to_move):
        item = stacks[from_col - 1].pop()
        stacks[to_col - 1].append(item)

stack_tops = ""

for stack in stacks:
    stack_tops += stack[-1][1]

print("part 1 stack tops")
print(stack_tops)

## Part 2

# Move items in stacks

for movement in stack_input_movements:
    movement_components = movement.split(" ")
    num_to_move = int(movement_components[1])
    from_col = int(movement_components[3])
    to_col = int(movement_components[5])
    # move a chunk
    moved_components = []
    for i in range(num_to_move):
        item = part_two_stacks[from_col - 1].pop()
        moved_components.insert(0, item)
    for component in moved_components:
        part_two_stacks[to_col - 1].append(component)

part_two_stack_tops = ""

for stack in part_two_stacks:
    part_two_stack_tops += stack[-1][1]

print("part 2 stack tops")
print(part_two_stack_tops)
