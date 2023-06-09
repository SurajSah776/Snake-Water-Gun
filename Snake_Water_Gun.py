# Snake Water Gun
'''Snake, Water and Gun is a variation of the children's game "rock- paper-scissorsii where players use hand gestures to represent a snake, water, or a gun. 
        *** Rules: ***
-->The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements.
Do not create any fancy GUI. Use proper functions to check for win.'''


import random

# Emulating do while loop
while True:
    print()
    print("***** Snake Water Gun *****".center(30))
    print()

    # Taking user Input
    print(" S - Snake \n W - Water \n G - Gun")
    userInput = input("Enter your choice (S, W or G): ")

    # Converting user input to upper case
    user = userInput.upper()

    # Validating the input
    if (user == "S") or (user == "W") or (user == "G"):
        print()

        # Computer Choosing Randomly
        options = ["S", "W", "G"]
        index = random.randint(0, 2)
        computer = options[index]

        # Checking the Winner
        print("-----------------------------------")
        print(f"You      : {user}")
        print(f"Computer : {computer}")
        print()

        if (user == "G" and computer == "S") or (user == "W" and computer == "G") or (user == "S" and computer == "W"):
            print("*** Congratulations !! You Won ***".center(30))

        elif (user == "G" and computer == "G") or (user == "W" and computer == "W") or (user == "S" and computer == "S"):
            print("*** Game Tied !! ***".center(20))

        else:
            print("*** You Lose !! ***".center(20))

        print("-----------------------------------")

        # Asking the user if he/she wants to play again
        print()
        more = input("Do you want to play again (y/n) ?: ")

        # Validating the user Input
        if more.upper() == "Y":
            continue
        elif more.upper() == "N":
            print("Thanks for playing".center(30))
            break
        else:
            print("Invalid Input")
            break

    else:
        print("Invalid Input")
        break
