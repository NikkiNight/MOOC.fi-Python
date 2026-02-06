"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

The exercise template contains the file words.txt, which contains some English language words, one on each line.

Please write a function named words(n: int, beginning: str), which returns a list containing n random words from the words.txt file.
All words should begin with the string specified by the second argument. The same word should not appear twice in the list.
If there are not enough words beginning with the specified string, the function should raise a ValueError exception.
"""

# Write your solution here
import random

def words(n: int, beginning: str):
    list_of_words = [] # Collect all words that begin with specified prefix

    with open ("words.txt", "r") as my_file:
        for line in my_file:
            line = line.strip() # Removes newlines & spaces

            if line.startswith(beginning):
                list_of_words.append(line)

    if n > len(list_of_words): # If there aren't enough words to return, raise an error
        raise ValueError("Not enough words")

    chosen_random_words = random.sample(list_of_words, n) # Randomly select n unique words from a list

    return chosen_random_words

# Tests
#word_list = words(3, "ca")
#for word in word_list:
#    print(word)