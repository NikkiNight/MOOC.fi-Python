"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named anagrams, which takes two strings as arguments.
The function returns True if the strings are anagrams of each other.
Two words are anagrams if they contain exactly the same characters.
"""

# Write your solution here
def anagrams(word1, word2):

    # Sort character in both words to compare
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

if __name__ == "main":
    print(anagrams("tame", "meta"))  # should return True
    print(anagrams("tabby", "batty"))  # should return False
