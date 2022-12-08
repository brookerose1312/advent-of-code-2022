## Part 1

# Read input
with open("day8input.txt") as f:
    trees = f.readlines()

# calculate number of trees on edge
numVisible = (len(trees) * 2) + (len(trees[0].strip()) * 2) - 4

# loop over interior trees and see if trees are visible
for row in range(1, len(trees) - 1):
    treeRow = trees[row].strip()
    for column in range(1, len(treeRow) - 1):
        tree = int(trees[row][column])
        visible = False
        # check trees to left
        for leftTreeIndex in range(0, column):
            leftTree = int(trees[row][leftTreeIndex])
            if leftTree >= tree:
                break
            if leftTree < tree and leftTreeIndex == column - 1:
                visible = True
        if visible == True:
            numVisible += 1
            continue

        # check trees above
        for upTreeIndex in range(0, row):
            upTree = int(trees[upTreeIndex][column])
            if upTree >= tree:
                break
            if upTree < tree and upTreeIndex == row - 1:
                visible = True
        if visible == True:
            numVisible += 1
            continue

        # check trees to right
        for rightTreeIndex in range(column + 1, len(treeRow)):
            rightTree = int(trees[row][rightTreeIndex])
            if rightTree >= tree:
                break
            if rightTree < tree and rightTreeIndex == len(treeRow) - 1:
                visible = True
        if visible == True:
            numVisible += 1
            continue

        # check trees below
        for downTreeIndex in range(row + 1, len(trees)):
            downTree = int(trees[downTreeIndex][column])
            if downTree >= tree:
                break
            if downTree < tree and downTreeIndex == len(trees) - 1:
                visible = True
        if visible == True:
            numVisible += 1
            continue

print(numVisible)

## Part 2

scenicDict = {}
# Loop over interior trees and find highest scenic score

for row in range(1, len(trees) - 1):
    treeRow = trees[row].strip()
    for column in range(1, len(treeRow) - 1):
        tree = int(trees[row][column])
        leftScore = 0
        upScore = 0
        rightScore = 0
        downScore = 0
        # calculate leftScore
        for leftTreeIndex in range(column-1, -1, -1):
            leftTree = int(trees[row][leftTreeIndex])
            leftScore += 1
            if leftTree >= tree:
                break

        # calculate upScore
        for upTreeIndex in range(row-1, -1, -1):
            upTree = int(trees[upTreeIndex][column])
            upScore += 1
            if upTree >= tree:
                break

        # calculate rightScore
        for rightTreeIndex in range(column + 1, len(treeRow)):
            rightTree = int(trees[row][rightTreeIndex])
            rightScore += 1
            if rightTree >= tree:
                break

        # calculate downScore
        for downTreeIndex in range(row + 1, len(trees)):
            downTree = int(trees[downTreeIndex][column])
            downScore += 1
            if downTree >= tree:
                break

        scenicScore = leftScore * upScore * rightScore * downScore
        scenicDict[(row, column)] = scenicScore

print(max(scenicDict.values()))