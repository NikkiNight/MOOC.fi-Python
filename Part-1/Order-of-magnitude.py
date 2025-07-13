"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks the user for an integer number.
The program should then print out the magnitude of the number according to the following examples:

Please type in a number: 950
This number is smaller than 1000
Thank you!

Sample output
Please type in a number: 59
This number is smaller than 1000
This number is smaller than 100
Thank you!

Sample output
Please type in a number: 2
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10
Thank you!

Sample output
Please type in a number: 1123
Thank you!"
"""

# Write your solution here
num = int(input("Enter an integer number: "))

ten = 10
hundred = 100
thousand = 1000

if num < thousand:
    print(f"This number is smaller than {thousand}")
if num < hundred:
    print(f"This number is smaller than {hundred}")
if num < ten:
    print(f"This number is smaller than {ten}")
print("Thank you!")