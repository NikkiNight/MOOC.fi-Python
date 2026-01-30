"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

Write a function named separate_characters(my_string: str).
The function takes a string as its argument, and it should separate the characters in the string into three other strings, and return these in a tuple:
- The first string should contain the lowercase and uppercase ASCII letters (string constant ascii_letters)
- The second string should contain all punctuation characters defined by the string constant punctuation
- The third string should contain all the other characters (including whitespace)

The characters should appear in the three strings in the same order as they appeared in the original string.
"""

# Write your solution here
import string

def separate_characters(my_string: str):
    # Empty variables to store different character types
    ascii_letters = ""
    punctuation = ""
    other = ""

    for character in my_string:
        if character in string.ascii_lowercase or character in string.ascii_uppercase: # If character is an ASCII letter (a-z or A-Z)
            ascii_letters += character
        
        elif character in string.punctuation: # If character is a punctuation mark
            punctuation += character

        else: # If character is whitespace, digit, or a non-ASCII symbol
            other += character

    return (ascii_letters, punctuation, other)

# Test
#test = separate_characters("Olé!!! Hey, are ümläüts wörking?")
