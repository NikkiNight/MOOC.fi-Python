"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for a positive integer number.
The program then prints out a list of multiplication operations until both operands reach the number given by the user."
"""

# Write your solution here
num = int(input("Please enter a positive number: ")) # Limit

i = 1 # Numbers

while i <= num:
    u = 1 # Multiply by
    while u <= num:
        answer = i * u
        print(f"{i} x {u} = {answer}")
        u += 1 # Increase multiply by
    i += 1 # Increase number