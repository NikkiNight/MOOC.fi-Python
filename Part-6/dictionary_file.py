"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a program which functions as a dictionary. The user can type in new entries or look for existing entries.
The dictionary entries should be written to a file called dictionary.txt. The program should first read the contents of the file.
New entries are written to the end of the file whenever they are added to the dictionary.

This exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
while True: # Loop
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")

    if function == "1": # Add word
        with open("dictionary.txt", "a") as dictionary_file:

            # input for finnish, input for english
            finnish_word = input("The word in Finnish: ")
            english_word = input("The word in English: ")

            # Add Finnish and English words to dictionary.txt file
            dictionary_file.write(f'{finnish_word} - {english_word}\n') # Format e.g.: auto - car

            print("Dictionary entry added")

    elif function == "2": # Search file
        search_term = input("Search term: ") # Input search term

        with open("dictionary.txt", "r") as dictionary_file:

            for line in dictionary_file:
                line = line.strip() # Remove newline \n

                if search_term in line:
                    print(f'{line}')

    else: # Quit
        print("Bye!")
        break