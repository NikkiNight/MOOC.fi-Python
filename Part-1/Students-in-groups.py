"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks for the number of students on a course and the desired group size.
The program will then print out the number of groups formed from the students on the course.
If the division is not even, one of the groups may have fewer members than specified."
"""

students = int(input("How many students on the course? "))
groupSize = int(input("Desired group size: "))

numGroups = students / groupSize

if numGroups % 2 != 0:
    numGroups = int(numGroups) + 1
    print(f"Number of groups formed: {numGroups}")
else:
    print(f"Number of groups formed: {numGroups}")