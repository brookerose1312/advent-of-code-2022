## Part 1

# Read input
with open('day3input.txt') as f:
  rucksacks = f.readlines()

# Build priority dict
priorities = dict()

for i in range(1, 27):
  priorities[chr(ord('a') + i - 1)]=i
for i in range(27, 53):
  priorities[chr(ord('A') + i - 27)]=i

# Sum priorities of common items
totalPriority = 0

for rucksack in rucksacks:
  fixedsack = rucksack.strip()
  totalItems = len(fixedsack)
  compartment1 = rucksack[0:totalItems//2]
  compartment2 = rucksack[totalItems//2:]
  commonItem = sorted(
    set.intersection(
      set(compartment1),
      set(compartment2)
    )
  )[0]
  totalPriority += priorities[commonItem]

print(totalPriority)

## Part 2

totalBadgePriority = 0

for rucksackIndex in range(0, len(rucksacks), 3):
  rucksack1 = rucksacks[rucksackIndex].strip()
  rucksack2 = rucksacks[rucksackIndex+1].strip()
  rucksack3 = rucksacks[rucksackIndex+2].strip()
  badge = sorted(
    set.intersection(
      set.intersection(
        set(rucksack1),
        set(rucksack2)
      ),
      set(rucksack3)
    )
  )[0]
  totalBadgePriority += priorities[badge]

print(totalBadgePriority)