"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named spruce, which takes one argument.
The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
"""

# Write your solution here
def spruce(num):
    print("a spruce!")
    i = 1
    while i <= num:
        spaces = num - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
        i += 1
    print(" " * (num - 1) + "*")        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)