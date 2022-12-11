## Part 1

# Read input
with open("day3input.txt", "r", encoding="utf-8") as f:
    rucksacks = f.readlines()

# Build priority dict
priorities = dict()

for i in range(1, 27):
    priorities[chr(ord("a") + i - 1)] = i
for i in range(27, 53):
    priorities[chr(ord("A") + i - 27)] = i

# Sum priorities of common items
total_priority = 0

for rucksack in rucksacks:
    fixedsack = rucksack.strip()
    total_items = len(fixedsack)
    compartment1 = rucksack[0 : total_items // 2]
    compartment2 = rucksack[total_items // 2 :]
    commonItem = sorted(set.intersection(set(compartment1), set(compartment2)))[0]
    total_priority += priorities[commonItem]

print(total_priority)

## Part 2

total_badge_priority = 0

for rucksack_index in range(0, len(rucksacks), 3):
    rucksack1 = rucksacks[rucksack_index].strip()
    rucksack2 = rucksacks[rucksack_index + 1].strip()
    rucksack3 = rucksacks[rucksack_index + 2].strip()
    badge = sorted(
        set.intersection(
            set.intersection(set(rucksack1), set(rucksack2)), set(rucksack3)
        )
    )[0]
    total_badge_priority += priorities[badge]

print(total_badge_priority)
