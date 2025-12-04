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
total_joltage = 0

for i in range(board.shape[0]):
    arg_jolt1 = board[i][:-1].argmax()
    jolt1 = board[i][arg_jolt1]
    jolt2 = max(board[i][arg_jolt1+1:])

    total_joltage = total_joltage + int(str(jolt1)+str(jolt2))

    #print(f"row {i} - jolt1: {jolt1}, jolt2: {jolt2}")

print(f"what is the total output joltage? {total_joltage}")
# 17100