import numpy as np

puzzle_input = "2023/inputs/10.txt"
#puzzle_input = "2023/inputs/10_sample1.txt"
#puzzle_input = "2023/inputs/10_sample2.txt"

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
    
    if adjacent_symbols["S"] == "|" and adjacent_symbols["E"] in ["-", "7", "J"]:
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


pt = (start_s[0][0], start_s[1][0])
m_puzzle[pt] = find_s_shape(start_s, m_puzzle)
steps = 0
travelled = []
new_coords = [pt]

# Start moving
while set(new_coords).difference(set(travelled)) != set():
    last_coords = set(new_coords).difference(set(travelled))
    travelled.extend(last_coords)

    new_coords = []
    for pt in last_coords:
        new_coords.extend(find_next_coordinates(pt, m_puzzle))
    
    steps = steps + 1


print(f"How many steps along the loop does it take to get from the starting position to the point farthest from the starting position? {steps-1}")

# Sample1 is 4
# Sample2 is 8
# 7030
