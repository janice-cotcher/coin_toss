# demonstration of experimental probability with a coin toss
# adapted from https://www.pythonforbeginners.com/code-snippets-source-code/game-rolling-the-dice/
import random

# toss a coin n_max times and store the tosses in a list
min = 1
max = 2
n = 1
rolls = []
while True:
    max_n = int(input("How many times do you want to toss the coin? "))
    try:
        while n <= max_n:
            x = random.randint(min, max)
            rolls.append(x)
            n += 1
        break
    except ValueError:
        print("Invalid choice, try again.")

# count the number of times each number appears in n_max tosses append
# and calculate the percent
for y in range(1, 3):
    percent = rolls.count(y) * 100 / max_n
    if y == 1:
        print(f"The number of times HEADS was rolled: {rolls.count(y)}")
        print(f"The percent of times HEADS was rolled: {percent}")
    else:
        print(f"The number of times TAILS was rolled: {rolls.count(y)}")
        print(f"The percent of times TAILS was rolled: {percent}")
    print("\n")
