"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks the user for a number of days.
The program then prints out the number of seconds in the amount of days given."
"""

# Write your solution here
days = int(input("Enter an amount of days: "))
seconds = days * 24 * 60 * 60

print(f"Seconds in that many days: {seconds}")