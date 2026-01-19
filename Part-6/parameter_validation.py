"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a function named new_person(name: str, age: int), which creates and returns a tuple containing the data in the arguments.
The first element should be the name and the second the age.

If the values stored in the parameter variables are not valid, the function should throw a ValueError exception.
Invalid parameters in this case include:
- name is an empty string
- name contains less than two words
- name is longer than 40 characters
- age is a negative number
- age is greater than 150
"""

# Write your solution here
def new_person(name: str, age: int):
    if age < 0 or age > 150: # If age is a negative number or age is greater than 150
        raise ValueError("Invalid age")

    if name == "": # If name is empty
        raise ValueError("Name cannot be empty")

    if len(name) > 40: # If name is longer than 40 characters
        raise ValueError("Name cannot be longer than 40 characters")

    name_length = name.split()
    if len(name_length) < 2: # If name is less than two words
        raise ValueError("Name cannot be less than two words")

    return (name, age)

# Tests
#test = new_person("Andrew", 320)
#print(test)

#test2 = new_person("", 20)
#print(test2)

#test3 = new_person("Andrew andrew andrew", 50)
#print(test3)

#test4 = new_person("Andrewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww", 25)
#print(test4)