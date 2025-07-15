"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for a number.
The program then prints out all integer numbers greater than zero but smaller than the input."
"""

# Write your solution here
number = int(input("Please enter a number: "))

i = 1

while i < number: 
    print(i)
    i += 1