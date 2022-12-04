import string

value = 0
alpha = list(string.ascii_letters)
with open("inputs/3.txt", "r") as sacks:
    for sack in sacks.readlines():
        shared_letters = []
        half = int(len(sack) / 2)
        first_sack = sack[:half]
        second_sack = sack[half:]
        for letter in first_sack:
            if letter in second_sack and letter not in shared_letters:
                shared_letters.append(letter)
                value += alpha.index(letter) + 1

print(value)
