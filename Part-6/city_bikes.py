"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.
Each station has a single line in the file. The line contains the coordinates, name, and other identifying information for the station.

Part 1: First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary.
Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station.
The first element in the tuple is the Longitude field, and the second is the Latitude field.

Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.
The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

Part 2: Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other.
The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.
"""

# Write your solution here
import math

# Part 1
def get_station_data(filename: str):
    city_bikes = {} # Dictionary to store info
    
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(";")

            # ignore the header line
            if parts[0] == "Longitude":
                continue

            # Remove excess whitespace \n
            parts[6] = parts[6].rstrip()

            # Variables for dictionary
            longitude = float(parts[0])
            latitude = float(parts[1])
            bike_FID = parts[2]
            station_name = parts[3]
            total_slot = parts[4]
            operative = parts[5]
            bike_id = parts[6]

            # Assign dictionary info to variables
            city_bikes[station_name] = {
                "longitude": longitude,
                "latitude": latitude,
                "bike_FID": bike_FID,
                "station_name": station_name,
                "total_slot": total_slot,
                "operative": operative,
                "bike_id": bike_id
            }

        stations = {}
        for name, info in city_bikes.items():
            stations[name] = (info["longitude"], info["latitude"])
        
    return stations

def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    # Math formula. Pythagorean theorem. sqrt from math module
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

# Part 2
def greatest_distance(stations: dict):

    station_a = "" # Station A name
    station_b = "" # Station B name
    max_distance = 0 # Greatest distance

    for stationA in stations:
        for stationB in stations:
            if stationA == stationB: # Skip if comparing with itself
                continue
            d = distance(stations, stationA, stationB)

            if d > max_distance:
                station_a = stationA
                station_b = stationB
                max_distance = d

            furthest_stations = (station_a, station_b, max_distance)

    return furthest_stations

# Part 1 tests
#test_bikes = get_station_data("stations1.csv")
#print(test_bikes)

# Part 1 distance tests
#stations = get_station_data('stations1.csv')
#d = distance(stations, "Designmuseo", "Hietalahdentori")
#print(d)
#d = distance(stations, "Viiskulma", "Kaivopuisto")
#print(d)

# Part 2 tests
#stations = get_station_data('stations1.csv')
#station1, station2, greatest = greatest_distance(stations)
#print(station1, station2, greatest)