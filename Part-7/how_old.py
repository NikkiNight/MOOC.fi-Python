"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

Please write a program which asks the user for their date of birth, and then prints out how old the user was on the eve of the new millennium.
The program should ask for the day, month and year separately, and print out the age in days.
"""

# Write your solution here
from datetime import datetime

# Prompt user for date of birth
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

# Date variables
users_dob = datetime(year, month, day)
millennium_eve = datetime(1999, 12, 31)

if users_dob > millennium_eve:
    print("You weren't born yet on the eve of the new millennium.")
else:
    days_old = millennium_eve - users_dob # Calculate how many days old the user was on that date
    print(f'You were {days_old.days} days old on the eve of the new millennium.') # Print only the number of days with .days attribute