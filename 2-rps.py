decode = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

game = {
    "rock": {"points": 1, "beats": "scissors"},
    "paper": {"points": 2, "beats": "rock"},
    "scissors": {"points": 3, "beats": "paper"},
}

with open("inputs/2.txt", "r") as games:
    points = 0
    for set in games.readlines():
        them, you = set.split()
        # print(f"Them: {them}\nYou: {you}")
        them = decode[them]
        you = decode[you]
        # print(f"Them: {them}\nYou: {you}")
        points += game[you]["points"]
        # print(f"Played points added: {points}")
        if you == them:
            points += 3
        elif game[you]["beats"] == them:
            points += 6
        elif game[them]["beats"] == you:
            points += 0
        # print(f"Post game points added: {points}")
    print(points)
