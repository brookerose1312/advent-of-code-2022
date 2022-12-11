## Part 1

# Read input
with open("day9input.txt", "r", encoding="utf-8") as f:
    movement = f.readlines()

# NUM_KNOTS = 2 # Part 1
NUM_KNOTS = 10  # Part 2
head_pos = (0, 0)
knot_positions = [(0, 0) for _ in range(NUM_KNOTS - 1)]
knot_histories = [{(0, 0)} for _ in range(NUM_KNOTS - 1)]
direction_dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

def sign(number):
    """Returns the sign of the number attached to the unit variable.
        0 is treated as positive

    Args:
        number (int): a number

    Returns:
        int: either 1 for a positive number (or 0) or -1 for a negative number
    """
    if number < 0:
        return -1
    return 1

for move in movement:
    direction, distance = move.strip().split(" ")
    distance = int(distance)
    position_diff = direction_dict[direction]
    for _ in range(distance):
        head_pos = head_pos[0] + position_diff[0], head_pos[1] + position_diff[1]
        moved_head_pos = head_pos
        for knot_index, knot_history in enumerate(knot_histories):
            x, y = knot_positions[knot_index][0], knot_positions[knot_index][1]
            dx, dy = x - moved_head_pos[0], y - moved_head_pos[1]

            if (abs(dx) > 0 and abs(dy) > 1) or (abs(dx) > 1 and abs(dy) > 0):
                knot_positions[knot_index] = x - sign(dx), y - sign(dy)
            elif abs(dx) > 1:
                knot_positions[knot_index] = x - sign(dx), y
            elif abs(dy) > 1:
                knot_positions[knot_index] = x, y - sign(dy)

            moved_head_pos = knot_positions[knot_index]
            knot_history.add(knot_positions[knot_index])

print(len(knot_histories[-1]))
