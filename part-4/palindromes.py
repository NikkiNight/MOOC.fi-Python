"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome.
Palindromes are words which are spelled exactly the same backwards and forwards.
Please also write a main program which asks the user to type in words until they type in a palindrome.
"""

# Write your solution here
def palindromes(word):
    if word == word[:: -1]:
        print(word, "is a palindrome!")
        return True
    else:
        print("that wasn't a palindrome")
        return False

word = input("Please type in a palindrome: ") 
while not palindromes(word):
    word = input("Please type in a palindrome: ")        

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
