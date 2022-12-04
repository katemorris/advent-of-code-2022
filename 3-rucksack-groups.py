import string

value = 0
alpha = list(string.ascii_letters)
index = 0
with open("inputs/3.txt", "r") as file:
    sacks = file.readlines()
print(f"Sacks are: {sacks}")
while index < len(sacks):
    print(f"At set {index}/{len(sacks)}")

    unique_letters = [list(set(sack.strip())) for sack in sacks[(index) : (index + 3)]]
    print(f"Unique sacks are: {unique_letters}")

    for letter in unique_letters[0]:
        if letter in unique_letters[1] and letter in unique_letters[2]:
            print(letter)
            value += alpha.index(letter) + 1
    index += 3
print(value)
