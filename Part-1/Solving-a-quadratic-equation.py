"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program for solving a quadratic equation of the form ax²+bx+c.
The program asks for values a, b and c. It should then use the quadratic formula to solve the equation.
The quadratic formula expressed with the Python sqrt function is as follows:
x = (-b ± sqrt(b²-4ac))/(2a).
You can assume the equation will always have two real roots, so the above formula will always work."
"""

# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

num1 = int(input("Enter a value: "))
num2 = int(input("Enter a second value: "))
num3 = int(input("Enter a third value: "))

# formula = (-b ± sqrt(b²-4ac))/(2a)
root1 = (-num2 + sqrt(num2**2 - 4 * num1 * num3)) / (2 * num1)
root2 = (-num2 - sqrt(num2**2 - 4 * num1 * num3)) / (2 * num1)

print(f"The roots are: {root1} and {root2}")