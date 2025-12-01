"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument.
The function should return the names of these people in a new list.
"""

# Write your solution here
def older_people(people: list, year: int):
    older_list = [] # New list to store older people

    for person in people:
        if person[1] < year:
            older_list.append(person[0])

    return older_list # Return the name of the oldest people

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)