## Part 1

# Read input
with open("day10input.txt") as f:
    instructions = f.readlines()

cycle = 0
X = 1
interestingCycleSum = 0
drawnScreen = ""


def updateScreen(cycle, X, drawnScreen):
    if cycle % 40 in [X - 1, X, X + 1]:
        drawnScreen += "#"
    else:
        drawnScreen += "."
    if (cycle + 1) % 40 == 0:
        drawnScreen += "\n"
    return drawnScreen


def updateInterestingCycle(cycle, X, interestingCycleSum):
    if cycle in [20, 60, 100, 140, 180, 220]:
        interestingCycleSum += cycle * X
    return interestingCycleSum


for instruction in instructions:
    instruction = instruction.strip()
    if instruction == "noop":
        drawnScreen = updateScreen(cycle, X, drawnScreen)
        cycle += 1
        interestingCycleSum = updateInterestingCycle(cycle, X, interestingCycleSum)
    else:
        drawnScreen = updateScreen(cycle, X, drawnScreen)
        cycle += 1
        interestingCycleSum = updateInterestingCycle(cycle, X, interestingCycleSum)
        drawnScreen = updateScreen(cycle, X, drawnScreen)
        cycle += 1
        interestingCycleSum = updateInterestingCycle(cycle, X, interestingCycleSum)
        X += int(instruction.split(" ")[1])

print(interestingCycleSum)
print(drawnScreen)
