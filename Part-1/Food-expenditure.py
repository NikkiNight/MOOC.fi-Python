"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which estimates a user's typical food expenditure.
The program asks the user how many times a week they eat at the student cafeteria.
Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
Based on this information the program calculates the user's typical food expenditure both weekly and daily."
"""

# Write your solution here
timesEat = float(input("How many times a week do you ear at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries a week? "))
print("")

weekly = (timesEat * price) + groceries
daily = weekly / 7

print("Average food expenditure: ")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")