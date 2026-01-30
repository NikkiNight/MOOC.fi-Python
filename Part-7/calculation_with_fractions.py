"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

Please familiarize yourself with the Python module fractions.
Use it to write a function named fractionate(amount: int), which takes the number of parts as its argument.
The function should divide the number 1 into as many equal sized fractions as is specified by the argument, and return these in a list.
"""

# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    result_list = []

    for parts in range(amount):
        result = Fraction(1, amount)

        print(result)
        result_list.append(result)

    return result_list

# Tests
#print(fractionate(5))
#print(fractionate(3))
