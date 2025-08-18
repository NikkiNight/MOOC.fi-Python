"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a program which first asks the user for the number of items to be added.
Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in.
Finally, the list is printed out.
"""

# Write your solution here
my_list = []

# Prompt user for number of items added
num_items = int(input("Enter the number of items to add: "))

i = num_items # initializing counter

# Prompt item values
while i != 0:
    value = input("Enter item value: ")
    my_list.append(int(value))
    i -= 1

# Output list of items
print(my_list)