"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"Please write a program which asks the user for an integer number.
If the number is divisible by three, the program should print out Fizz.
If the number is divisible by five, the program should print out Buzz.
If the number is divisible by both three and five, the program should print out FizzBuzz."
"""

# Write your solution here
num = int(input("Enter an integer number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")