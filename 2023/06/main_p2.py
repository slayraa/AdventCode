import re

puzzle_input = "2023/inputs/06.txt"
#puzzle_input = "2023/inputs/06_sample.txt"

# Read the input
with open(puzzle_input) as f:
    for line in f:
        if "Time" in line:
            time = "".join(re.findall(r'\d+', line))
        elif "Distance" in line:
            distance = "".join(re.findall(r'\d+', line))

t = int(time)
d = int(distance)

ct = 0
for i in range(1, t):
    race = i * (t - i)
    if race > d:
        ct = ct + 1

print(f"What do you get if you multiply these numbers together? Answer: {ct}")

# Sample is 71503
# 36530883