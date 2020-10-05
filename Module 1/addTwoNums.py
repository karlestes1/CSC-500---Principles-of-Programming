# Python Program to Add and Subtract Two Numbers
# Created by Karl Estes
# Monday, October 5th, 2020

# This program prompts a user to input two integers and, given those two numbers, adds them together to find the output
# It also subtracts the two numbers to find the output

# I am using the Python extension for Visual Studion Code which includes the ability to create python cells 
# which can be individually run in an interactive window. 
# The syntax to create a cell is as follows: #%%
# Any line with these three characters on it denotes the beginning of a 
# python cell and is included due to the utilization of the python extension. 

#%%
# Import statements
import sys

# Do we keep trying input
redoInput = True

#%%

while redoInput:
    # Get the user input and validate the input type
    in1 = input('Enter your first integer:\n')
    in2 = input('Enter your second integer:\n')

    try:
        num1 = int(in1)
        num2 = int(in2)
        redoInput = False
    except ValueError:
        print('A provided input was not an integer, please try input again.')
        redoInput = True


#%%
# Prints the sum of the two numbers
print('The sum of', num1, 'and', num2, 'is', num1 + num2)

# Prints the difference of the two numbers
print('The difference of', num1, 'and', num2, 'is', num1 - num2)
