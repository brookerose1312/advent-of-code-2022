## Part 1

# Read input
with open("day2input.txt", "r", encoding="utf-8") as f:
    games = f.readlines()

# Read strategies and generate score

played_score = {"R": 1, "P": 2, "S": 3}

outcome_score = {"L": 0, "D": 3, "W": 6}

opponent_decode = {
    "A": "R",
    "B": "P",
    "C": "S",
}

player_decode = {"X": "R", "Y": "P", "Z": "S"}

score = 0


def find_outcome(incoming_player_throw, incoming_opponent_throw):
    """Finds the outcome of a match given a player throw and an opponent throw

    Args:
        incoming_player_throw (string): "R", "P", or "S", representing either
            rock, paper, or scissors
        incoming_opponent_throw (string): same as incoming_player_throw

    Returns:
        string: result of the game
    """
    if incoming_player_throw == incoming_opponent_throw:
        return "D"
    if incoming_player_throw == "R" and incoming_opponent_throw == "S":
        return "W"
    if incoming_player_throw == "P" and incoming_opponent_throw == "R":
        return "W"
    if incoming_player_throw == "S" and incoming_opponent_throw == "P":
        return "W"
    return "L"


for game in games:
    player_throw = player_decode[game[2]]
    opponent_throw = opponent_decode[game[0]]
    outcome = find_outcome(player_throw, opponent_throw)
    score += played_score[player_throw] + outcome_score[outcome]

## Part 2

part_two_player_decode = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}

part_two_score = 0


def find_thrown(incoming_outcome, incoming_opponent_throw):
    """Finds the player's thrown move based on the outcome of the game and the
        opponent's thrown move

    Args:
        incoming_outcome (string): the outcome of the game
        incoming_opponent_throw (_type_): either "R", "P", or "S", representing
            rock, paper, or scissors respectively

    Returns:
        string: the player's thrown move ("R", "P", or "S")
    """
    if incoming_outcome == "D":
        return incoming_opponent_throw
    if (incoming_outcome == "W" and incoming_opponent_throw == "R") or (
        incoming_outcome == "L" and incoming_opponent_throw == "S"
    ):
        return "P"
    if (incoming_outcome == "W" and incoming_opponent_throw == "P") or (
        incoming_outcome == "L" and incoming_opponent_throw == "R"
    ):
        return "S"
    return "R"


for game in games:
    outcome = part_two_player_decode[game[2]]
    opponent_throw = opponent_decode[game[0]]
    player_throw = find_thrown(outcome, opponent_throw)
    part_two_score += played_score[player_throw] + outcome_score[outcome]

print(f"Part 1 score: {score}")
print(f"Part 2 score: {part_two_score}")
