import numpy as np

puzzle_input = "2025/inputs/03_input.txt"
#puzzle_input = "2025/inputs/03_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    board = []
    for line in lines:
        board.append(list(line.replace("\n","")))
    
    board = np.array(board)
    board = board.astype(np.int64)
    
    return board

board = read_puzzle_input(puzzle_input)
max_digits = 12
row_size = board.shape[1]
total_joltage = 0

for row_i in range(board.shape[0]):
    row_jolts = []
    remaining_row = board[row_i] 

    while len(remaining_row)>0:
        arg_jolt = remaining_row[:(len(remaining_row)-(max_digits-len(row_jolts))+1)].argmax()
        
        # while the best is not the last
        if (len(remaining_row[arg_jolt:]) + len(row_jolts)) > max_digits:
            row_jolts.append(remaining_row[arg_jolt])

            if len(row_jolts) == max_digits:
                remaining_row = []
            else:
                remaining_row = remaining_row[arg_jolt+1:]
        else:
            # if the best number is the last, add everything to the left to fill the 12 digits
            if arg_jolt == (len(remaining_row)-1):
                for val in remaining_row[(-max_digits+len(row_jolts)):]:
                    row_jolts.append(val)
            
            # add everything that fits to the right from arg_jolt
            else:
                for val in remaining_row[arg_jolt:]:
                    row_jolts.append(val)

            remaining_row = []
    
    print(f"Joltage for row {row_i} is {''.join(map(str, row_jolts))}")
    total_joltage = total_joltage + int(''.join(map(str, row_jolts)))

print(f"what is the total output joltage? {total_joltage}")
# sample = 3121910778619
# 170418192256861