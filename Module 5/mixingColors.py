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
RED = "\u001b[38;5;196m"
BLUE = "\u001b[38;5;21m"
YELLOW = "\u001b[38;5;226m"
GREEN = "\u001b[38;5;34m"
ORANGE = "\u001b[38;5;209m"
PURPLE = "\u001b[38;5;165m"
BOLD = "\u001b[38;5;15m"
RESET = "\u001b[0m"

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
        elif lowString == "yellow":
            return 2
        elif lowString == "blue":
            return 3
        elif lowString == "q" or lowString == "quit":
            return 0
        elif lowString == "?":
            return 4
        else:
            return -1
    except ValueError:
        return -1

def mixColors(colors):
    '''
    Input should be a list of integers corresponding to what colors will be mixed\n
    List should contain no more than two entires, and the resulting color will printed to the screen
    '''

    # If not enough colors, an error has occured
    if len(colors) < 2:
        print("Error has occured. Cannot mix less than 2 colors")
    else:
        if (colors[0] == 1 and colors[1] == 1):
            print("Mixing " + RED + "red" + RESET +" and " + RED + "red" + RESET + " results in " + RED + "red" + RESET)
        elif (colors[0] == 2 and colors[1] == 2):
            print("Mixing " + YELLOW + "yellow" + RESET + " and " + YELLOW + "yellow" + RESET + " results in "+ YELLOW + "yellow" + RESET)
        elif colors[0] == 3 and colors[1] == 3:
            print("Mixing " + BLUE + "blue" + RESET + " and " + BLUE + "blue" + RESET + " results in " + BLUE + "blue" + RESET)
        elif (colors[0] == 1 and colors[1] == 2) or (colors[1] == 1 and colors[0] == 2):
            print("Mixing " + RED + "red" + RESET + " and " + YELLOW + "yellow" + RESET + " results in " + ORANGE + "orange" + RESET)
        elif (colors[0] == 1 and colors[1] == 3) or (colors[1] == 3 and colors[0] == 1):
            print("Mixing " + RED + "red" + RESET + " and " + BLUE + "blue" + RESET + " results in " + PURPLE + "purple" + RESET)
        elif (colors[0] == 2 and colors[1] == 3) or (colors[0] == 3 and colors[1] == 2):
            print("Mixing " + BLUE + "blue" + RESET + " and " + YELLOW + "yellow" + RESET + " results in " + GREEN + "green" + RESET)
        else:
            print("huh?")

def welcomeMessage():
    """
    Prints a welcome message when the program starts\n
    Also clears the console on program start
    """

    # For windows
    if name == 'nt':
        _ = system('cls')
    # Mac and linux 
    else:
        _ = system('clear')

    # Font (Small Slant) for title generated from Text to ASCII Art Generator on patorjk.com
    print(BOLD)
    print(r"   __  ____       _             _____     __           ")
    print(r"  /  |/  (_)_ __ (_)__  ___ _  / ___/__  / /__  _______")
    print(r" / /|_/ / /\ \ // / _ \/ _ `/ / /__/ _ \/ / _ \/ __(_-<")
    print(r"/_/  /_/_//_\_\/_/_//_/\_, /  \___/\___/_/\___/_/ /___/")
    print(r"                      /___/                            ")
    print("Developed by Karl Estes")
    print("Created as per Portfolio Milestone 2 instructions in CSC 500 at CSUG\n\n")
    print("You may type q or quit at any point to exit this program")
    print("You may type ? at any point to see a list of primary colors")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n" + RESET)
    


# !SECTION

# SECTION - Main

if __name__ == "__main__":
    exitProg = False
    validInput = True
    colors = []
    colorNames = []

    welcomeMessage()

    while exitProg is False:
        userInput = ''
        
        # Get user input
        
        print("(" + BOLD + "Selected Color: " + RESET, end="")
        for color in colorNames:
            print(color, end=" ")

        if validInput is True:
            print(") Please enter a primary color\n", end=BOLD + ">> ")        
            userInput = input()
        else:
            print(") (Invalid Input) Please enter a primary color\n", end=BOLD + ">> ")
            userInput = input()
        
        # Process input
        check = handleInput(userInput)
        
        if check == -1:
            validInput = False
        elif check == 0:
            exitProg = True
        elif check >= 1 and check <= 3:
            colors.append(check)

            if check == 1:
                colorNames.append(RED + "red" + RESET)
            elif check == 2:
                colorNames.append(YELLOW + "yellow" + RESET)
            elif check == 3:
                colorNames.append(BLUE + "blue" + RESET) 
        elif check == 4:
            print("\n*** The primary colors " + RED + "red" + BOLD + ", " + YELLOW + "yellow" + BOLD + ", and " + BLUE + "blue" + BOLD + " ***\n")
        else:
            print("Invalid check value")


        if len(colors) == 2:
            print(BOLD + "\nMixing colors..." + RESET)
            mixColors(colors)
            exitProg = True


# !SECTION
    