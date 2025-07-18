"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to type in a string.
The program then prints out all the substrings which begin with the first character, from the shortest to the longest."
"""

# Write your solution here
word = str(input("Please enter a word: "))

length = len(word)
i = 1 # Letter counter

while length > 0:
    print(word[0:i])
    length -= 1 # Counts down to track how many letters are left to print
    i += 1 # Indicates the word splicing from the start (first letter), then continues until the whole word is printed                  