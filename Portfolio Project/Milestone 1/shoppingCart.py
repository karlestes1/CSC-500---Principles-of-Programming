# Milestone 1 for CSC500 Portfolio Project
# Created by Karl Estes
# Created: Tuesday, October 6th, 2020

# This milestone program prompts the user to enter two item names, prices, and quantities of the items
# It then outputs the information and the cost of the two items

# I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
# to allow for quick navigation around the file by creating sections and anchor points. Any use
# of "ANCHOR", "TODO", "FIXME", "STUB", "NOTE", "REVIEW", "SECTION", and "LINK" are used in conjunction with 
# this extension

#Import Statements 
from os import system, name

#!SECTION

#SECTION - ItemToPurchase class

class ItemToPurchase:

    # Default Constructor
    def __init__(self):
        self.name = 'none'
        self.price = 0.0
        self.quantity = 0

    # Methods

    # Prints out the current cost of the item
    def printItemCost(self):
        print(self.quantity, self.name, "@ ${:.2f} = ${:.2f}".format(self.price, (self.price * self.quantity)))


#!SECTION

#SECTION - Program Functions
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

    print("   _           ")
    print(r"    \________   ____  _  _   __  ____  ____  __  __ _   ___     ___   __   ____  ____ ")
    print(r" ~   \######/  / ___)/ )( \ /  \(  _ \(  _ \(  )(  ( \ / __)   / __) / _\ (  _ \(_  _)")      
    print(r"  ~   |####/   \___ \) __ ((  O )) __/ ) __/ )( /    /( (_ \  ( (__ /    \ )   /  )(  ")
    print(r" ~    |____.   (____/\_)(_/ \__/(__)  (__)  (__)\_)__) \___/   \___)\_/\_/(__\_) (__) ")
    print("      o    o   \n")
    print("Developed by Karl Estes")
    print("Created as per Portfolio Milestone 1 instructions in CSC 500 at CSUG\n\n")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")


def getItemDetails():
    """
    Prompts the user to fill out an items details and returns the completed item at the end
    """

    # Variables
    newItem = ItemToPurchase()
    valid = False # Used to check if input is valid

    # Prompt the user for info
    newItem.name = input('Please enter an item name as you want it to appear: ')

    print('Please enter the price of', newItem.name,  'in USD: $', end='')
    newPrice = input()

    # Loop until valid input is reached
    while not valid:
        try:
            newItem.price = float(newPrice)
            valid = True
        except ValueError:
            print('(Invalid Input) Please enter the price of', newItem.name,  'in USD: $', end='')
            newPrice = input()

    valid = False
    print('Please enter the quantitiy of', newItem.name, ': ', end='')
    newQuantity = input()

    # Loop until valid input is reached
    while not valid:
        try:
            newItem.quantity = int(newQuantity)
            valid = True
        except ValueError:
            print('(Invalid Input) Please enter the quantitiy of', newItem.name, ': ', end='')
            newQuantity = input()

    return newItem

#!SECTION

# SECTION - Main

if __name__ == "__main__":

    welcomeMessage()

    print("---First Item---")
    item1 = getItemDetails()
    print('\n---Second Item---')
    item2 = getItemDetails()

    totalItem1 = item1.price * item1.quantity
    totalItem2 = item2.price * item2.quantity
    
    print("\n\n* * * * * * * * * * * * * *")
    print("        Total Cost\n")
    item1.printItemCost()
    item2.printItemCost()
    print("\nTotal = ${:.2f}".format(((item1.price * item1.quantity) + (item2.price * item2.quantity))))



#!SECTION
# %%
