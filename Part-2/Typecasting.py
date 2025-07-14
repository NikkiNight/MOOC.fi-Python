"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately.
Use the Python int function.
You can assume the number given by the user is always greater than zero."
"""

# Write your solution here
num = float(input("Please enter a floating-point number: "))

integer = int(num)
decimal = float(num) - int(num)

print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")