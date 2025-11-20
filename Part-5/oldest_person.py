"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named oldest_person(people: list), which takes a list of tuples as its argument.
In each tuple, the first element is the name of a person, and the second element is their year of birth.
The function should find the oldest person on the list and return their name.
"""

# Write your solution here
def oldest_person(people: list):
    oldest = min(people, key=lambda person: person[1])

    return oldest[0] # Return the name of the oldest person

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))