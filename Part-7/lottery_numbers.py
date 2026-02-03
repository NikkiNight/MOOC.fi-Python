"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

Please write a function named lottery_numbers(amount: int, lower: int, upper: int), which generates as many random numbers as specified by the first argument.
All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned. The numbers should be in ascending order in the returned list.
As these are lottery numbers, no number should appear twice in the list.
"""

# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    lottery_nums = []

    while len(lottery_nums) < amount:
        num = randint(lower, upper) # Generate a random number based on the given upper and lower values

        if num in lottery_nums: # If randomly generated number is already in the list, skip
            continue
        else: # Else append it to the list
            lottery_nums.append(num)

    # Sort numbers in ascending order
    lottery_nums.sort()

    return lottery_nums

# Tests
#print(lottery_numbers(3, 1, 6))