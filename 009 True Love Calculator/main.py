print("Welcome to the True Love Calculator app! \n")

# Prompt the user for their name and their lover's name
your_name = input("What is your name? ")
lover_name = input("What is your lover's name? ")

# Combine both names and convert to lowercase to ensure case insensitivity
combined_names = (your_name + lover_name).lower()

# Count occurrences of specific letters in the combined names for "TRUE" calculation
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

# Sum the counts to form the first digit of the score
first_digit = t + r + u + e

# Count occurrences of specific letters in the combined names for "LOVE" calculation
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

# Sum the counts to form the second digit of the score
second_digit = l + o + v + e

# Combine the first and second digits to form the final score
score = int(str(first_digit) + str(second_digit))

# Determine the message based on the score
if (score > 90) or (score < 10):  # If the score is either greater than 90 or less than 10
    print(f"Your score is {score}, you are dying for each other.")
elif (score >= 40) and (score <= 90):  # If the score is between 40 and 90, inclusive
    print(f"Your score is {score}, you're alright together.")
else:  # For all other scores
    print(f"Your score is {score}. I am sorry to have to tell you this, but you should give up on your lover.")
