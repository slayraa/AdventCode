import numpy as np

puzzle_input = "2025/inputs/07_input.txt"
#puzzle_input = "2025/inputs/07_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    board = []
    for line in lines[1:]:
        line = list(line.replace("\n",""))
        if len(np.unique(line)) > 1:
            board.append(line)
    
    board = np.array(board)
    board = board.astype(str)

    return board

board = read_puzzle_input(puzzle_input)
n_splits = 1
splits = np.argwhere(board == '^')

for split in splits[1:]:
    i, j = split
    
    if (j>0) and ('^' in board[:i, j-1]):
        _left = np.argwhere(board[:i, j-1] == '^').max()
    else:
        _left = 0
    
    if (j < board.shape[1]-1) and ('^' in board[:i, j+1]):
        _right = np.argwhere(board[:i, j+1] == '^').max()
    else:
        _right = 0
    
    if ('^' in board[:i, j]):
        _hat = np.argwhere(board[:i, j] == '^').max()
    else:
        _hat = 0

    if (_hat < max(_left, _right)) or (int(i)==1):
        n_splits = n_splits + 1
        #print(f"Beam splits at {split}")

print(f"How many times will the beam be split? {n_splits}")
# 1541