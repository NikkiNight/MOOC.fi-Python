"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to type in an integer number.
If the user types in a number equal to or below 0, the execution ends.
Otherwise the program prints out the factorial of the number.
The factorial of a number involves multiplying the number by all the positive integers smaller than itself.
In other words, it is the product of all positive integers less than or equal to the number.
For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120."
"""

# Write your solution here
import math

while True:
    num = int(input("Please enter an integer number: "))
    if num <= 0:
        # End program
        print("Thanks and bye!")
        break
    else:  
        factorial = math.factorial(num)
        print(f"The factorial of the number {num} is {factorial}")    