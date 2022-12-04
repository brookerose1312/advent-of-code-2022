## Part 1

# Read input
with open("day2input.txt") as f:
    games = f.readlines()

# Read strategies and generate score

playedScore = {"R": 1, "P": 2, "S": 3}

outcomeScore = {"L": 0, "D": 3, "W": 6}

opponentDecode = {
    "A": "R",
    "B": "P",
    "C": "S",
}

playerDecode = {"X": "R", "Y": "P", "Z": "S"}

score = 0


def findOutcome(playerThrow, opponentThrow):
    if playerThrow == opponentThrow:
        return "D"
    elif playerThrow == "R":
        if opponentThrow == "S":
            return "W"
        else:
            return "L"
    elif playerThrow == "P":
        if opponentThrow == "R":
            return "W"
        else:
            return "L"
    elif playerThrow == "S":
        if opponentThrow == "P":
            return "W"
        else:
            return "L"
    return "L"


for game in games:
    playerThrow = playerDecode[game[2]]
    opponentThrow = opponentDecode[game[0]]
    outcome = findOutcome(playerThrow, opponentThrow)
    score += playedScore[playerThrow] + outcomeScore[outcome]

## Part 2

part2PlayerDecode = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}

part2Score = 0


def findThrown(outcome, opponentThrow):
    if outcome == "D":
        return opponentThrow
    elif outcome == "W":
        if opponentThrow == "R":
            return "P"
        elif opponentThrow == "P":
            return "S"
        else:
            return "R"
    elif outcome == "L":
        if opponentThrow == "R":
            return "S"
        elif opponentThrow == "P":
            return "R"
        else:
            return "P"


for game in games:
    outcome = part2PlayerDecode[game[2]]
    opponentThrow = opponentDecode[game[0]]
    playerThrow = findThrown(outcome, opponentThrow)
    part2Score += playedScore[playerThrow] + outcomeScore[outcome]

print(f"Part 1 score: {score}")
print(f"Part 2 score: {part2Score}")
