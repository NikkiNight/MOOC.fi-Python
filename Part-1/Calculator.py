"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks the user for two numbers and an operation.
If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers.
If the user types in anything else, the program should print out nothing."
"""

# Write your solution here
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operation = input("Enter operation: ")

if operation == "add" or operation == "Add":
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")
if operation == "subtract" or operation == "Subtract":
    answer = num1 - num2
    print(f"{num1} - {num2} = {answer}")

if operation == "multiply" or operation == "Multiply":
    answer = num1 * num2
    print(f"{num1} * {num2} = {answer}")

if operation == "divide" or operation == "Divide":
    answer = num1 / num2
    print(f"{num1} / {num2} = {answer}")