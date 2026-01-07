"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user.
"""

# Write your solution here
name = input("Whom should I sign this to: ")
file = input("Where shall I save it: ")

with open(file, "w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, ")
    my_file.write("Mooc.fi Team")