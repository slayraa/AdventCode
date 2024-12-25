import numpy as np

puzzle_input = "2024/inputs/25_input.txt"
#puzzle_input = "2024/inputs/25_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    keys = []
    locks = []
    curr_board = []
    for line in lines:
        if (line == "\n"):
            curr_board = np.array(curr_board)
            curr_board[curr_board == '#'] = 1
            curr_board[curr_board == '.'] = 0
            curr_board = curr_board.astype(np.int64)

            if curr_board[0].sum() == len(curr_board[0]):
                locks.append(curr_board)
            else:
                keys.append(curr_board)

            curr_board = []
        else:
            curr_board.append(list(line.replace("\n","")))
            
            if line == lines[-1]:
                curr_board = np.array(curr_board)
                curr_board[curr_board == '#'] = 1
                curr_board[curr_board == '.'] = 0
                curr_board = curr_board.astype(np.int64)

                if curr_board[0].sum() == len(curr_board[0]):
                    locks.append(curr_board)
                else:
                    keys.append(curr_board)
    
    return keys, locks

keys, locks = read_puzzle_input(puzzle_input)

unique_pairs = 0
for key in keys:
    for lock in locks:
        res = key + lock
        if res[res>1].sum() == 0:
            unique_pairs = unique_pairs + 1

print(f"How many unique lock/key pairs fit together without overlapping in any column? {unique_pairs}")
# 3671