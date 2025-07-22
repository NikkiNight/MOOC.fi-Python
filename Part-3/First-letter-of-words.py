"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to type in a sentence.
The program then prints out the first letter of each word in the sentence, each letter on a separate line."
"""

# Write your solution here
sentence = input("Please enter a sentence: ")

words = sentence.split() # ["word", "word", etc] 01234...
index = 0 

while index < len(words):    
    print(words[index][:1]) # Prints the first letter
    index += 1