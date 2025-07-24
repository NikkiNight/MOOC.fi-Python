"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a function named seven_brothers.
When the function is called, it should print out the names of the seven brothers in alphabetical order."
"""

# Write your solution here

def seven_brothers():
    list_brothers = ["Aapo", "Eero", "Juhani", "Lauri", "Simeoni", "Timo", "Tuomas"]
    list_brothers.sort()
    
    i = 0
    while i < len(list_brothers):
        print(list_brothers[i])
        i += 1
        
if __name__ == "__main__":
    seven_brothers()