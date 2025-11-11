"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers.
The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.
"""

# Write your solution here# Write your solution here
phonebook = {}

while True: # Loop until user exits
    command = input("Please enter a command: 1 search, 2 add, 3 quit: ") # User input

    if command == "1": # Search phone book
        name = input("Name: ")

        if name in phonebook:
            for num in phonebook[name]:
                print(num)
        else:
            print("no number")       

    elif command == "2": # Add key(Name) & value(Number) to phone book
        name = input("Name: ")
        number = input("Number: ")

        if name in phonebook:
            phonebook[name].append(number) # Appends additional numbers to name 
        else:
            phonebook[name] = [number] # Assigns Name and Number to phonebook dictionary as a list

        print("ok!")

    else: # Quit        
        print("quitting...")
        break
