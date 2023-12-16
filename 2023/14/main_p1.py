
import numpy as np

puzzle_input = "2023/inputs/14.txt"
#puzzle_input = "2023/inputs/14_sample.txt"

# Read the text file
with open(puzzle_input, "r") as f:
    lines = f.read().splitlines()

m_puzzle = np.array([list(line) for line in lines])

# Find coordinates for the Os in m_puzzle
o_coords = np.where(m_puzzle == "O")
hash_coords = np.where(m_puzzle == "#")


def find_lowest_x(row, col, m_puzzle, hash_coords):
    """
    Find the lowest row an O can move up to
    """

    # Move north
    for i in range(row):
        if m_puzzle[i, col] == ".":

            # Check if there is no # between
            hash_rows = hash_coords[0][hash_coords[1] == col]
            
            if len([hr for hr in hash_rows if hr in range(i, row)]) == 0:
                return([i, col])

    return([row, col])


# Find the lowest x for each "O" in coordinates
for row, col in zip(o_coords[0], o_coords[1]):
    if row > 0:
        new_coordinates = find_lowest_x(row, col, m_puzzle, hash_coords)
        if set(new_coordinates) != set([row, col]):
            i = new_coordinates[0]
            # Replace with "O" and "." to avoid double counting
            m_puzzle[i, col] = "O"
            m_puzzle[row, col] = "."

total_load = 0
row = 0
# Find the sum of Os times their row
for multiplier in range(m_puzzle.shape[0], 0, -1):
    count_os = sum(m_puzzle[row, :] == "O")
    total_load = total_load + (count_os * multiplier)
    row = row + 1

print(f"What is the total load on the north support beams? Answer: {total_load}")
# Sample is 136
# 112046