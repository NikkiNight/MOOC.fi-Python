"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a program which asks the user to choose between addition and removal.
Depending on the choice, the program adds an item to or removes an item from the end of a list.
The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
"""

# Write your solution here
my_list = [] # Initialize an empty list

# Print list contents
print(f'The list is now', my_list)

i = 1

while True:
    # Prompt the user for an action
    action = input("Do you want to add or remove an item? Or exit? (d/r/x): ")

    if action == "d": # Add to the list
        my_list.append(i)
        print(f'The list is now', my_list)
        i += 1

    elif action == "r": # Remove the last item from the list
        if my_list:
            del my_list[-1]
            i -= 1
        print(f'The list is now', my_list)

    elif action == "x": # Exit
        print("Bye!")
        break