import pandas as pd
import re
import itertools

puzzle_input = "2023/inputs/02.txt"
#puzzle_input = "2023/inputs/02_sample.txt"

# Create dataframe to store the data
df = pd.DataFrame(columns=["red", "green", "blue"])
dict_all = {}

with open(puzzle_input, "r") as file:
    ct = 1
    for line in file:
        # Process each line here
        line.replace('\n','')
        games = line.split(":")[1].split(";")

        # Save into a dictionary according to color
        dict_colour = {"red": [], "green": [], "blue": []}
        for c in dict_colour:
            if sum([c in game for game in games]) > 0:
                digits_c = [re.findall(r'\d+\s'+c, game) for game in games]
                str_digits_c = " ".join(list(itertools.chain.from_iterable(digits_c)))
                digits = [int(d) for d in re.findall(r'\d+', str_digits_c)]
                dict_colour.get(c).extend(digits)
        
        # Store all data and choose maximum for the dataframe
        dict_all[ct] = dict_colour
        dict_colour_sum = {k: max(v) for k, v in dict_colour.items()}
        df = pd.concat([df, pd.DataFrame(dict_colour_sum, index=[ct])], ignore_index=False)
        ct = ct + 1

# Find the games that are possible with 12 red cubes, 13 green cubes, and 14 blue cubes
df["power"] = df["red"]*df["blue"]*df["green"]

print(f"What is the sum of the IDs of those games? Answer: {df["power"].sum()}")
#83105