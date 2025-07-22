"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to type in a string and a single character.
The program then prints the first three character slice which begins with the character specified by the user.
You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.
Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for.
In that case nothing should be printed out, and there should not be any indexing errors when executing the program."
"""

# Write your solution here
word = str(input("Please enter a word: "))
letter = str(input("Please enter a letter: "))

index = word.find(letter)

if index != -1 and index + 3 <= len(word):
    print(word[index:index + 3])