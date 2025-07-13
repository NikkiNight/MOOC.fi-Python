"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.
The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar."
"""

# Write your solution here
print("What is the weather forecast for tomorrow? ")
temp = int(input("Temperature: "))
bool_rain = input("Will it rain? (yes/no): ")

if temp <= 20:
    print("Wear jeans and a T-shirt")
    if bool_rain == "yes":
        print("I recommend a jumper as well")
        print("Don't forget your umbrella!")


if temp > 20:
    print("Wear jeans and a T-shirt")
    if bool_rain == "yes":
        print("Don't forget your umbrella!")

if temp < 20 and temp > 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    if bool_rain == "yes":
        print("Don't forget your umbrella!")

if temp <= 10 and temp > 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    if bool_rain == "yes":
        print("Don't forget your umbrella!")
		
if temp <= 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
    if bool_rain == "yes":
        print("Don't forget your umbrella!")