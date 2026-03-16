"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

Please write a function named print_persons(filename: str), which reads a JSON file and prints the contents.
The file may contain any number of entries.
The hobbies should be listed in the same order as they appear in the JSON file.
"""

# Write your solution here
import json

def print_persons(filename: str):
    with open(filename, 'r') as my_file:
        info = json.load(my_file) # Load the file

    for student in info:
        name, age, hobbies = student["name"], student["age"], student["hobbies"]

        hobbies_str = ", ".join(hobbies) # Join the contents of "hobbies" together

        print(f'{student["name"]} {age} years ({hobbies_str})')