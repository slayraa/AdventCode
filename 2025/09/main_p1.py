import numpy as np
import re

puzzle_input = "2025/inputs/09_input.txt"
#puzzle_input = "2025/inputs/09_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    squares = []
    for line in lines:
        coords = re.findall(r'\d+', line)
        squares.append(coords)
    
    squares = np.array(squares).astype(float)
    
    return squares

squares = read_puzzle_input(puzzle_input)

# find the manhattan distance between all pairs of squares
# store in a dictionary with keys as tuple of indices and values as distance
dist_pairs = {}
for i in range(len(squares)):
    for j in range(i+1, len(squares)):
        pair = [squares[i], squares[j]]
        dist = (np.abs(squares[j][0] - squares[i][0]) + 1) * (np.abs(squares[j][1] - squares[i][1]) + 1)
        dist_pairs[(i,j)] = dist

# sort pairs by values (distance)
sorted_dist_keys = sorted(dist_pairs, key=dist_pairs.get, reverse=True)
best_pair = [squares[sorted_dist_keys[0][0]], squares[sorted_dist_keys[0][1]]]

print(f"what is the largest area of any rectangle you can make? {dist_pairs[sorted_dist_keys[0]]}")
# 4749929916
