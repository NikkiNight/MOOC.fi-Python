"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a program which asks the user to type in some text.
Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them.
The case of the letters should be irrelevant to the functioning of your program.
The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.
"""

# write your solution here
text = input("Please enter some text: ")

words = text.split(" ") # Seperate each word based on white space

lowercase_words = text.lower().split(" ") # Convert to lowercase & seperate each word based on white space

with open("wordlist.txt") as new_file:
    word_dictionary = [] # Store words from the file in a dictionary

    for line in new_file:
        line = line.replace("\n", "")

        word_dictionary.append(line)

    new_text = [] # New list to store words
    for i in range(len(words)):
        original = words[i]
        lowercase = lowercase_words[i]

        if lowercase in word_dictionary:
            new_text.append(original)
        else:
            new_text.append(f'*{original}*')

    print(" ".join(new_text))
