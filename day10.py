## Part 1

# Read input
with open("day10input.txt", "r", encoding="utf-8") as f:
    instructions = f.readlines()

cycle = 0
x = 1
interesting_cycle_sum = 0
drawn_screen = ""


def update_screen(incoming_cycle, incoming_x, incoming_drawn_screen):
    """returns the updated screen from the incoming drawn screen

    Args:
        incoming_cycle (int): the current cycle
        incoming_x (int): the current value of x
        incoming_drawn_screen (string): the current state of the screen

    Returns:
        string: the new state of the screen
    """
    if incoming_cycle % 40 in [incoming_x - 1, incoming_x, incoming_x + 1]:
        new_drawn_screen = incoming_drawn_screen + "#"
    else:
        new_drawn_screen = incoming_drawn_screen + "."
    if (incoming_cycle + 1) % 40 == 0:
        new_drawn_screen = incoming_drawn_screen + "\n"
    return new_drawn_screen


def update_interesting_cycle(incoming_cycle, incoming_x, incoming_interesting_cycle_sum):
    """Updates the sum of interesting cycles (20, 60, 100, 140, 180, 220)

    Args:
        incoming_cycle (int): the current cycle
        incoming_x (int): the current value of x
        interesting_cycle_sum (int): the current sum of interesting cycles

    Returns:
        int: the new sum of interesting cycles
    """
    new_interesting_cycle_sum = incoming_interesting_cycle_sum
    if incoming_cycle in [20, 60, 100, 140, 180, 220]:
        new_interesting_cycle_sum += incoming_cycle * incoming_x
    return new_interesting_cycle_sum


for instruction in instructions:
    instruction = instruction.strip()
    if instruction == "noop":
        drawn_screen = update_screen(cycle, x, drawn_screen)
        cycle += 1
        interesting_cycle_sum = update_interesting_cycle(cycle, x, interesting_cycle_sum)
    else:
        drawn_screen = update_screen(cycle, x, drawn_screen)
        cycle += 1
        interesting_cycle_sum = update_interesting_cycle(cycle, x, interesting_cycle_sum)
        drawn_screen = update_screen(cycle, x, drawn_screen)
        cycle += 1
        interesting_cycle_sum = update_interesting_cycle(cycle, x, interesting_cycle_sum)
        x += int(instruction.split(" ")[1])

print(interesting_cycle_sum)
print(drawn_screen)
