"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a program which initialises a list with the values [1, 2, 3, 4, 5].
Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again.
This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.
"""

# Write your solution here

# Initialize lsit with values
my_list = [1, 2, 3, 4, 5]

index = 0 # Initialize index to 0

while index != -1:
    # Prompt user for index input
    index = int(input("Please enter an index: "))

    if index == -1: # If user enter -1, exit the program
        break

    # prompt user for new value to enter
    new_value = int(input("Please enter a new value: "))

    # Replace value at the given index
    my_list[index] = new_value

    print(my_list)