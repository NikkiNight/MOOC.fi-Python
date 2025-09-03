"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named same_chars, which takes one string and two integers as arguments.
The integers refer to indexes within the string.
The function should return True if the two characters at the indexes specified are the same.
Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.
"""

# Write your solution here
def same_chars(word, num1, num2):

    index = word

    if num1 > len(index) - 1 or num2 > len(index) - 1 or num1 < 0 or num2 < 0:
        return False

    if index[num1] == index[num2]:
        return True
    else:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))