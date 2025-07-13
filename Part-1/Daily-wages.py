"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks for the hourly wage, hours worked, and the day of the week.
The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled."
"""

# Write your solution here
hourlyWage = float(input("Enter hourly wage: "))
hoursWorked = int(input("Enter hours worked: "))
dayOfWeek = input("Enter day of the week: ")

if dayOfWeek == "sunday" or dayOfWeek == "Sunday":
    dailyWage = (hourlyWage * hoursWorked) * 2
    print(f"Daily wages: {dailyWage} euros")
else:
    dailyWage = hourlyWage * hoursWorked
    print(f"Daily wages: {dailyWage} euros")