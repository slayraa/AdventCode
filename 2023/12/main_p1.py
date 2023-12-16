
import numpy as np
from itertools import product
import re

puzzle_input = "2023/inputs/12.txt"
#puzzle_input = "2023/inputs/12_sample.txt"

# Read the text file
with open(puzzle_input, "r") as f:
    lines = f.read().splitlines()

# Convert to numpy array and find all symbols
puzzle = np.array([line.split(" ") for line in lines])


def valid_row(symbols, order):
    """Check if a row of symbols is valid"""

    broken_s = re.findall(r'\#+.|\#+\Z', "".join(symbols))
    
    # Count the number of # in broken_s
    num_broken = [len(b.replace(".","")) for b in broken_s]

    return (num_broken == order)


def find_options(symbols, length, total):
    """Find all possible combinations of # and . to fill ? in line"""

    options = []
    for opt in product(symbols, repeat=length):
        if sum([1 for o in opt if o == "#"]) == total:
            options.append(opt)

    return options


counts = []
for row in puzzle:
    count = 0
    line = row[0]
    order = [int(num) for num in row[1].split(",")]
    question_coords = np.where(np.array([s for s in line]) == "?")[0]
    
    # Find how many # are missing
    number_hash = sum(order) - len(np.where(np.array([s for s in line]) == "#")[0])

    # Find all possible combinations of # and . to fill ? in line
    options = find_options(symbols=[".", "#"], 
                           length=len(question_coords), 
                           total=number_hash)

    for opt in options:
        new_line = np.array([s for s in line])
        
        for i in range(len(question_coords)):
            new_line[question_coords[i]] = opt[i]
        
        if valid_row(new_line, order):
            #print(f"Found valid line: {new_line}")
            count = count + 1
    
    counts.append(count)

print(f"What is the sum of those counts? Answer: {np.sum(counts)}")
# Sample is 21
# 7857