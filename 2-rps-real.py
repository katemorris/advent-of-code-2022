# sure this is right
decode = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}
# sure this is right
game = {
    "rock": {"points": 1, "beats": "scissors"},
    "paper": {"points": 2, "beats": "rock"},
    "scissors": {"points": 3, "beats": "paper"},
}

with open("inputs/2.txt", "r") as games:
    points = 0
    for set in games.readlines():
        them, outcome = set.split()
        # print(f"Them: {them}\nOutcome: {outcome}")
        them = decode[them]
        outcome = decode[outcome]
        you = ""
        # print(f"Them: {them}\nOutcome: {outcome}")
        if outcome == "lose":
            points += 0
            you = game[them]["beats"]
        elif outcome == "draw":
            points += 3
            you = them
        elif outcome == "win":
            points += 6
            for key, value in game.items():
                if them == value["beats"]:
                    you = key
        # print(f"Them: {them}\nYou: {you}")
        # print(f"Game points added: {points}")
        points += game[you]["points"]
        # print(f"Played points added: {points}")

    print(points)
    # 10348 is not right, too high
