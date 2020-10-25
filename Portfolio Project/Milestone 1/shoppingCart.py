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


#%% ItemToPurchase class

class ItemToPurchase:

    # Default Constructor
    def __init__(self):
        self.name = 'none'
        self.price = 0.0
        self.quantity = 0

    # Methods
    '''
    Will print out the current cost of the item
    '''
    def printItemCost(self):
        print(self.price)

#%%% Extra Functions
