"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"Please write a program which asks for the names and ages of two persons.
The program should then print out the name of the elder."
"""

# Write your solution here
print("Person 1:")
person1Name = input("Name: ")
person1Age = int(input("Age: "))

print("Person 2:")
person2Name = input("Name: ")
person2Age = int(input("Age: "))

if person1Age > person2Age:
    print(f"The elder is {person1Name}")
elif person2Age > person1Age:
    print(f"The elder is {person2Name}")
elif person1Age == person2Age:
    print(f"{person1Name} and {person2Name} are the same age")