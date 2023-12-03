import numpy as np

puzzle_input = "2023/inputs/03.txt"
#puzzle_input = "2023/inputs/03_sample.txt"

# Read the text file
with open(puzzle_input, "r") as file:
    lines = file.readlines()

# Convert each character to a NumPy matrix
m_puzzle = np.array([list(line.replace("\n","").strip()) for line in lines])

hot_coordinates=[]
# Find all the (i,j) coordinates of the symbols
for row in range(len(m_puzzle)):
    for col in range(len(m_puzzle[row])):
        # Found a symbol then store the 8 coordinates that surround it
        if m_puzzle[row][col] != "." and (not m_puzzle[row][col].isdigit()):
            #print(m_puzzle[row][col])
            hot_coordinates.append((row-1,col-1))
            hot_coordinates.append((row-1,col))
            hot_coordinates.append((row-1,col+1))
            hot_coordinates.append((row,col-1))
            hot_coordinates.append((row,col+1))
            hot_coordinates.append((row+1,col-1))
            hot_coordinates.append((row+1,col))
            hot_coordinates.append((row+1,col+1))

# Remove duplicates
hot_coordinates = list(set(hot_coordinates))

# Keep all numbers that are in hot coordinates
hot_numbers = []
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
                    if (row,j) in hot_coordinates:
                        number = "".join(m_puzzle[row][start_number:(col+1)])
                        hot_numbers.append(int(number))
                        first_digit = True
                        break
        else:
            if not first_digit:
                for j in range(start_number,col):
                    if (row,j) in hot_coordinates:
                        number = "".join(m_puzzle[row][start_number:col])
                        hot_numbers.append(int(number))
                        break

                first_digit = True

print(f"What is the sum of all of the part numbers in the engine schematic? Answer: {sum(hot_numbers)}")
#537732