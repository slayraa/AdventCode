
import numpy as np
from tqdm import tqdm

puzzle_input = "2023/inputs/14.txt"
puzzle_input = "2023/inputs/14_sample.txt"

# Read the text file
with open(puzzle_input, "r") as f:
    lines = f.read().splitlines()

m_puzzle = np.array([list(line) for line in lines])

# Find coordinates for the #s in puzzle_c
hash_coords = np.where(m_puzzle == "#")


def find_lowest_x(row, col, puzzle_c, hash_coords, orientation="N"):
    """
    Find the lowest row an O can move up to
    """

    if orientation == "N":
        for i in range(row):
            if puzzle_c[i, col] == ".":

                # Check if there is no # between
                hash_rows = hash_coords[0][hash_coords[1] == col]
                
                if len([hr for hr in hash_rows if hr in range(i, row)]) == 0:
                    return([i, col])

        return([row, col])
    
    elif orientation == "S":
        for i in range(puzzle_c.shape[0]-1, row, -1):
            if puzzle_c[i, col] == ".":

                # Check if there is no # between
                hash_rows = hash_coords[0][hash_coords[1] == col]
                
                if len([hr for hr in hash_rows if hr in range(row, i)]) == 0:
                    return([i, col])

        return([row, col])

    elif orientation == "W":
        for j in range(col):
            if puzzle_c[row, j] == ".":

                # Check if there is no # between
                hash_cols = hash_coords[1][hash_coords[0] == row]
                
                if len([hc for hc in hash_cols if hc in range(j, col)]) == 0:
                    return([row, j])

        return([row, col])
    
    elif orientation == "E":
        for j in range(puzzle_c.shape[1]-1, col, -1):
            if puzzle_c[row, j] == ".":

                # Check if there is no # between
                hash_cols = hash_coords[1][hash_coords[0] == row]
                
                if len([hc for hc in hash_cols if hc in range(col, j)]) == 0:
                    return([row, j])

        return([row, col])


#Each cycle tilts the platform four times: N, W, S, E
number_cycles = 1000000000
# Find the lowest x for each "O" in coordinates
for c in tqdm(range(number_cycles)):
    
    puzzle_c = m_puzzle.copy()
    for orientation in ["N", "W", "S", "E"]:
        o_coords = np.where(puzzle_c == "O")

        if orientation == "N":
            for row, col in zip(o_coords[0], o_coords[1]):
                if row > 0:
                    new_coordinates = find_lowest_x(row, col, puzzle_c, hash_coords, orientation)
                    if set(new_coordinates) != set([row, col]):
                        i = new_coordinates[0]
                        # Replace with "O" and "." to avoid double counting
                        puzzle_c[i, col] = "O"
                        puzzle_c[row, col] = "."
        
        elif orientation == "S":
            for row, col in zip(o_coords[0][::-1], o_coords[1][::-1]):
                if row < puzzle_c.shape[0] - 1:
                    new_coordinates = find_lowest_x(row, col, puzzle_c, hash_coords, orientation)
                    if set(new_coordinates) != set([row, col]):
                        i = new_coordinates[0]
                        # Replace with "O" and "." to avoid double counting
                        puzzle_c[i, col] = "O"
                        puzzle_c[row, col] = "."
        
        elif orientation == "W":
            for row, col in zip(o_coords[0], o_coords[1]):
                if col > 0:
                    new_coordinates = find_lowest_x(row, col, puzzle_c, hash_coords, orientation)
                    if set(new_coordinates) != set([row, col]):
                        j = new_coordinates[1]
                        # Replace with "O" and "." to avoid double counting
                        puzzle_c[row, j] = "O"
                        puzzle_c[row, col] = "."
        
        elif orientation == "E":
            for row, col in zip(o_coords[0][::-1], o_coords[1][::-1]):
                if col < puzzle_c.shape[1] - 1:
                    new_coordinates = find_lowest_x(row, col, puzzle_c, hash_coords, orientation)
                    if set(new_coordinates) != set([row, col]):
                        j = new_coordinates[1]
                        # Replace with "O" and "." to avoid double counting
                        puzzle_c[row, j] = "O"
                        puzzle_c[row, col] = "."

    # Compare the solutions after each cycle
    if (m_puzzle == puzzle_c).all():
        print(f"Same puzzle as previous after {c} cycles")
        break
    else:
        m_puzzle = puzzle_c.copy()


total_load = 0
row = 0
# Find the sum of Os times their row
for multiplier in range(puzzle_c.shape[0], 0, -1):
    count_os = sum(puzzle_c[row, :] == "O")
    total_load = total_load + (count_os * multiplier)
    row = row + 1

print(f"What is the total load on the north support beams? Answer: {total_load}")
# Sample is 64
#