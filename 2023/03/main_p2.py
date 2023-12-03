import numpy as np

puzzle_input = "2023/inputs/03.txt"
#puzzle_input = "2023/inputs/03_sample.txt"

# Read the text file
with open(puzzle_input, "r") as file:
    lines = file.readlines()

# Convert each character to a NumPy matrix
m_puzzle = np.array([list(line.replace("\n","").strip()) for line in lines])

gears = {}
# Find all the (i,j) coordinates of the symbols
for row in range(len(m_puzzle)):
    for col in range(len(m_puzzle[row])):
        # Found a symbol then store the 8 coordinates that surround it
        if m_puzzle[row][col] == "*":
            hot_coordinates = []
            #print(m_puzzle[row][col])
            hot_coordinates.append((row-1,col-1))
            hot_coordinates.append((row-1,col))
            hot_coordinates.append((row-1,col+1))
            hot_coordinates.append((row,col-1))
            hot_coordinates.append((row,col+1))
            hot_coordinates.append((row+1,col-1))
            hot_coordinates.append((row+1,col))
            hot_coordinates.append((row+1,col+1))
            gears[(row,col)] = hot_coordinates

# Create dictionary to store the values per gear
gears_numbers = {}
for k in gears.keys():
    gears_numbers[k] = []

# Keep all numbers that are in hot coordinates
first_digit = True
for row in range(len(m_puzzle)):
    for col in range(len(m_puzzle[row])):
        #print(m_puzzle[row][col])
        if m_puzzle[row][col].isdigit():
            if first_digit:
                start_number = col
                first_digit = False
            # end of line
            elif (col == len(m_puzzle[row])-1) and (not first_digit):
                for j in range(start_number,col):
                    for k, v in gears.items(): 
                        if (row,j) in v:
                            number = "".join(m_puzzle[row][start_number:(col+1)])
                            gears_numbers[k].append(int(number))
                            first_digit = True
                            break
        else:
            if not first_digit:
                for j in range(start_number,col):
                    for k, v in gears.items(): 
                        if (row,j) in v:
                            number = "".join(m_puzzle[row][start_number:col])
                            gears_numbers[k].append(int(number))
                            first_digit = True
                            break

                first_digit = True

# Remove duplicates from gears_numbers and calculate gear ratio
gears_ratio = []
for k in gears_numbers.keys():
    gears_numbers[k] = list(set(gears_numbers[k]))
    if len(gears_numbers[k]) == 2:
        gears_ratio.append(gears_numbers[k][0]*gears_numbers[k][1])

print(f"What is the sum of all of the part numbers in the engine schematic? Answer: {sum(gears_ratio)}")
#sample is 467835
#84883664