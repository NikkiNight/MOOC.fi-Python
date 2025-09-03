"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

"Please write a program which asks the user which editor they are using.
The program should keep on asking until the user types in Visual Studio Code."
"""

# Write your solution here
while True:
    answer = input("What editor are you using?")
    answer = answer.upper()

    if answer == "WORD" or answer  == "NOTEPAD":
        print("awful")
    if answer =="EMACS" or answer == "ATOM":
        print("not good")
    if answer == "VISUAL STUDIO CODE":
        print("an excellent choice!")
        break
