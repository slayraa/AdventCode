import numpy as np

puzzle_input = "2025/inputs/04_input.txt"
#puzzle_input = "2025/inputs/04_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    board = []
    for line in lines:
        board.append(list(line.replace("\n","")))
    
    board = np.array(board)
    board[board == '@'] = 1
    board[board == '.'] = 0
    board = board.astype(np.int64)

    return board

board = read_puzzle_input(puzzle_input)
n_rolls = 0
max_rolls = 4

#Sum all 8 the adjacent cells to (i,j) and add 1 to n_rolls if the sum is <= max_rolls
for i in range(board.shape[0]):
    for j in range(board.shape[1]):
        if board[i,j] == 1:
            adjacent_sum = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if (di == 0 and dj == 0):
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < board.shape[0] and 0 <= nj < board.shape[1]:
                        adjacent_sum += board[ni, nj]
            if adjacent_sum < max_rolls:
                n_rolls += 1

print(f"How many rolls of paper can be accessed by a forklift? {n_rolls}")
# 1370