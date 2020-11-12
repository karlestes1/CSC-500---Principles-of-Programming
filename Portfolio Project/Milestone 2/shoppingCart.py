# Milestone 2 for CSC500 Portfolio Project
# Created by Karl Estes
# Created: Tuesday, October 6th, 2020

# This milestone program simulates shopping - but virtually. The user is able to add or removes item from a cart,
# modify item traits (i.e. description, price, quantity), and view current items in the cart. The view modes are
# available: one allows you to view all of the items and their descriptions, and the other will show item cost and
# quantity, and it will output the total cose of the shopping cart

# I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
# to allow for quick navigation around the file by creating sections and anchor points. Any use
# of "ANCHOR", "TODO", "FIXME", "STUB", "NOTE", "REVIEW", "SECTION", and "LINK" are used in conjunction with 
# this extension

# SECTION - Imports, Constants, and Globals

#Import Statements 
from os import system, name
from datetime import datetime

# REVIEW - Look into adding color messages like other programs
# NOTE - Perhaps this is a final milestone feature?

# !SECTION

#SECTION - Classes

# REVIEW - Consider adding confirmation outputs to each function

class ItemToPurchase:

    # Default Constructor
    def __init__(self, name="none", description="", price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # Methods

    def printItemCost(self):
        '''
        Outputs the item name, quantitiy, and cost to the console
        '''
        print(self.quantity, self.name, "@ ${:.2f} = ${:.2f}".format(self.price, (self.price * self.quantity)))

    def printItemDescriptions(self):
        '''
        Outputs the item name and description to the console
        '''
        print(self.name + ': ' + self.description)
    

class ShoppingCart:

    # Constructor
    def __init__(self, customerName="none", date="January 1, 2020"):
        self.customerName = customerName
        self.curDate = date
        self.itemsInCart = []

    # Methods

    def addItem(self, itemToPurchase):
        '''
        Adds the passed item to cartItems list
        '''
        self.itemsInCart.append(itemToPurchase)
    
    def removeItem(self, itemName):
        '''
        Takes the name of an item and searches for it in the cart

        If the item is found, removes it from the cart, otherwise, outputs message stating no item could be found
        '''
        itemRemoved = False

        for item in self.itemsInCart:

            # Check if the item is in the list
            if itemName == item.name:
                self.itemsInCart.remove(item)
                itemRemoved = True
                break

        if itemRemoved:
            print("Sucessfully removed " + itemName + " from your cart")
        else:
            print("Could not find " + itemName + "in your cart. Nothing was removed")
        



    def modifyItem(self, itemName):
        '''
        Modifies an items description, price, and/or quantity

        Searches for an item by name in the cart and will prompt for what peices to modify

        If item cannot be found, outputs a message stating as such and nothing wil lbe modified
        '''
        
        itemFound = False

        # Check to make sure item is in the list
        for item in self.itemsInCart:
            if itemName == item.name:
                itemFound = True

                print("Modify Menu")
                print("n = Item Name")
                print("d = Item Description")
                print("p = Item Price")
                print("q = Item Quantity")
                print("c = Current Item Values")
                print("e = exit modification")

                # Loop for modificaiton of item
                while True:
                    print(custName + "@ShoppingCart (Modify) >> ", end="")
                    userInput = input()

                    userInput = userInput.lower()

                    if userInput == "n": # Change the item name
                        print("(Current: " + item.name + ") Please enter a new item name", end="\n>> ")
                        newName = input()

                        # REVIEW consider putting confirmation here
                        item.name = newName
                        print("Item is now called " + newName)
                    elif userInput == "d":
                        print("(Current: " + item.description + ") Please enter a new item description", end="\n>> ")
                        newDescription = input()
                        
                        # REVIEW consider putting confirmation here
                        item.description = newDescription
                        print(item.name + " description is now " + newDescription)
                    elif userInput == "p":
                        print("(Current: ${:.2f})".format(item.price) + " Please enter a new item price", end="\n>> $")
                        userInput = input()

                        try:
                            newPrice = float(userInput)
                            item.price = newPrice
                            print("New item price is {:.2f}".format(newPrice))
                        except ValueError:
                            print("Invalid price entered. Please attempt modification again ")
                        
                    elif userInput == "q":
                        print("(Current: {})".format(item.quantity) + " Please enter a new item quantity", end="\n>> ")
                        userInput = input()

                        try:
                            newQuant = int(userInput)
                            item.quantity = newQuant
                            print("New item quantitity is {}".format(newQuant))
                        except ValueError:
                            print("Invalid quantitity entered. Please attempt modification again ")
                    elif userInput == "c":
                        print("Current Item details")
                        print("Name: " + item.name)
                        print("Description: " + item.description)
                        print("Price: {:.2f}".format(item.price))
                        print("Quantity: {}".format(item.quantity))
                    elif userInput == "e":
                        break

                    print("\n")
                break

        if not itemFound:
            print("Could not find " + itemName + " in your cart")

                


    def getNumItemsInCart(self):
        '''
        Returns the quantity of all items in the cart
        '''
        itemCount = 0

        for item in self.itemsInCart:
            itemCount = itemCount + item.quantity
        
        return itemCount

    def getCostOfCart(self):
        '''
        Calculates the total cost of all items in the cart and returns that amount
        '''
        totalCost = 0.0

        for item in self.itemsInCart:
            totalCost = totalCost + (item.price * item.quantity)

        return totalCost

        
    
    def printTotal(self):
        '''
        Outputs the total of objects in the cart

        If the cart is empty, outputs a message stating as such
        '''

        print(self.customerName + "'s Shopping Cart - " + self.curDate)
        print("Number of Items in Cart: " + str(self.getNumItemsInCart()))
        
        # Print all item costs
        for item in self.itemsInCart:
            item.printItemCost()

        print("Total: ${:.2f}".format(self.getCostOfCart()))

    def printDescriptions(self):
        '''
        Outputs each item's description
        '''

        print(self.customerName + "'s Shopping Cart - " + self.curDate)
        print("Item Descriptions")
        
        for item in self.itemsInCart:
            item.printItemDescriptions()


#!SECTION

#SECTION - Program Functions
def welcomeMessage():
    """
    Prints a welcome message when the program starts

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
    print("Created as per Portfolio Milestone 2 instructions in CSC 500 at CSUG\n\n")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")

def getItemDetails():
    """
    Prompts the user to fill out an items details and returns the completed item at the end
    """

    valid = False # Used to check if input is valid

    # Prompt the user for info
    print("Please enter the name of the item", end="\n>> ")
    itemName = input()

    print("Please enter an item description (Leave blank if there is none)", end="\n>> ")
    itemDescription = input()
    

    print('How much does ' + itemName + ' cost?', end='\n>> (USD)$')
    newPrice = input()

    # Loop until valid input is reached
    while not valid:
        try:
            itemPrice = float(newPrice)
            valid = True
        except ValueError:
            print('(Invalid Input) How much does ' + itemName + ' cost?', end='\n>> (USD)$')
            newPrice = input()

    valid = False
    print('How many ' + itemName + ' are you purchasing?', end="\n>> ")
    newQuantity = input()

    # Loop until valid input is reached
    while not valid:
        try:
            itemAmount = int(newQuantity)
            valid = True
        except ValueError:
            print('(Invalid Input) How many ' + itemName + ' are you purchasing?', end="\n>> ")
            newQuantity = input()

    return ItemToPurchase(itemName, itemDescription, itemPrice, itemAmount)

def printCommands():
    '''
    Outputs a menu with all of the available options for the program
    '''

    print("\n*** Program Commands ***")
    print("a - add item to cart")
    print("r - remove item from cart")
    print("c - change/modify an item")
    print("i - output items' descriptions")
    print("o - output shopping cart")
    print("q - quit")
    print("? - print menu options")

def getCustomerName():
    '''
    Prompts the customer for their name, verifies it's a proper input, and returns the name
    '''
    finalAnswer = False
    inputLoop = True

    print("What is your name?", end="\n>> ")
    name = input()

    while not finalAnswer:
        if name == "":
            print("Can you please type your name again?", end="\n>> ")
            name = input()
        else:
            inputLoop = True
            while inputLoop:
                print("Is " + name + " correct? (Enter y for yes or n for no)", end="\n>> ")
                userChoice = input()

                if userChoice == "y" or userChoice == "yes":
                    finalAnswer = True
                    inputLoop = False
                elif userChoice == "n" or userChoice == "no":
                    inputLoop = False
                    name = ""
                else:
                    print("I didn't understand your choice. Please try again")
        
    return name

def printMenu(cart):
    '''
    Print menu will handle the command flow for the program. It is called printMenu as per the assignment instructions

    It will handle printing the menu, taking user input, and calling the necessary functions

    Takes a shopping cart object as a parameter
    '''


    while True:
        print(cart.customerName + "@ShoppingCart >> ", end="")
        userInput = input()

        userInput = userInput.lower()

        if userInput == "a":
            newItem = getItemDetails()
            cart.addItem(newItem)
        elif userInput == "r":
            print("Please enter the name of the item you'd like to remove from your cart", end="\n>> ")
            userInput = input()

            cart.removeItem(userInput)
        elif userInput == "c":
            print("Please enter the name of the item in your cart you'd like to modify", end="\n>> ")
            userInput = input()

            cart.modifyItem(userInput)
        elif userInput == "i":
            cart.printDescriptions()
        elif userInput == "o":
            cart.printTotal()
        elif userInput == "q":
            exit(0)
        elif userInput == "?":
            printCommands()
        
        print("\n")



#!SECTION

# SECTION - Main

if __name__ == "__main__":

    # Get customer name and current date to create shopping cart
    now = datetime.now()
    curDate = now.strftime("%B %d, %Y")

    welcomeMessage()

    custName = getCustomerName()

    cart = ShoppingCart(custName, curDate)

    
    print(f"\nWelcome {custName}!")
    printCommands()
    print("\n***** Begin Shopping *****\n")

    # Handle input
    
    printMenu(cart)

#!SECTION
# %%
