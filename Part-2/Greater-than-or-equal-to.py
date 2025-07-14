"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"Please write a program which asks for two integer numbers.
The program should then print out whichever is greater.
If the numbers are equal, the program should print a different message."
"""

# Write your solution here
num1 = int(input("Please enter an integer number: "))
num2 = int(input("Please enter a second integer number: "))

if num1 > num2:
    print(f"The greater number was: {num1}")
if num2 > num1:
    print(f"The greater number was: {num2}")
if num1 == num2:
    print("The numbers are equal!")