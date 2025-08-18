"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named greatest_number, which takes three arguments.
The function returns the greatest in value of the three.
"""

# Write your solution here
def greatest_number(a, b, c):
    return max(a, b, c)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)