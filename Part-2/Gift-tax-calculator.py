"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation or payment.
If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.
When the gift is received from a close relative or a family member, the amount of tax to be paid can be found on this website: https://www.vero.fi/en/individuals/property/gifts/gift-tax-calculator/
Please write a program which calculates the correct amount of tax for a gift from a close relative."
"""

# Write your solution here
amount = int(input("Enter amount: "))

if amount >= 5000 and amount <= 25000:
    tax = (100 + (amount - 5000) * 0.08)
    print(f"Amount of tax: {tax}")
elif amount >= 25000 and amount <= 55000:
    tax = (1700 + (amount - 25000) * 0.10)
    print(f"Amount of tax: {tax}")
elif amount >= 55000 and amount <= 200000:
    tax = (4700 + (amount - 55000) * 0.12)
    print(f"Amount of tax: {tax}")
elif amount >= 200000 and amount <= 1000000:
    tax = (22100 + (amount - 200000) * 0.15)
    print(f"Amount of tax: {tax}")
elif amount > 1000000:
    tax = (142100 + (amount - 1000000) * 0.17)
    print(f"Amount of tax: {tax}")
else:
   print("No tax!")