"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks the user for an integer number.
If the number is less than zero, the program should print out the number multiplied by -1.
Otherwise the program prints out the number as is."
"""

# Write your solution here
num = int(input("Please enter an integer number: "))

if num < 0:
    num = num * -1
    print(f"The absolute value of this number is {num}")
else:
    print(f"The absolute value of this number is {num}")