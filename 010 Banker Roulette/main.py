import random

print("Welcome to the Banker Roulette app! It determines who will pay the bill... \n")

# Prompt the user to enter names, separating them with a comma and a space.
get_name = input("Enter the names, separating them with a comma and a space: ")

# Split the input string into a list of names based on ", "
names = get_name.split(", ")

# Check if the list is not empty to avoid errors
if names:
    # Generate a random index to select a random name
    index = random.randint(0, len(names) - 1)

    # Retrieve the name at the random index
    bill_payer = names[index]

    print(f"{bill_payer} should pay the bill.\n")
    
else:
    print("No names were entered.")
