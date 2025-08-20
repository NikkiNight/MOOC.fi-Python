"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a program which asks the user to type in values and adds them to a list.
After each addition, the list is printed out in two different ways:
    - in the order the items were added
    - ordered from smallest to greatest
The program exits when the user types in 0.
"""

# Write your solution here
my_list = []

while True:
    value = int(input("Please enter a value: "))

    my_list.append(value) # Add the value to the list

    if value == 0:
        print("Bye!")
        break

    print(f"The list now:", my_list)

    sorted_list = sorted(my_list)  # Sort the list
    print(f"The list in order:", sorted_list)