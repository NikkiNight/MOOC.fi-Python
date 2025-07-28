"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters."
"""

# Write your solution here
def squared(word, length):
    i = 0 # Counter

    while i != length:
        board = ""
        j = 0 # Counter  
        while j != length:            
            index = (i * length + j) % len(word)
            board += word[index]
            j += 1
        print(board)
        i += 1

# Testing the function
if __name__ == "__main__":
    squared("ab", 3)