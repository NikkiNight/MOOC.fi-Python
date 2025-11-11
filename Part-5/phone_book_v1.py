"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a phone book application.
Sample output:
command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: emily
number: 045-1212344
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...

As you can see above, each name can be attached to a single number only.
If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
phonebook = {}

while True: # Loop until user exits
    command = input("Please enter a command: 1 search, 2 add, 3 quit: ") # User input

    if command == "1": # Search phone book
        name = input("Name: ")

        if name in phonebook:
            print(phonebook[name]) # Prints Number(value) for Name(key)
        else:
            print("no number")          

    elif command == "2": # Add key(Name) & value(Number) to phone book
        name = input("Name: ")
        number = input("Number: ")

        phonebook[name] = number # Assigns Name and Number to phonebook dictionary

        print("ok!")

    else: # Quit        
        print("quitting...")
        break
