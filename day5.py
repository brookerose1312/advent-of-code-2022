## Part 1

# Read input
with open("day5input.txt") as f:
  stackInput = f.readlines()

# Split into stacks and movements
stackInputData = []
stackInputMovements = []

dataDone = False

for line in stackInput:
  if (line == '\n'):
    dataDone = True
    continue
  if (not dataDone):
    stackInputData.insert(0, line.rstrip())
  else:
    stackInputMovements.append(line.strip())

# Generate actual stacks

stacks = []
part2Stacks = []
# calculate number of columns
numCols = int(stackInputData[0].strip().split(' ')[-1])
for colIndex in range(numCols):
  col = []
  # loop over actual rows of stacks
  for rowIndex in range(1, len(stackInputData)):
    row = stackInputData[rowIndex]
    colSelector = (colIndex) * 4
    item = row[colSelector:colSelector+4].strip()
    if (item != ''):
      col.append(item)
  stacks.append(col)
  # col copy because otherwise part2Stacks and stacks would be identical
  part2Stacks.append(col.copy())

# Move items in stacks

for movement in stackInputMovements:
  movementComponents = movement.split(' ')
  numToMove = int(movementComponents[1])
  fromCol = int(movementComponents[3])
  toCol = int(movementComponents[5])
  # move 1-by-1
  for i in range(numToMove):
    item = stacks[fromCol-1].pop()
    stacks[toCol-1].append(item)

stackTops = ""

for stack in stacks:
  stackTops += stack[-1][1]

print('part 1 stack tops')
print(stackTops)

## Part 2

# Move items in stacks

for movement in stackInputMovements:
  movementComponents = movement.split(' ')
  numToMove = int(movementComponents[1])
  fromCol = int(movementComponents[3])
  toCol = int(movementComponents[5])
  # move a chunk
  movedComponents = []
  for i in range(numToMove):
    item = part2Stacks[fromCol-1].pop()
    movedComponents.insert(0, item)
  for component in movedComponents:
    part2Stacks[toCol-1].append(component)

part2StackTops = ""

for stack in part2Stacks:
  part2StackTops += stack[-1][1]

print('part 2 stack tops')
print(part2StackTops)