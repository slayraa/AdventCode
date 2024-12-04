import re

puzzle_input = "2024/inputs/03_input.txt"
#puzzle_input = "2024/inputs/03_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()

# Convert into a single string
s = "".join(lines)

# Find all mul(X,Y) values
mul_values = re.findall(r'mul\((\d+),(\d+)\)', s)

sum = 0
for val in mul_values:
    sum = sum + (int(val[0]) * int(val[1]))

print(f"What do you get if you add up all of the results of the multiplications? Answer: {sum}")
#184122457