# Part 1

# Read input
with open("day4input.txt") as f:
    assignments = f.readlines()

fullyContainedRanges = 0

partiallyContainedRanges = 0


def getElfStartAndEnd(assignment):
    elves = assignment.split(",")
    elf1 = elves[0]
    elf2 = elves[1]
    elf1Sections = elf1.split("-")
    elf2Sections = elf2.split("-")
    elf1Start = elf1Sections[0]
    elf1End = elf1Sections[1]
    elf2Start = elf2Sections[0]
    elf2End = elf2Sections[1]
    return (elf1Start, elf1End, elf2Start, elf2End)


for assignment in assignments:
    cleanedAssignment = assignment.strip()
    (elf1Start, elf1End, elf2Start, elf2End) = getElfStartAndEnd(cleanedAssignment)
    if (int(elf1Start) >= int(elf2Start) and int(elf1End) <= int(elf2End)) or (
        int(elf1Start) <= int(elf2Start) and int(elf1End) >= int(elf2End)
    ):
        fullyContainedRanges += 1

print(fullyContainedRanges)

for assignment in assignments:
    cleanedAssignment = assignment.strip()
    (elf1Start, elf1End, elf2Start, elf2End) = getElfStartAndEnd(cleanedAssignment)
    if (
        (int(elf1Start) <= int(elf2Start) <= int(elf1End))
        or (int(elf1Start) <= int(elf2End) <= int(elf1End))
        or (int(elf2Start) <= int(elf1Start) <= int(elf2End))
        or (int(elf2Start) <= int(elf1End) <= int(elf2End))
    ):
        partiallyContainedRanges += 1

print(partiallyContainedRanges)
