# List containing the alphabet twice to handle shifts beyond 'z'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Prompt the user to choose between encoding and decoding
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# Prompt the user to input the message and convert it to lowercase
text = input("Type your message:\n").lower()
# Prompt the user to input the shift number and convert it to an integer
shift = int(input("Type the shift number:\n"))

# Define the function to encrypt the message
def encrypt(shift, text):
    encoded_text = ""  # Initialize an empty string for the encoded text

    # Iterate over each letter in the input text
    for letter in text:
        # Find the current position of the letter in the alphabet list
        position = alphabet.index(letter)
        # Calculate the new position by adding the shift amount
        new_position = position + shift
        # Get the new letter from the alphabet list at the new position
        new_letter = alphabet[new_position]
        # Append the new letter to the encoded text
        encoded_text += new_letter

    # Print the encoded text
    print(f"Encoded text is: {encoded_text}")

# Define the function to decrypt the message
def decrypt(shift_amount, ciphered_text):
    decoded_text = ""  # Initialize an empty string for the decoded text

    # Iterate over each letter in the ciphered text
    for letter in ciphered_text:
        # Find the current position of the letter in the alphabet list
        position = alphabet.index(letter)
        # Calculate the new position by subtracting the shift amount
        new_position = position - shift_amount
        # Get the new letter from the alphabet list at the new position
        new_letter = alphabet[new_position]
        # Append the new letter to the decoded text
        decoded_text += new_letter

    # Print the decoded text
    print(f"Decoded text is {decoded_text}")

# Check if the user chose to encode or decode
if direction == "encode":
    # Call the encrypt function with the given shift and text
    encrypt(shift=shift, text=text)
else:
    # Call the decrypt function with the given shift and text
    decrypt(shift_amount=shift, ciphered_text=text)
