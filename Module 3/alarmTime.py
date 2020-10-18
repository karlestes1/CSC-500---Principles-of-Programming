# Python Program to help keep time
# Created by Karl Estes
# Created: Sunday, October 18th, 2020

# This program displays the current date and time (hour only) and prompts the user to enter
# how many hours they would like to wait. The program them tells the user what day and time
# it will be when the 'alarm' would go off

# I am using the Python extension for Visual Studio Code which includes the ability to create python cells 
# which can be individually run in an interactive window. 
# The syntax to create a cell is as follows: #%%
# Any line with these three characters on it denotes the beginning of a 
# python cell and is included due to the utilization of the python extension. 

from os import system, name
from datetime import datetime, timedelta

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

    print(r" .----------------. .----------------. .----------------. .----------------. .----------------.     .----------------. .----------------. .----------------. .----------------. ")
    print(r"| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |   | .--------------. | .--------------. | .--------------. | .--------------. |")
    print(r"| |      __      | | |   _____      | | |      __      | | |  _______     | | | ____    ____ | |   | |  _________   | | |     _____    | | | ____    ____ | | |  _________   | |")
    print(r"| |     /  \     | | |  |_   _|     | | |     /  \     | | | |_   __ \    | | ||_   \  /   _|| |   | | |  _   _  |  | | |    |_   _|   | | ||_   \  /   _|| | | |_   ___  |  | |")
    print(r"| |    / /\ \    | | |    | |       | | |    / /\ \    | | |   | |__) |   | | |  |   \/   |  | |   | | |_/ | | \_|  | | |      | |     | | |  |   \/   |  | | |   | |_  \_|  | |")
    print(r"| |   / ____ \   | | |    | |   _   | | |   / ____ \   | | |   |  __ /    | | |  | |\  /| |  | |   | |     | |      | | |      | |     | | |  | |\  /| |  | | |   |  _|  _   | |")
    print(r"| | _/ /    \ \_ | | |   _| |__/ |  | | | _/ /    \ \_ | | |  _| |  \ \_  | | | _| |_\/_| |_ | |   | |    _| |_     | | |     _| |_    | | | _| |_\/_| |_ | | |  _| |___/ |  | |")
    print(r"| ||____|  |____|| | |  |________|  | | ||____|  |____|| | | |____| |___| | | ||_____||_____|| |   | |   |_____|    | | |    |_____|   | | ||_____||_____|| | | |_________|  | |")
    print(r"| |              | | |              | | |              | | |              | | |              | |   | |              | | |              | | |              | | |              | |")
    print(r"| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |   | '--------------' | '--------------' | '--------------' | '--------------' |")
    print(r" '----------------' '----------------' '----------------' '----------------' '----------------'     '----------------' '----------------' '----------------' '----------------'")
    print("Developed by Karl Estes")
    print("Created as per Module 3 instructions in CSC 500 at CSUG\n\n")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

'''
Gets the current date and time at program start
Outputs that information to the screen
Returns the current datetime
'''
def getCurrentDatetime():
    
    # Get the time and date right now
    now = datetime.now()

    # Get the hour and date
    hour = now.strftime("%H")
    date = now.strftime("%d day of %B in the year %Y")


    # Print the info to the screen
    print("It is hour", hour, "of the", date)

    return now

''' 
Calculates what the new time will be based on the user input
Displays the results to the screen
'''
def calculateNewDatetime(currentTime, hoursToWait):

    # Calculate the new time
    newTime = currentTime + timedelta(hours=hoursToWait)

    # Get the hour and date
    hour = newTime.strftime("%H")
    date = newTime.strftime("%d day of %B in the year %Y")

    # Print the info to the screen
    print("After", hoursToWait, "hours, it will be hour", hour, "of the", date)



def main():

    # Print the title and welcome message
    welcomeMessage()

    # Get the current date and time
    curTime = getCurrentDatetime()

    # Prompt user
    validInput = False
    print("How many whole hours would you like to wait? >>> ", end='')

    while not validInput:
        
        userInput = input()

        try:
            hoursToWait = int(userInput)
            validInput = True
        except ValueError:
            print("(Invalid Input) How many whole hours would you like to wait? >>> ", end='')
            pass

    # Calculate new datetime
    calculateNewDatetime(curTime, hoursToWait)



if __name__ == "__main__":
    main()