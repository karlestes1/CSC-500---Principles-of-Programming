# Option 2 CSC500 Module 4 - Budget Program
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
BRIGHT_RED = "\033[1;31m"
BIRGHT_GREEN = "\033[1;32m"
BOLD = "\033[1;37m"
NOCOLOR = "\033[m"



# !SECTION

# SECTION - Program Functions

def getCurMonth():
    """
    Gets the current month and returns it as a string
    """
    now = datetime.now()
    return (now.strftime("%B"))

def getUserExpenses():
    """
    Asks the user what their budget for the month was and how much they spent in a number of predefined categories\n
    The predifined categories are contained in the budgetCategories variable at the top of the .py file\n
    Returns a list containing the expenses and the budget for the month
    """

    # Get the current month
    curMonth = getCurMonth()

    # Ask user for budget for the month
    print("How much have you budgeted for the month of " + BOLD + curMonth + NOCOLOR + "?\n>> $", end="")
    userInput = input()

    valid = False

    # Continue to prompt until valid input
    while not valid:
        try:
            userBudget = float(userInput)
            valid = True
        except ValueError:
            print(BRIGHT_RED + "(Invalid Input)" + NOCOLOR + " How much have you budgeted for the month of " + BOLD + curMonth + NOCOLOR + "?\n>> $", end="")
            userInput = input()
            pass

    # Loop through all categories
    userExpenses = []

    for category in budgetCategories:
        valid = False

        print("How much have you spent on " + BOLD + category + NOCOLOR + " for " + curMonth + "?\n>> $", end="")
        userInput = input()

        # Continue to prompt until valid input is reached
        while not valid:
            try:
                expense = float(userInput)
                userExpenses.append(expense)
                valid = True
            except ValueError:
                print(BRIGHT_RED + "(Invalid Input)" + NOCOLOR + " How much have you spent on " + BOLD + category + NOCOLOR + " for " + curMonth + "?\n>> $", end="")
                userInput = input()
                pass

    return userExpenses, userBudget 

# TODO - Write function to output results
def outputResults(expenseList, monthlyBudget):
    """
    Takes a list of user expenses and the budget for the month\n
    Outputs a list of the expenses and if the user was under or over the budget and by how much
    """

    curMonth = getCurMonth()

    # Calculate total amount spent
    totalExpenses = sum(expenseList)

    print("\n* * * * " + BOLD + curMonth + " Budget Results" + NOCOLOR + " * * * *\n")

    # Prints all the categories and expenses
    for category, expense in zip(budgetCategories, expenseList):
        print("\t" + BOLD + category + NOCOLOR + ": ${:.2f}".format(expense))

    print("\n")
    # Print out budget result
    if totalExpenses > monthlyBudget:
        print(BRIGHT_RED + "\tYou are over budget by ${:.2f}\n".format(totalExpenses - monthlyBudget) + NOCOLOR)
    elif totalExpenses == monthlyBudget:
        print(BOLD + "\tYou have spent your exact budget amount\n" + NOCOLOR)
    else:
        print(BIRGHT_GREEN + "\tYou are under budget by ${:.2f}\n".format(monthlyBudget - totalExpenses) + NOCOLOR)

# !SECTION

# SECTION - Extra Functions

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
        

    # Diamond ascii art is from asciiart.eu and was crated by Donovan Blake
    # Font for ascii title was generated on patorjk.com with the Text to ASCII Art Generator (TAAG)
    print(r" .     '     ,  ██████  ██    ██ ██████   ██████  ███████ ████████ ██ ███    ██  ██████  ")
    print(r"   _________    ██   ██ ██    ██ ██   ██ ██       ██         ██    ██ ████   ██ ██       ")
    print(r"_ /_|_____|_\ _ ██   ██ ██    ██ ██   ██ ██       ██         ██    ██ ████   ██ ██       ")
    print(r"  '. \   / .'   ██████  ██    ██ ██   ██ ██   ███ █████      ██    ██ ██ ██  ██ ██   ███ ")
    print(r"    '.\ /.'     ██   ██ ██    ██ ██   ██ ██    ██ ██         ██    ██ ██  ██ ██ ██    ██ ")
    print(r"      '.'       ██████   ██████  ██████   ██████  ███████    ██    ██ ██   ████  ██████  ")
    print("\nDeveloped by Karl Estes")
    print("Created as per Module 4 instructions in CSC 500 at CSUG\n\n")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")

# !SECTION



# SECTION - Main

if __name__ == "__main__":
    welcomeMessage()
    expenses, monthBudget = getUserExpenses()
    outputResults(expenses, monthBudget)

# !SECTION
