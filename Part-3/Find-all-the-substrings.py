"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please make an extended version of the previous program,
which prints out all the substrings which are at least three characters long,
and which begin with the character specified by the user.
You may assume the input string is at least three characters long."
"""

# Write your solution here# Write your solution here
word = str(input("Please enter a word: "))
letter = str(input("Please enter a letter: "))

index = word.find(letter)

while index != -1 and index + 3 <= len(word):        
    print(word[index:index + 3])
    index = word.find(letter, index + 1) # Find the next letter