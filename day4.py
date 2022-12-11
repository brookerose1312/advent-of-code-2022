# Part 1

# Read input
with open("day4input.txt", "r", encoding="utf-8") as f:
    assignments = f.readlines()

fully_contained_ranges = 0

partially_contained_ranges = 0


def get_elf_start_and_end(incoming_assignment):
    """Gets starting and ending sections for two elves based on the given assignment

    Args:
        incoming_assignment (string): contains two elves assigned sections

    Returns:
        tuple: a tuple containing the start and end sections that the elves are assigned
    """
    elves = incoming_assignment.split(",")
    elf_one = elves[0]
    elf_two = elves[1]
    elf_one_sections = elf_one.split("-")
    elf_two_sections = elf_two.split("-")
    func_elf_one_start = elf_one_sections[0]
    func_elf_one_end = elf_one_sections[1]
    func_elf_two_start = elf_two_sections[0]
    func_elf_two_end = elf_two_sections[1]
    return (
        int(func_elf_one_start),
        int(func_elf_one_end),
        int(func_elf_two_start),
        int(func_elf_two_end),
    )


for assignment in assignments:
    cleaned_assignment = assignment.strip()
    (elf_one_start, elf_one_end, elf_two_start, elf_two_end) = get_elf_start_and_end(
        cleaned_assignment
    )
    if (elf_one_start >= elf_two_start and elf_one_end <= elf_two_end) or (
        elf_one_start <= elf_two_start and elf_one_end >= elf_two_end
    ):
        fully_contained_ranges += 1

print(fully_contained_ranges)

for assignment in assignments:
    cleaned_assignment = assignment.strip()
    (elf_one_start, elf_one_end, elf_two_start, elf_two_end) = get_elf_start_and_end(
        cleaned_assignment
    )
    if (
        (elf_one_start <= elf_two_start <= elf_one_end)
        or (elf_one_start <= elf_two_end <= elf_one_end)
        or (elf_two_start <= elf_one_start <= elf_two_end)
        or (elf_two_start <= elf_one_end <= elf_two_end)
    ):
        partially_contained_ranges += 1

print(partially_contained_ranges)
