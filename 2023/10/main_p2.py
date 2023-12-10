import numpy as np

puzzle_input = "2023/inputs/10.txt"
#puzzle_input = "2023/inputs/10_sample3.txt"
#puzzle_input = "2023/inputs/10_sample4.txt"
#puzzle_input = "2023/inputs/10_sample5.txt"

# Read the text file
with open(puzzle_input, "r") as file:
    lines = file.readlines()

# Convert each character to a NumPy matrix
m_puzzle = np.array([list(line.replace("\n","").strip()) for line in lines])
start_s = np.where(m_puzzle == "S")

def find_s_shape(start_s, m_puzzle):
    # Find all adjacent coordinates to start_s in m_puzzle
    row = start_s[0][0]
    col = start_s[1][0]

    adjacent_symbols = {"N":"", "S":"", "E":"", "W":""}
    if row-1 >= 0:
        adjacent_symbols["N"] = m_puzzle[row-1][col]
    if row+1 < len(m_puzzle):
        adjacent_symbols["S"] = m_puzzle[row+1][col]
    if col-1 >= 0:
        adjacent_symbols["W"] = m_puzzle[row][col-1]
    if col+1 < len(m_puzzle[0]):
        adjacent_symbols["E"] = m_puzzle[row][col+1]
    
    if adjacent_symbols["S"] in ["J", "|"] and adjacent_symbols["E"] in ["-", "7", "J"]:
        return "F"
    elif adjacent_symbols["S"] == "|" and adjacent_symbols["W"] in ["-", "F", "L"]:
        return "7"
    elif adjacent_symbols["N"] == "|" and adjacent_symbols["E"] in ["-", "7", "J"]:
        return "L"
    elif adjacent_symbols["N"] == "|" and adjacent_symbols["W"] in ["-", "F", "L"]:
        return "J"
    elif adjacent_symbols["W"] == "-" and adjacent_symbols["N"] in ["|", "7", "J"]:
        return "J"


def find_next_coordinates(pt, m_puzzle):
    row = pt[0]
    col = pt[1]
    coords = []
    
    if m_puzzle[pt] == "F":
        if m_puzzle[(row+1, col)] != ".":
            coords.append((row+1, col))
        if m_puzzle[(row, col+1)] != ".":
            coords.append((row, col+1))
    
    elif m_puzzle[pt] == "7":
        if m_puzzle[(row+1, col)] != ".":
            coords.append((row+1, col))
        if m_puzzle[(row, col-1)] != ".":
            coords.append((row, col-1))
    
    elif m_puzzle[pt] == "L":
        if m_puzzle[(row-1, col)] != ".":
            coords.append((row-1, col))
        if m_puzzle[(row, col+1)] != ".":
            coords.append((row, col+1))

    elif m_puzzle[pt] == "J":
        if m_puzzle[(row-1, col)] != ".":
            coords.append((row-1, col))
        if m_puzzle[(row, col-1)] != ".":
            coords.append((row, col-1))

    elif m_puzzle[pt] == "|":
        if m_puzzle[(row-1, col)] != ".":
            coords.append((row-1, col))
        if m_puzzle[(row+1, col)] != ".":
            coords.append((row+1, col))

    elif m_puzzle[pt] == "-":
        if m_puzzle[(row, col-1)] != ".":
            coords.append((row, col-1))
        if m_puzzle[(row, col+1)] != ".":
            coords.append((row, col+1))

    return coords


# Find the loop
m_puzzle[start_s] = find_s_shape(start_s, m_puzzle)
pt = (start_s[0][0], start_s[1][0])
travelled = []
new_coords = [pt]

while set(new_coords).difference(set(travelled)) != set():
    last_coords = set(new_coords).difference(set(travelled))
    travelled.extend(last_coords)

    new_coords = []
    for pt in last_coords:
        new_coords.extend(find_next_coordinates(pt, m_puzzle))


int_points = 0
# Scan the matrix
for row in range(m_puzzle.shape[0]-1):
    in_region = False
    corner_L = False
    corner_F = False

    for col in range(m_puzzle.shape[1]-1):

        # Use loop coords to know what's inside or outside
        if ((row, col) in travelled):
            
            if corner_L and (m_puzzle[row][col] == "7"):
                in_region = not in_region
                corner_L = False
            
            elif corner_F and (m_puzzle[row][col] == "J"):
                in_region = not in_region
                corner_F = False
                
            elif m_puzzle[row][col] == "F":
                corner_F = True

            elif m_puzzle[row][col] == "L":
                corner_L = True
            
            elif m_puzzle[row][col] in ["7", "J"]:
                corner_L = False
                corner_F = False
            
            elif m_puzzle[row][col] == "|":
                in_region = not in_region
    
        else:
            if in_region:
                #print(f"Found a point at ({row},{col}) for {m_puzzle[row][col]}")
                int_points = int_points + 1


print(f"How many tiles are enclosed by the loop? Answer: {int_points}")

# Sample3 is 4
# Sample4 is 8
# Sample5 is 10
# 285