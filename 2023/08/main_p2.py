import re
from math import lcm

puzzle_input = "2023/inputs/08.txt"
#puzzle_input = "2023/inputs/08_sample3.txt"

with open(puzzle_input) as f:
    lines = f.read().splitlines()

orientation = lines[0]

# create dictionary of input
or_dict = {}
for line in lines[2:]:
    or_dict[line[:3]] = re.findall(r'\w+', line[4:])

# Find all starting points that end with "A"
start = [k for k in or_dict.keys() if k[2]=="A"]

# get dictionary with all steps to reach xxZ
steps_start = {}

for pointer in start:
    k = pointer
    ct = 0
    steps = 0
    
    while pointer[2] != "Z":
        if orientation[ct] == "L":
            orient = 0
        else:
            orient = 1
        ct = (ct + 1) % len(orientation)

        pointer = or_dict[pointer][orient]
        steps = steps + 1
    
    steps_start[k] = [pointer, steps]
    print(f"From {k} reaching pointer {pointer} took {steps} steps")

# Find the least common multiplier for all steps
lcm_numbers = [steps_start[k][1] for k in steps_start.keys()]
steps = lcm(16043, 20777, 13939, 18673, 11309, 17621)

print(f"How many steps does it take before you're only on nodes that end with Z? Answer: {steps}")

# Sample is 6
# 13740108158591