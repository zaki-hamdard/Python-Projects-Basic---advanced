# Import the random module
import random
import hangman_words
import hangman_art

print(hangman_art.logo)
# Create a list of words
word_list = hangman_words.word_list

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize blanks for the letters of the chosen word
blanks = []

for letter in chosen_word:
    blanks.append("_")

# The game continues as long as there is an "_" in the blanks list
lives = 6

while "_" in blanks:
    # Prompt the user to guess a letter
    guess = input("Guess a letter: ")

    # Inform the user if the guessed letter was already chosen
    if guess in blanks:
        print(f"You have already guessed '{guess}'. Please try a different letter.")       

    # Check if the guessed letter is in the chosen word
    for i in range(word_length):
        if guess == chosen_word[i]:
            blanks[i] = guess

    # If the guessed letter is not in the chosen word, reduce lives by 1
    if guess not in chosen_word: 
        print("Wrong guess, you lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lose.")
            break

    # Check if the user has guessed all letters correctly
    if not "_" in blanks:
        print("Congratulations, you won!")            
    print(blanks)
