import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

# Get user choice safely
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors. "))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
else:
    # Get computer choice
    random_number = random.randint(0, 2)
    computer_choice = game[random_number]

    # Print choices
    print(f"User's choice: {game[user_choice]}")
    print(f"Computer's choice: {computer_choice}")

    # Determine and print the result
    if user_choice == random_number:
        print("It's a draw.")
    elif (user_choice == 0 and random_number == 2) or (user_choice == 1 and random_number == 0) or (user_choice == 2 and random_number == 1):
        print("The user wins.")
    else:
        print("The computer wins.")
