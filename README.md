# CSC 500 - Principles of Programming

**Disclaimer:** These projects were built as a requirement for CSC 500: Principles of Programming at Colorado State University Global under the instruction of Dr. Lori Farr. Unless otherwise noted, all programs were created to adhere to explicit guidelines as outlined in the assignment requirements I was given. Descriptions of each [programming assignment](#programming-assignments) and the [portfolio project](#portfolio-project) can be found below.

*****This repository was archived after completion of the class*****
___

### Languages and Tools
<img align="left" height="32" width="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />
<img align="left" height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/anaconda.svg" />
<img align="left" height="32" width="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png" />
<img align="left" height="32" width="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png" />
<img align="left" height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/gitkraken.svg" />
<br />

### Textbook
The textbook for this class was specially designed and is hosted on zyBooks to allow for interactive programming while learning the concepts
<br />

### VS Code Python Extension
I am using the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Visual Studio Code which includes the ability to create python cells which can be individually run in an interactive window. The syntax to create a cell is as follows: 
```python
#%%
```
Any line with these three characters on it denotes the beginning of a python cell and is included due to the utilization of the python extension.

### VS Code Comment Anchors Extension
I am also using the [Comment Anchors extension](https://marketplace.visualstudio.com/items?itemName=ExodiusStudios.comment-anchors) for Visual Studio Code which places anchors within comments to allow for easy navigation and the ability to track TODO's, code reviews, etc. 
<br />

___
<!--When doing relative paths, if a file or dir name has a space, use %20 in place of the space-->
<!--TODO - Update all code files with attributions for ascii art-->
## Programming Assignments
### Module 1: [Python Program to Add Two Numbers](Module%201/addTwoNums.py)
- A simple python program to find the addition and subtraction of two numbers
- Asks the user to input two numbers, performs simple mathematical operations on the inputs, and displays the resulting output

### Module 2: [Retail Total](Module%202/retailTotal.py)
- A python program that prompts the user to input prices for 5 different items
- Calculates the subtotal of those item costs and the total with a 7% sales tax
- Outputs the results to the terminal
- I went overboard and added some ascii art

### Module 3: [Alarm Time](Module%203/alarmTime.py)
- A python program displays the current time (H, D, M, Y) and asks the user how many hours to wait
- Calculates what hour, day, month, and year it will be after that many hours and outputs to the terminal
- I continued the Ascii Art title theme

### Module 4: [Budgeting](Module%204/budget.py)
- A python program that asks the user for a budget and expenses for the current month
- Outputs what the user spent in each category, the total expenses, and a message on whether or not the user was within their budget range and by how much
- Added some nice color to some of the terminal messages cause why not!

### Module 5: [Mixing Colors](Module%205/mixingColors.py)
- A python program which prompts the user to enter the name of two primary colors
- Outputs what color the resulting mixture would produce

### Module 6: [Course Information](Module%206/courseInfo.py)
- A python program which reads in a series of csv files containing course information
- The user is able to view a list of all courses or specify detailed information about a single course
- Course information is stored in separate csv files which are read in upon program start
___
## Portfolio Project
The portfolio project is final project of the class and consists of two milestones and the final submission. The project centers around creating a shopping cart where users can buy items and it will calculate the total cost of the entire cart. Descriptions of each milestone and their requirements are listed below

### [Milestone 1](Portfolio%20Project/Milestone%201/shoppingCart.py)
#### Requirements Include:
- A class called ItemToPurchase with the following:
    - Attributes
        - item name (string)
        - item price (float)
        - item quantity (int)
    - A default constructor 
    - A method to print the item cost
- Prompt the user to enter the price and quantity of two items, and output the total cost to the screen

### [Milestone 2](Portfolio%20Project/Milestone%202/shoppingCart.py)
- Addition of a class called ShoppingCart with the following:
    - A parameterized constructor
    - Attributes
        - customer name (string)
        - current date (string)
        - items in cart (list)
    - A method to add items to the cart
    - A method to remove items from the cart
    - A method to modify item detials once in the cart
    - A method to get the number of items (total quantity) in the cart
    - A method to calculate the total cost of the cart
    - Methods to output all items in the cart and all item descriptions
- The program will continue to execute until the users explicitly quits

### [Final](Portfolio%20Project/Final/shoppingCart.py)
- Structure is the same as Milestone 2
- Did some reformatting of console output for final submission
