# Option 2 CSC500 Module 6 - Course Information
# Created by Karl Estes
# Created: Tuesday, November 10th, 2020

# This program reads in some course information from a series of files and allows the user to view the information
# related to each course.
# The user can prompt to see a list of all courses or view more detailed information about a single course

# I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
# to allow for quick navigation around the file by creating sections and anchor points. Any use
# of "ANCHOR", "TODO", "FIXME", "STUB", "NOTE", "REVIEW", "SECTION", and "LINK" are used in conjunction with 
# this extension

# TODO - Make sure test files are populated with data

# SECTION - Imports and Global Variables
from os import system, name
import csv

allCourses = set([]) # Will contain a list of all available courses sorted by course title

RESET = "\u001b[0m"
WARNING = "\u001b[38;5;220m"
ERROR = "\u001b[38;5;196m"
INFO = "\u001b[38;5;123m"
BOLD = "\u001b[38;5;15m"


# !SECTION

# SECTION - File Handling

def readInCSV(filePath):
    '''
    Reads in the specified file with the assumption it follows a csv format

    The csv should have the first column containing the keys and the second column
    should contain the values

    The key-value pairs will be added to a dictionary which will be returned upon 
    function completion

    Also adds courses to the global course list (TODO - create helper function to add things to the list w/o duplicates)
    '''

    entryDict = {}

    # Read in the CSV
    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1

        for row in csv_reader:
            if line_count == 1:
                line_count += 1
            else:
                # Add to the dictionary
                try:
                    entryDict[row[0]] = row[1]
                    allCourses.add(row[0]) 
                except (RuntimeError, TypeError, NameError, IndexError):
                    printError(f">> Error reading in line {line_count} from {filePath}")
                line_count += 1

    return entryDict

def loadAllFiles():
    '''
    Loads the three files required for the program (instructorInfo.csv, meetingTime.csv, and
    roomInfo.csv) into dictionaries

    Returns all three dictionaries in the following order: roomInfo, instructorInfo, meetingTime
    '''
    roomInfo = readInCSV("roomInfo.csv")
    instructorInfo = readInCSV("instructorInfo.csv")
    meetingTime = readInCSV("meetingTime.csv")

    return roomInfo, instructorInfo, meetingTime

# !SECTION

# SECTION - Program Actions

# TODO - outline and complete function
def viewCourses():
    '''
    Pulls from the global courseList to display all courses for which there is information
    '''

# TODO - outline and complete function
def displayCourseDetails(courseName, roomDict, instructorDict, meetingDict):
    '''
    Takes a course name and the three dictionaries containing course information

    Will search the dictionaries for the provided course name and output any of the course information that
    is found to the screen

    Will display a message if missing course information exists or if the entered course cannot be found
    '''


# !SECTION

# SECTION - Extra/Helper Functions

# TODO - figure out what print functions for warning, error, title, etc are needed and write them
def printWarning(stringToPrint):
    print(WARNING + str(stringToPrint) + RESET)

def printError(stringToPrint):
    print(ERROR + str(stringToPrint) + RESET)

def printInfo(stringToPrint):
    print(INFO + str(stringToPrint) + RESET)

def welcomeMessage():
    '''
    Prints a welcome message and clears the console on program start
    '''
    # For windows
    if name == 'nt':
        _ = system('cls')
    # Mac and linux 
    else:
        _ = system('clear')

    # Font is Stick Letters from the Text to ASCII Art Generator (TAAG) on www.patorjk.com
    print()
    print(WARNING + r" __   __        __   __   ___            ___  __  ")
    print(r"/  ` /  \ |  | |__) /__` |__     | |\ | |__  /  \ ")
    print(r"\__, \__/ \__/ |  \ .__/ |___    | | \| |    \__/ " + RESET)
    print("\nDeveloped by Karl Estes")
    print("Created as per Module 6 Option 2 instructions in CSC 500 at CSUG\n\n")
    printInfo("You may type q or quit at any point to exit this program")
    printInfo("You may type ? or help at any point to see a list of commands")
    print(BOLD + "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n" + RESET)

def printMenu():
    '''
    Displays the meny of commands to the screen
    '''
    print(BOLD + "\n* * * Commands * * *" + RESET)
    printInfo("'v'/'view' : View all courses")
    printInfo("'i'/'info' : Will prompt for a course number to pull information for a specific course")
    printInfo("'q'/'quit' : Quit the program")
    printInfo("'?'/'help' : Print the commands menu\n")



# !SECTION

# SECTION - Main

# TODO - define main

if __name__ == "__main__":

    welcomeMessage()
    printInfo(">> Loading course data...")
    loadAllFiles()
    printInfo(">> Course data has been loaded")

    # Loop with user input until program is quit
    while True:
        print(BOLD + ">> " + RESET, end='') # TODO - Make arrows bold
        userInput = input()

        '''
        Menu choices include:

        v/view to view all courses
        i/info to view course info
            - will prompt for course name after selecting
        q/quit to exit program
        ?/help to print menu commands
        '''
        if userInput == "v" or userInput == "view":
            viewCourses()
        elif userInput == "i" or userInput == "info":
            # TODO - prompt for coursename and search
            printWarning("Need to implement")
        elif userInput == "?" or userInput == "help":
            printMenu()
        elif userInput == "q" or userInput == "quit":
            exit(0)
        else:
            # TODO - print warning message (make warning function first)
            printWarning(">> Invalid Input - Please try again")



# !SECTION