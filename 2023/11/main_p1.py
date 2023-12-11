import numpy as np

puzzle_input = "2023/inputs/11.txt"
#puzzle_input = "2023/inputs/11_sample.txt"

# Read the text file
with open(puzzle_input, "r") as file:
    lines = file.readlines()

# Convert each character to a NumPy matrix
m_puzzle = np.array([list(line.replace("\n","").strip()) for line in lines])

# Find rows and columns where all symbols are "."
dotted_rows = np.where(np.all(m_puzzle == ".", axis=1))[0]
dotted_cols = np.where(np.all(m_puzzle == ".", axis=0))[0]

# Replace "#" in m_puzzle with range of ints from 1 to number of #s
galax_coordinates = np.argwhere(m_puzzle == "#")
m_puzzle[m_puzzle == "#"] = np.arange(1, np.sum(m_puzzle == "#") + 1)

distances = []
# Find the Manhattan distance between all pairs of #s
for i in range(len(galax_coordinates)-1):
    for j in range(i+1, len(galax_coordinates)):

        [row1, col1] = galax_coordinates[i]
        [row2, col2] = galax_coordinates[j]

        # Only calculate distance between different galaxies
        if [row1, col1] != [row2, col2]:
            
            # Find the number of empty rows and columns that the galaxy crosses
            rows_crossed = [r for r in range(min(row1, row2), max(row1, row2)) if r in dotted_rows] # increases row number
            cols_crossed = [c for c in range(min(col1, col2), max(col1, col2)) if c in dotted_cols] # increases column number

            # Find the start and end coordinates of the galaxy
            galax_start = np.array([row1, col1])
            galax_end = np.array([row2, col2])

            # Calculate the Manhattan distance between the two galaxies
            distance = np.linalg.norm(galax_end - galax_start, 1) + len(rows_crossed) + len(cols_crossed)
            
            distances.append(distance)
            #print(f"The distance between galaxy {m_puzzle[row1,col1]} and {m_puzzle[row2,col2]} is {distance}")

print(f"What is the sum of these lengths? Answer: {np.sum(distances)}")
# Sample is 374
# 10077850