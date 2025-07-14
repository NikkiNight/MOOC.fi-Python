"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"The table below outlines the grade boundaries on a certain university course.
Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points	grade
< 0	impossible!
0-49	fail
50-59	1
60-69	2
70-79	3
80-89	4
90-100	5
> 100	impossible!"
"""

# Write your solution here
points = int(input("Enter the amount of points received: "))

if points < 0:
    print("Grade: impossible!")
elif points >= 0 and points <= 49:
    print("Grade: fail")
elif points >= 50 and points <= 59:
    print("Grade: 1")
elif points >= 60 and points <= 69:
    print("Grade: 2")
elif points >= 70 and points <= 79:
    print("Grade: 3")
elif points >= 80 and points <= 89:
    print("Grade: 4")
elif points >= 90 and points <= 100:
    print("Grade: 5")
elif points > 100:
    print("Grade: impossible!")