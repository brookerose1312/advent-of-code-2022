from itertools import groupby

## Part 1

# Read input
with open('day1input.txt') as f:
  calories = f.readlines()

# Split into chunks
indexes = (list(g) for _, g in groupby(calories, key='\n'.__ne__))
grouped_calories = [a + b for a, b in zip(indexes, indexes)]

# Sum chunks

total_cals = []

for elf in grouped_calories:
  total_cal = 0
  for food in elf:
    if (food != '\n'):
      num_string = food[:-1]
      num = int(num_string)
      total_cal += num
  total_cals.append(total_cal)

# Output highest

total_cals.sort(reverse=True)
print(total_cals[0])

## Part 2

print(total_cals[0] + total_cals[1] + total_cals[2])