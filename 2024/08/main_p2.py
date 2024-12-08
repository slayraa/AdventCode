import numpy as np

puzzle_input = "2024/inputs/08_input.txt"
#puzzle_input = "2024/inputs/08_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

board = []
for line in lines:
    # Convert each line into a list of characters
    board.append(list(line.replace("\n","")))

# Add antinodes if they don't get out of the board
def add_antinodes(vec_i,vec_j,dist):
    antinodes = []

    valid = True
    prev_i = vec_i
    while valid:
        new_i = np.array(prev_i) - dist

        #Confirm the new positions do not leave the board
        if new_i[0] >= 0 and new_i[0] < len(board) and new_i[1] >= 0 and new_i[1] < len(board[0]):
            antinodes.append(new_i.tolist())
            prev_i = new_i
        else:
            valid = False
    
    valid = True
    prev_j = vec_j
    while valid:
        new_j = np.array(prev_j) + dist

        #Confirm the new positions do not leave the board
        if new_j[0] >= 0 and new_j[0] < len(board) and new_j[1] >= 0 and new_j[1] < len(board[0]):
            antinodes.append(new_j.tolist())
            prev_j = new_j
        else:
            valid = False

    return antinodes

# Find the different frequency antennas
freqs = [freq[0] for freq in np.unique(board) if freq != "."]

# Find the coordinates of each frequency antenna
freq_coords = {}
for freq in freqs:
    freq_coords[freq] = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == freq:
                freq_coords[freq].append((i,j))

# For the antennas with the same frequency, find the antinodes coordinates
antinodes = []
for freq in freqs:
    for i in range(len(freq_coords[freq])):
        for j in range(i+1,len(freq_coords[freq])):

            # Find the distance between the antennas
            dist = np.array(freq_coords[freq][j]) - np.array(freq_coords[freq][i])
            antinodes.extend(add_antinodes(freq_coords[freq][i],freq_coords[freq][j], dist))

# Remode duplicates
antinodes_unique = []
for antinode in antinodes:
    if antinode not in antinodes_unique:
        antinodes_unique.append(antinode)

# Add frequencies that appear more than once
for freq in freq_coords.keys():
    if len(freq_coords[freq]) > 1:
        for coord in freq_coords[freq]:
            if [coord[0], coord[1]] not in antinodes_unique:
                antinodes_unique.append([coord[0], coord[1]])

print(f"How many unique locations within the bounds of the map contain an antinode? {len(antinodes_unique)}")
#994