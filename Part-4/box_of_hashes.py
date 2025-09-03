"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named box_of_hashes, which prints out a rectangle of hash characters.
The function takes one argument, which specifies the height of the rectangle.
The rectangle should be ten characters wide.
The function should call the function line from the exercise above for the actual printing out.
Copy your solution to that exercise above the code for this exercise.
Please don't change anything in your line function.
"""

# Copy here code of line function from previous exercise
def line(num, word):
    if word == "":
        print("*" * num)
    else:
        print(word[0] * num)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    counter = 0
    while counter < height:
        line(10, "#")
        counter += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
