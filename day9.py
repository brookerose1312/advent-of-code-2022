## Part 1

# Read input
with open("day9input.txt") as f:
    movement = f.readlines()

# numKnots = 2 # Part 1
numKnots = 10  # Part 2
headPos = (0, 0)
knotPositions = [(0, 0) for _ in range(numKnots - 1)]
knotHistories = [{(0, 0)} for _ in range(numKnots - 1)]
directionDict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

sign = lambda x: (1, -1)[x < 0]

for move in movement:
    direction, distance = move.strip().split(" ")
    distance = int(distance)
    positionDiff = directionDict[direction]
    for _ in range(distance):
        headPos = headPos[0] + positionDiff[0], headPos[1] + positionDiff[1]
        movedHeadPos = headPos
        for knotIndex, knotHistory in enumerate(knotHistories):
            x, y = knotPositions[knotIndex][0], knotPositions[knotIndex][1]
            dx, dy = x - movedHeadPos[0], y - movedHeadPos[1]

            if (abs(dx) > 0 and abs(dy) > 1) or (abs(dx) > 1 and abs(dy) > 0):
                knotPositions[knotIndex] = x - sign(dx), y - sign(dy)
            elif abs(dx) > 1:
                knotPositions[knotIndex] = x - sign(dx), y
            elif abs(dy) > 1:
                knotPositions[knotIndex] = x, y - sign(dy)

            movedHeadPos = knotPositions[knotIndex]
            knotHistory.add(knotPositions[knotIndex])

print(len(knotHistories[-1]))
