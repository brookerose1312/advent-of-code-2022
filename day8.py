## Part 1

# Read input
with open("day8input.txt", "r", encoding="utf-8") as f:
    trees = f.readlines()

# calculate number of trees on edge
num_visible = (len(trees) * 2) + (len(trees[0].strip()) * 2) - 4

# loop over interior trees and see if trees are visible
for row in range(1, len(trees) - 1):
    tree_row = trees[row].strip()
    for column in range(1, len(tree_row) - 1):
        tree = int(trees[row][column])
        visible = False
        # check trees to left
        for left_tree_index in range(0, column):
            left_tree = int(trees[row][left_tree_index])
            if left_tree >= tree:
                break
            if left_tree < tree and left_tree_index == column - 1:
                visible = True
        if visible == True:
            num_visible += 1
            continue

        # check trees above
        for up_tree_index in range(0, row):
            up_tree = int(trees[up_tree_index][column])
            if up_tree >= tree:
                break
            if up_tree < tree and up_tree_index == row - 1:
                visible = True
        if visible == True:
            num_visible += 1
            continue

        # check trees to right
        for right_tree_index in range(column + 1, len(tree_row)):
            right_tree = int(trees[row][right_tree_index])
            if right_tree >= tree:
                break
            if right_tree < tree and right_tree_index == len(tree_row) - 1:
                visible = True
        if visible == True:
            num_visible += 1
            continue

        # check trees below
        for down_tree_index in range(row + 1, len(trees)):
            down_tree = int(trees[down_tree_index][column])
            if down_tree >= tree:
                break
            if down_tree < tree and down_tree_index == len(trees) - 1:
                visible = True
        if visible == True:
            num_visible += 1
            continue

print(num_visible)

## Part 2

scenic_dict = {}
# Loop over interior trees and find highest scenic score

for row in range(1, len(trees) - 1):
    tree_row = trees[row].strip()
    for column in range(1, len(tree_row) - 1):
        tree = int(trees[row][column])
        left_score = 0
        up_score = 0
        right_score = 0
        down_score = 0
        # calculate leftScore
        for left_tree_index in range(column - 1, -1, -1):
            left_tree = int(trees[row][left_tree_index])
            left_score += 1
            if left_tree >= tree:
                break

        # calculate upScore
        for up_tree_index in range(row - 1, -1, -1):
            up_tree = int(trees[up_tree_index][column])
            up_score += 1
            if up_tree >= tree:
                break

        # calculate rightScore
        for right_tree_index in range(column + 1, len(tree_row)):
            right_tree = int(trees[row][right_tree_index])
            right_score += 1
            if right_tree >= tree:
                break

        # calculate downScore
        for down_tree_index in range(row + 1, len(trees)):
            down_tree = int(trees[down_tree_index][column])
            down_score += 1
            if down_tree >= tree:
                break

        scenic_score = left_score * up_score * right_score * down_score
        scenic_dict[(row, column)] = scenic_score

print(max(scenic_dict.values()))
