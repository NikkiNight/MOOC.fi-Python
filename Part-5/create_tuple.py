"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments,
and creates and returns a tuple based on the following criteria:

The first element in the tuple is the smallest of the arguments
The second element in the tuple is the greatest of the arguments
The third element in the tuple is the sum of the arguments
"""

# Write your solution here
def create_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z) # Find the smallest number
    greatest = max(x, y, z) # Find the greatest number

    addition = sum((x, y, z)) # Add all values

    result = (smallest, greatest, addition) # Construct result as a tuple

    return result

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))    