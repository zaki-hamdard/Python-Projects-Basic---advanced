# Welcome message for the user.
print('Welcome to the Highest Score Finder app! \n')

# Prompt user for a comma-separated list of scores and convert them to integers.
get_input = input("Enter the numbers, separating them with a comma and a space. ")
numbers = [int(number) for number in get_input.split(", ")]

# Initialize the variable to store the maximum number.
max_number = 0  # Assumes non-negative numbers; consider using min(numbers) if negatives are expected.

# Iterate through the list to find the highest score.
for item in numbers:
    if item > max_number:
        max_number = item

# Output the highest score found.
print(f"The highest number is {max_number}")
