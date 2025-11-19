"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.
The database is a list, and each movie object in the list is a dictionary.
The dictionary should contain the following keys.
name
director
year
runtime
The values attached to these keys are given as arguments to the function.
"""

# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):    
    database.append({
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    })

if __name__ =="__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    print(database)