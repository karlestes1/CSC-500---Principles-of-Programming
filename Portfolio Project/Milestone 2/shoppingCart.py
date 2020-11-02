# Milestone 2 for CSC500 Portfolio Project
# Created by Karl Estes
# Created: Tuesday, October 6th, 2020

# TODO update this description
# This milestone program prompts the user to enter two item names, prices, and quantities of the items
# It then outputs the information and the cost of the two items

# I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
# to allow for quick navigation around the file by creating sections and anchor points. Any use
# of "ANCHOR", "TODO", "FIXME", "STUB", "NOTE", "REVIEW", "SECTION", and "LINK" are used in conjunction with 
# this extension

#Import Statements 
from os import system, name

#SECTION - Classes

class ItemToPurchase:

    # Default Constructor
    def __init__(self, name="none", description="", price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # Methods

    # Prints out the current cost of the item
    def printItemCost(self):
        print(self.quantity, self.name, "@ ${:.2f} = ${:.2f}".format(self.price, (self.price * self.quantity)))

class ShoppingCart:

    # Constructor
    def __init__(self, customerName="none", date="January 1, 2020"):
        self.customerName = customerName
        self.curDate = date
        self.cartItems = []

    # Methods

    # TODO actually write functions
    def addItem(self, itemToPurchase):
        '''
        Adds the passed item to cartItems list
        '''
    
    def removeItem(self, itemName):
        '''
        Takes the name of an item and searches for it in the cart\n
        If the item is found, removes it from the cart, otherwise, outputs message stating no item could be found
        '''

    def modifyItem(self, itemToModify):
        '''
        Modifies an items description, price, and/or quantity\n
        Searches for an item by name in the cart and will prompt for what peices to modify\n
        If item cannot be found, outputs a message stating as such and nothing wil lbe modified
        '''

    def getNumItemsInCart(self):
        '''
        Returns the quantity of all items in the cart
        '''

    def getCostOfCart(self):
        '''
        Calculates the total cost of all items in the cart and returns that amount
        '''
    
    def printTotal(self):
        '''
        Outputs the total of objects in the cart
        If the cart is empty, outputs a message stating as such
        '''

    def printDescriptions(self):
        '''
        Outputs each item's description
        '''

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
