# Milestone 1 for CSC500 Portfolio Project
# Created by Karl Estes
# Created: Tuesday, October 6th, 2020

# This milestone program prompts the user to enter two item names, prices, and quantities of the items
# It then outputs the information and the cost of the two items

# I am using the Python extension for Visual Studio Code which includes the ability to create python cells 
# which can be individually run in an interactive window. 
# The syntax to create a cell is as follows: #%%
# Any line with these three characters on it denotes the beginning of a 
# python cell and is included due to the utilization of the python extension. 

#%% Import Statements


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
