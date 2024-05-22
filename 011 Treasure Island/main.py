print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


# Initialize a flag to control the game loop
should_continue = True
# Message to display when the game is over
msg = "Game Over."

# Start the game loop
while should_continue:

    # Prompt the user for their first choice at the crossroad
    choice = input("You're at crossroad. Want to go left or right? ").lower()

    # If the choice is "right", the game ends
    if choice == "right":
        print(msg)
        should_continue = False  # Set the flag to False to end the game

    else:  # If the choice is not "right", proceed to the next choice
        choice = input("Do you want to swim or wait for a boat? ").lower()

        # If the choice is "swim", the game ends
        if choice == "swim":
            print(msg)
            should_continue = False  # Set the flag to False to end the game

        else:  # If the choice is not "swim", proceed to the next choice
            choice = input("Which door do you want to enter? 'red', 'blue', 'yellow'? ").lower()
            # If the choice is "yellow", the player wins
            if choice == "yellow":
                print(f"{choice} is the right path. You win! \n")
                should_continue = False  # Set the flag to False to end the game

            else:  # If the choice is not "yellow", the game ends
                print(msg)
