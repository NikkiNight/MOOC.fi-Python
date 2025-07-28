"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes.
The function takes an integer argument, which specifies the length of the side of the board."
"""

# Write your solution here
def chessboard(length):
    i = 0 # Counter
    while i != length:
        board = ""
        j = 0 # Counter
        while j != length:
            if (i + j) % 2 == 0:
                board += "1"
            else:
                board += "0"
            j += 1
        print(board)
        i += 1        

# Testing the function
if __name__ == "__main__":
    chessboard(3)
