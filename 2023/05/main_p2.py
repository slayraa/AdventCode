import re
import numpy as np

puzzle_input = "2023/inputs/05.txt"
#puzzle_input = "2023/inputs/05_sample.txt"

dict_almanac = {"seed": [], "soil": [], "fertilizer": [], "water": [], 
                "light": [], "temperature": [], "humidity": [], "location": []}

# Code almanac into dictionary
with open(puzzle_input, "r") as file:
    for line in file:
        if "seeds" in line:
            k = "seed"
        elif "seed-to-soil" in line:
            k = "soil"
        elif "soil-to-fertilizer" in line:
            k = "fertilizer"
        elif "fertilizer-to-water" in line:
            k = "water"
        elif "water-to-light" in line:
            k = "light"
        elif "light-to-temperature" in line:
            k = "temperature"
        elif "temperature-to-humidity" in line:
            k = "humidity"
        elif "humidity-to-location" in line:
            k = "location"

        if line != "\n":
            dict_almanac[k].append(re.findall(r"\d+", line))


# Remove empty lines from dict_almanac
for k in list(dict_almanac.keys()):
    dict_almanac[k] = [line for line in dict_almanac[k] if line != []]


location = 60000000
seed_not_found = True
while seed_not_found:
    location = location + 1
    src = location
    
    # Find seed backwards
    for k in list(dict_almanac.keys())[::-1]:
        new_src = None
        for line in dict_almanac[k]:
            destination = int(line[0])
            source = int(line[1])
            step = int(line[2])

            if src in range(destination, destination+step):
                new_src = source + (src - destination)
                break
        
        if new_src is not None:
            src = new_src
    
        for seeds in dict_almanac["seed"]:
            if src in range(int(seeds[0]), int(seeds[0])+int(seeds[1])):
                print(f"Found seed {src} for location {location}")
                seed_not_found = False
                break

print(f"What is the lowest location number that corresponds to any of the initial seed numbers? Answer: {location}")
# Sample is 46
# 69323688