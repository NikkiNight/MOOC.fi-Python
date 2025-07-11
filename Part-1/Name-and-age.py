"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks the user for their name and year of birth."
"""

# Write your solution here
name = input("Enter your full name: ")
year = int(input("Enter your birth year: "))

age = 2021 - year

print(f"Hi {name}, you will be {age} years old at the end of the year 2021")