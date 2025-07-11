"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks the user for four numbers.
The program then prints out the sum and the mean of the numbers."
"""

# Write your solution here
NumOne = int(input("Enter a number: "))
NumTwo = int(input("Enter a second number: "))
NumThree = int(input("Enter a third number: "))
NumFour = int(input("Enter a fourth number: "))

add = NumOne + NumTwo + NumThree + NumFour
mean = add / 4

print(f"The sum of the numbers is {add} and the mean is {mean}")