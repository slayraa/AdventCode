import re

puzzle_input = "2023/inputs/06.txt"
#puzzle_input = "2023/inputs/06_sample.txt"

# Read the input
with open(puzzle_input) as f:
    for line in f:
        if "Time" in line:
            time = re.findall(r'\d+', line)
        elif "Distance" in line:
            distance = re.findall(r'\d+', line)

races = [(int(i), int(j)) for i,j in zip(time, distance)]

races_dict = {}
ct = 0
for t, d in races:
    ct = ct + 1
    races_dict[ct] = []
    for i in range(1, t):
        race = i * (t - i)
        if race > d:
            races_dict[ct].append(i)

wins = [len(race) for race in races_dict.values()] 

mult = 1
for i in wins:
    mult = mult * i

print(f"What do you get if you multiply these numbers together? Answer: {mult}")

# Sample is 288
# 512295