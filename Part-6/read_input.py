"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a function named read_input, which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function.
The function should return the final valid integer value typed in by the user.
"""

# Write your solution here
def read_input(prompt_text: str, min_value: int, max_value: int):    
    while True: # Loop
        try: # Try
            guess = input(prompt_text) # Prompt user for input

            if int(guess) >= min_value and int(guess) <= max_value: # If user input is an integer between min_value and max_value
                return int(guess) # Return the valid integer
            else: # Input was an integer but outside of the allowed range
                print(f'You must type in an integer between {min_value} and {max_value}')

        except ValueError: # User input was not an integer (e.g. letters or symbols)
            print(f'You must type in an integer between {min_value} and {max_value}')

# Tests
#number = read_input("Please type in a number: ", 5, 10)
#print("You typed in:", number)