"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not."
"""

# Write your solution here
year = int(input("Please enter a year: "))

if year % 400 == 0:   
    print("That year is a leap year")  
elif year % 100 == 0:  
    print("That year is not a leap year")  
elif year % 4 == 0:
    print("That year is a leap year")       
else:
    print("That year is not a leap year")