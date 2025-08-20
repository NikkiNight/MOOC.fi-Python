"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named list_of_stars, which takes a list of integers as its argument.
The function should print out lines of star characters.
The numbers in the list specify how many stars each line should contain.
"""

# Write your solution here
def list_of_stars(my_list):
    for i in my_list:
        print("*" * i)

if __name__ == "__main__":
    my_list = [3, 7, 1, 1, 2]
    list_of_stars(my_list)