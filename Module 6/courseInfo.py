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

# SECTION - Imports and Global Variables
from os import system, name

allCourses = [] # Will contain a list of all available courses sorted by course title

# TODO - Decide what colors are needed and make global variables


# !SECTION

# SECTION - File Handling

# TODO - outline and complete function
def readInCSV(filePath):
    '''
    Reads in the specified file with the assumption it follows a csv format

    The csv should have the first column containing the keys and the second column
    should contain the values

    The key-value pairs will be added to a dictionary which will be returned upon 
    function completion

    Also adds courses to the global course list (TODO - create helper function to add things to the list w/o duplicates)
    '''


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

# TODO - write welcome function
def welcomeMessage():
    '''
    Prints a welcome message and clears the console on program start
    '''



# !SECTION

# SECTION - Main

# TODO - define main



# !SECTION