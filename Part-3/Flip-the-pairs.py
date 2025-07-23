"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to type in a number.
The program then prints out all the positive integer values from 1 up to the number.
However, the order of the numbers is changed so that each pair or numbers is flipped.
That is, 2 comes before 1, 4 before 3 and so forth."
"""

# Write your solution here
num = int(input("Please enter a number: "))

i = 1 # Counter

while i <= num:
    if i + 1 <= num: # Check to see if pair
        print(i + 1)
        print(i)
    else: # Print lone number
        print(i)
    i += 2 # Move forward 2 numbers (pairs)