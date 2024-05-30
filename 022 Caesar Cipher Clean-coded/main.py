# List containing the alphabet twice to handle shifts beyond 'z'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo  # Import the logo from the art module
print(logo)  # Print the logo

should_continue = True  # Initialize a flag to control the loop
while should_continue:
    # Prompt the user to choose between encoding and decoding
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Prompt the user to input the message and convert it to lowercase
    text = input("Type your message:\n").lower()
    # Prompt the user to input the shift number and convert it to an integer
    shift = int(input("Type the shift number:\n"))

    # Define the Caesar cipher function
    def caesar(start_text, shift_amount, text_direction):
        end_text = ""  # Initialize an empty string for the result

        # If the direction is decode, reverse the shift amount
        if text_direction == "decode":
            shift_amount *= -1

        # Iterate over each character in the input text
        for char in start_text:
            # Check if the character is in the alphabet list
            if char in alphabet:
                position = alphabet.index(char)  # Find the position of the character
                new_position = position + shift_amount  # Calculate the new position
                end_text += alphabet[new_position]  # Append the new character to the result
            else:
                end_text += char  # If the character is not in the alphabet, keep it as is

        # Print the final encoded or decoded text
        print(f"The {text_direction}d text is {end_text}")

    # Adjust the shift to ensure it is within the range of the alphabet length
    shift = shift % 26
    # Call the Caesar cipher function with the provided inputs
    caesar(start_text=text, shift_amount=shift, text_direction=direction)

    # Ask the user if they want to go again
    ask = input("If you want to go again, type 'yes' otherwise type 'no': ").lower()
    # If the user types 'no', end the loop
    if ask == "no":
        should_continue = False
        print("Goodbye!")  # Print a goodbye message
