"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which finds the second occurrence of a substring.
If there is no second (or first) occurrence, the program should print out a message accordingly.
In this exercise the occurrences cannot overlap.
For example, in the string aaaa the second occurrence of the substring aa is at index 2."
"""

# Write your solution here# Write your solution here
word = str(input("Please enter a word: "))
substring = str(input("Please enter a substring: "))

index1 = word.find(substring) # Finds the first occurance
index2 = word.find(substring, index1 + len(substring)) # Finds the second occurance

if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {index2}.")