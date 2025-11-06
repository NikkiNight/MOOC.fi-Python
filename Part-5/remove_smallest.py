"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.
The functions should find and remove the smallest item in the list.
You may assume there is a single smallest item in the list.
The function should not have a return value - it should directly modify the list it receives as a parameter.
"""

# Write your solution here
def remove_smallest(numbers: list):
    smallest = min(numbers)

    numbers.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)