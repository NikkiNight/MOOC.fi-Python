"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt.
When the program is executed, it should first read any entries already in the file.
"""

# Write your solution here
file = "diary.txt"

while True: # Loop until user quits
    print("1 - add an entry, 2 - read entries, 0 - quit")
    options = input("Function: ")

    if options == "1":
        diary_entry = input("Diary entry: ")

        with open(file, "a") as my_file: # Append file
            my_file.write(diary_entry + "\n")
            print("Diary saved\n")

    elif options == "2":
        print("Entries:")  

        with open(file, "r") as my_file: # Read file
            for line in my_file:
                line = line.strip() # Removes new lines & spaces
                print(line)

    else:
        print("Bye now!")
        break
