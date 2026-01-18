"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

The exercise template includes the file words.txt, which contains words in English.

Please write a function named find_words(search_term: str). It should return a list containing all the words in the file which match the search term.
The search term may include lowercase letters and the following wildcard characters:
- A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield words like ping and pong, and .a.e would yield words like sane, care and late.
- An asterisk * at the end of the search term means that any word which begins with the search term is acceptable.
- An asterisk at the beginning of the search term means that any word which ends with the search term is acceptable.
For example, ca* would yield words like california, cat, caring and catapult, while *ane would yield words like crane, insane and aeroplane.

There can only ever be a single asterisk in the search term.
If there are no wildcard characters in the search term, only words which match the search term exactly are returned.
You may assume both wildcards are never used in the same search term.
The words in the file are all written in lowercase. You may also assume the argument to the function will be in lowercase entirely.
If no matching words are found, the function should return an empty list.
"""

# Write your solution here
import re # Regex

def find_words(search_term: str):
    words = [] # Empty list to store matching words

    if search_term.endswith("*"): # If the search_term ends with an asterisk (*)
        prefix = search_term[:-1] # Remove the last character: (*), to get the prefix 
        pattern = re.compile(f'^{prefix}.*') # ^ starts with {prefix} (e.g. "ca"). Pattern = "ca" (california, car, cat, candy, etc)

    elif search_term.startswith("*"): # If the search_term starts with an asterisk (*)
        suffix = search_term[1:] # Remove the first character: (*), to get the suffix
        pattern = re.compile(f'.*{suffix}$') # .* ends with {suffix} (e.g. "ane"). Pattern = "-ane" (crane, insane, aeroplane, etc)

    else: # If the search_term contains no wildcard or contains a dot (.)
        pattern = re.compile(f'^{search_term}$') # . = "any single character". Checks search_term for matches, and any matches with . as any single character (e.g. "c.t" = cat, cut, cot, etc)

    with open("words.txt", "r") as word_file:
        for line in word_file:
            word = line.strip() # Remove newline \n

            if pattern.match(word): # Check if regex pattern matches word in the file, if yes,
                words.append(word) # append word to words list

    return words

#print(find_words("*vokes"))