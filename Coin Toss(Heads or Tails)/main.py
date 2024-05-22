print("Welcome to the Coin Toss program! \n")

import random

toss = random.randint(0, 1)


if toss == 1:
    msg = "heads"
else:
    msg = "tails"

print(f"It is {msg.title()}")