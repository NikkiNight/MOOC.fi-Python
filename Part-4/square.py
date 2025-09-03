"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named square, which prints out a square of characters, and takes two arguments.
The first parameter specifies the length of the side of the square.
The second parameter specifies the character used to draw the square.
The function should call the function line from the exercise above for the actual printing out.
Copy your solution to that exercise above the code for this exercise.
Please don't change anything in the line function.
"""

# Copy here code of line function from previous exercise
def line(num, word):
    if word == "":
        print("*" * num)
    else:
        print(word[0] * num)

def square(size, character):
    # You should call function line here with proper parameters
    counter = 0
    while counter < size:
        line(size, character)
        counter += 1    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")