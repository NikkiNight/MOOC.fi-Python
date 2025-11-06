"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named double_items(numbers: list), which takes a list of integers as its argument.
The function should return a new list, which contains all values from the original list doubled.
The function should not change the original list.
"""

# Write your solution here
def double_items(numbers: list):
    doubled = [] # New list

    for num in numbers:
        new_num = num * 2

        doubled.append(new_num)
    
    return doubled

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)