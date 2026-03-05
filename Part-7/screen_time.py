"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

Please write a program for recording the amount of time the user has spent in front of a television, computer or mobile device screen over a specific period of time.
The user will input each day on a separate line, and the entries will contain three numbers separated by spaces, representing minutes.
With the above input, the program should store the data in a file.
"""

# Write your solution here
from datetime import datetime, timedelta

# Prompt filename
filename = input("Filename: ")

# ----

# Prompt start date
start_date = input("Starting date: ") # Format "%d.%m.%Y"

day, month, year = start_date.split(".") # Split parts based on .

# Integer conversion & building the start date
int_day = int(day)
int_month = int(month)
int_year = int(year)

strt_date = datetime(int_year, int_month, int_day)

# ----

# Prompt length of test period
length = input("How many days: ")

# Integer conversion & building the finish date
int_length = int(length)

finish_date = strt_date + timedelta(days=int_length - 1)

# ----

# Prompting for data. Format: TV Computer Mobile, in minutes, (i.e 200 0 60), seperated by whitespace
print("Please type in screen time in minutes on each day (Format: TV computer mobile):")

# Creation of the file
with open(filename, "w") as my_file:

    # Variables
    total_tv = 0
    total_computer = 0
    total_mobile = 0

    daily_data = [] # Store data by day

    for i in range(int_length):
        current_day = strt_date + timedelta(days=i)

        data = input(f"{current_day.strftime('%d.%m.%Y')}: ") # Display date

        tv, computer, mobile = data.split(" ") # Split data based on whitespace

        # Convert str to int
        tv = int(tv)
        computer = int(computer)
        mobile = int(mobile)

        # Append data to list for later use
        daily_data.append((current_day, tv, computer, mobile))

        # Sum for average
        total_tv += tv
        total_computer += computer
        total_mobile += mobile
    
    # Calc total minutes & average
    total_minutes = total_tv + total_computer + total_mobile
    average = total_minutes / int_length

    # Write to file
    my_file.write(f"Time period: {strt_date.strftime('%d.%m.%Y')}-{finish_date.strftime('%d.%m.%Y')}\n") # Add original time period given by user and final date based on length given (i.e 5 days)
    my_file.write(f"Total minutes: {total_minutes}\n")
    my_file.write(f"Average minutes: {average}\n")    
    for date, tv, computer, mobile in daily_data:
        my_file.write(f"{date.strftime('%d.%m.%Y')}: {tv}/{computer}/{mobile}\n")
