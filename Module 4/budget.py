# Option 2 CSC500 Portfolio Project - Budget Program
# Created by Karl Estes
# Created: Monday, October 26th, 2020

# This program asks the user to enter an amount they have budgeted for the month and then loops through
# a list of categories, prompting the user to enter their expenses in each category. When the program is
# finished, it lets the user know how over or under the budget they were.

# I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
# to allow for quick navigation around the file by creating sections and anchor points. Any use
# of "ANCHOR", "TODO", "FIXME", "STUB", "NOTE", "REVIEW", "SECTION", and "LINK" are used in conjunction with 
# this extension

# SECTION - Imports and Variables

from os import system, name
from datetime import datetime

budgetCategories = ['Gas/Feul', 'Dining', 'Food/Grocery', 'Water', 'Electricity', 'Automotive']


# !SECTION

# SECTION - Program Functions

def getCurMonth():
    """
    Gets the current month and returns it as a string
    """
    now = datetime.now()
    return (now.strftime("%B"))

# TODO - Function to prompt user for input
def getUserExpenses():
    """
    Asks the user what their budget for the month was and how much they spent in a number of predefined categories\n
    The predifined categories are contained in the budgetCategories variable at the top of the .py file\n
    Returns a list containing the expenses and the budget for the month
    """

    # Get the current month
    curMonth = getCurMonth()

    # Ask user for budget for the month
    print("How much have you budgeted for the month of " + curMonth + "?\n>> $", end="")
    userInput = input()

    valid = False

    # Continue to prompt until valid input
    while not valid:
        try:
            userBudget = float(userInput)
            valid = True
        except ValueError:
            print("(Invalid Input) How much have you budgeted for the month of " + curMonth + "?\n>> $", end="")
            userInput = input()
            pass

    # Loop through all categories
    userExpenses = []

    for category in budgetCategories:
        valid = False

        print("How much have you spent on " + category + " this month?\n>> $", end="")
        userInput = input()

        # Continue to prompt until valid input is reached
        while not valid:
            try:
                expense = float(userInput)
                userExpenses.append(expense)
                valid = True
            except ValueError:
                print("(Invalid Input) How much have you spent on " + category + " this month?\n>> $", end="")
                userInput = input()
                pass

    return userExpenses, userBudget 

# TODO - Write function to output results
def outputResults(expenseList, monthlyBudget):
    """
    Takes a list of user expenses and the budget for the month\n
    Outputs a list of the expenses and if the user was under or over the budget and by how much
    """

    # Calculate total amount spent
    totalExpenses = sum(expenseList)

    # Prints all the categories and expenses
    for category, expense in zip(budgetCategories, expenseList):
        print("\t" + category + ": ${:.2f}".format(expense))

    # Print out budget result
    if totalExpenses > monthlyBudget:
        print("You are over budget by ${:.2f}".format(totalExpenses - monthlyBudget))
    elif totalExpenses == monthlyBudget:
        print("You have spent your exact budget amount")
    else:
        print("You are under budget by ${:.2f}".format(monthlyBudget - totalExpenses))

# !SECTION

# SECTION - Extra Functions

# TODO - Create welcome message

# !SECTION



# SECTION - Main

if __name__ == "__main__":
    # TODO - Call welcome message
    # TODO - Call program functions
    expenses, monthBudget = getUserExpenses()
    outputResults(expenses, monthBudget)

# !SECTION
