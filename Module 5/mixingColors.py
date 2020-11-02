# Option 2 CSC500 Module 5 - Mixing Colors 
# Created by Karl Estes
# Created: Monday, October 27th, 2020

# This program asks the user to enter the name of two primary colors.
# Once two primary color names are enteres, the color of of the resulting mix
# will be displayed.
# The program will continue to loop until two primary color names have been entered or the
# letter q or quit is typed to quit the program

# I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
# to allow for quick navigation around the file by creating sections and anchor points. Any use
# of "ANCHOR", "TODO", "FIXME", "STUB", "NOTE", "REVIEW", "SECTION", and "LINK" are used in conjunction with 
# this extension

# SECTION - Imports and variables
from os import system, name

# TODO color codes
# !SECTION

# SECTION - Functions

def handleInput(userInput):
    """
    Processes input from the console\n
    Returns -1 on error, 0 on quit, 1 on red, 2 on blue, and 3 on green
    """
    
    try:
        lowString = userInput.lower()
        
        if lowString == "red":
            return 1
        elif lowString == "green":
            return 2
        elif lowString == "blue":
            return 3
        elif lowString == "q" or lowString == "quit":
            return 0
        else:
            return -1
    except ValueError:
        return -1

# !SECTION

# SECTION - Main

if __name__ == "__main__":
    exitProg = False
    validInput = True
    colors = []

    # TODO - Welcome Message

    while exitProg is False:
        userInput = ''
        
        # Get user input
        # TODO print selected colors
        if validInput is True:
            print("(colors here) Please enter a primary color\n >> ", end='')        
            userInput = input()
        else:
            print("(colors here) (Invalid Input) Please enter a primary color\n>> ", end='')
            userInput = input()
        
        # Process input
        check = handleInput(userInput)
        
        if check == -1:
            validInput = False
        elif check == 0:
            exitProg = True
        elif check == 1 or check == 2 or check == 3:
            colors.append(check)
        else:
            print("Invalid check value")


        if len(colors) == 2:
            # TODO - mix Colors
            exitProg = True


# !SECTION
    