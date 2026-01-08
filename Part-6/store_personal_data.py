"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a function named store_personal_data(person: tuple), which takes a tuple containing some identifying information as its argument.

The tuple contains the following elements:
Name (string)
Age (integer)
Height (float)

This should be processed and written into the file people.csv. The file may already contain some data; the new entry goes to the end of the file.
The data should be written in the format: name;age;height
Each entry should be on a separate line.
"""

# Write your solution here
def store_personal_data(person: tuple):
    name, age, height = person # Unpack tuple into variables

    with open("people.csv", "a") as my_file:
        my_file.write(f'{name};{age};{height}\n')

# Tests
#test = store_personal_data(("Paul Paulson", 37, 175.5))
#print(test)