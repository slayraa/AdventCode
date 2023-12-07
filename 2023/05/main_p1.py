import re
import pandas as pd

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

# Create the seed map
list_seeds = [int(seed) for seed in dict_almanac["seed"][0]]
map_df = pd.DataFrame(columns=["seed"], data=list_seeds)

# Create columns
for k in list(dict_almanac.keys())[1:]:
    map_df[k] = None

# Fill in the map
for ki in range(1, len(dict_almanac.keys())):
    k = list(dict_almanac.keys())[ki]
    kprev = list(dict_almanac.keys())[ki-1]

    for line in dict_almanac[k]:
        if line != []:
            start = int(line[1])
            step = int(line[2])
            diff = int(line[0]) - start
            filter = ((map_df[kprev] > start) & (map_df[kprev] < (start+step)))
            map_df.loc[filter, k] = map_df.loc[filter, kprev] + diff       
            
    # Fill none with the values in the last column
    map_df[k] = map_df[k].fillna(map_df[kprev])

# Find the seed with the minimum location
min_seed = map_df["location"].min()
print(f"What is the lowest location number that corresponds to any of the initial seed numbers? Answer: {min_seed}")

# Sample is 35
# 111627841