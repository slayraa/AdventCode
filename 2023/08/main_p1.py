import re

puzzle_input = "2023/inputs/08.txt"
#puzzle_input = "2023/inputs/08_sample1.txt"
#puzzle_input = "2023/inputs/08_sample2.txt"

with open(puzzle_input) as f:
    lines = f.read().splitlines()

orientation = lines[0]

or_dict = {}
for line in lines[2:]:
    or_dict[line[:3]] = re.findall(r'\w+', line[4:])

# initialise variables
goal = "ZZZ"
steps = 0
pointer = "AAA"
ct = 0

while pointer != goal:
    if orientation[ct] == "L":
        orient = 0
    else:
        orient = 1
    ct = (ct + 1) % len(orientation)

    pointer = or_dict[pointer][orient]
    steps = steps + 1

print(f"How many steps are required to reach ZZZ? Answer: {steps}")

# Sample1 is 2 and sample2 is 6
# 11309