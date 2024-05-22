import random

# Display a welcome message
print("Welcome to the Pypassword Generator! \n")

# List of alphabets
alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# List of symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}',
    '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?', '~', '`'
]

# List of numbers as strings for consistency in handling
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Get the desired inputs from user
letter_number = int(input("How many letters do you want the password to include? "))
symbol_number = int(input("And how many symbols? "))
how_many_numbers = int(input("And how many numbers? "))

# Create the password by extending the list with samples
raw_password = []
raw_password.extend(random.sample(alphabets, letter_number))
raw_password.extend(random.sample(symbols, symbol_number))
raw_password.extend(random.sample(numbers, how_many_numbers))

# Shuffle the password list to mix up the characters
random.shuffle(raw_password)

# Convert list to a string
final_password = ''.join(raw_password)
print("Generated Password:", final_password)
