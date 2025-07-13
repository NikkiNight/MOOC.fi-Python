"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius.
If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!"."
"""

# Write your solution here
temp = int(input("Enter the temperature in degrees Fahrenheit: "))

celsius = (temp - 32) * 5/9

if celsius < 0:
    print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")