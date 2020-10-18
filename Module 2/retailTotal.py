# Python Program to calculate the retail total of a few items
# Created by Karl Estes
# Created: Tuesday, October 6th, 2020

# This program prompts a customer for the price of five different items, them displays the subtotal
# of the sale, the amount of sales tax, and the total.

# I am using the Python extension for Visual Studio Code which includes the ability to create python cells 
# which can be individually run in an interactive window. 
# The syntax to create a cell is as follows: #%%
# Any line with these three characters on it denotes the beginning of a 
# python cell and is included due to the utilization of the python extension. 

from os import system, name

#%% Welcome Message
'''
Prints a welcome message when the program starts
Also clears the console on program start
'''
def welcomeMessage():

    # For windows
    if name == 'nt':
        _ = system('cls')
    # Mac and linux 
    else:
        _ = system('clear')

    print("   _          ")
    print("    \________      ____       __        _ __   ______      __        __")
    print(" ~   \######/     / __ \___  / /_____ _(_) /  /_  __/___  / /_____ _/ /")      
    print("  ~   |####/     / /_/ / _ \/ __/ __ `/ / /    / / / __ \/ __/ __ `/ / ")
    print(" ~    |____.    / _, _/  __/ /_/ /_/ / / /    / / / /_/ / /_/ /_/ / /  ")
    print("      o    o   /_/ |_|\___/\__/\__,_/_/_/    /_/  \____/\__/\__,_/_/   \n")
    print("Developed by Karl Estes")
    print("Created as per Module 2 instructions in CSC 500 at CSUG\n\n")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")

#%% Validate Input
'''
- Takes a user input and converts it to an int or float
- A price must be an integer or float
- Will return the value as a float or -1.0 if error
'''
def convertInput(userInput):
    try:
        price = int(userInput)
        price = float(price)
    except ValueError:
        try:
            price = float(userInput)
        except ValueError:
            price = -1.0
    
    return price

#%% Output Results
'''
- Takes an array of prices, calculates the subtotal of the sale, and applies tax
- Outputs formatted results to the screen
'''
def outputResults(prices):

    # Do math
    subtotal = sum(prices)
    total = subtotal * 1.07

    # Print results
    print("\n\n* * * * * * * * * * * * * *")
    print("      Receipt      ")
    for i in range(5):
        print(" Item", i+1, "cost", "${:.2f} ".format(prices[i]))
    print(" - - - - - - - - - - - -")
    print(" Subtotal =", "${:.2f}  ".format(subtotal))
    print(" Sales Tax = 7%    ")
    print(" Total =", "${:.2f}     ".format(total))
    print("* * * * * * * * * * * * * *")
   

#%% Main Function
def main():

    welcomeMessage()

    # Array which will hold the prices
    prices = []

    # Prompt user for enough prices
    i = 0
    valid = True
    while i < 5 :

        # Prompt User
        if valid :
            print("\rPlease enter a price for Item", i+1, ": $", end='')
            price = convertInput(input())
        else:
            print("(Invalid Input) Please enter a new price for Item", i+1, ": $", end='')
            price = convertInput(input())

        # is Valid?
        valid = (False if price < 0 else True)

        if valid:
            prices.append(price)
            i = i + 1

    # Calculate and display result
    outputResults(prices)



#%% Run Program
if __name__ == "__main__":
    main()
