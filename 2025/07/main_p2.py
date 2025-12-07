import numpy as np

puzzle_input = "2025/inputs/07_input.txt"
#puzzle_input = "2025/inputs/07_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    board = []
    for line in lines:
        line = list(line.replace("\n",""))
        board.append(line)
    
    board = np.array(board)

    return board

board = read_puzzle_input(puzzle_input)
start = np.argwhere(board == 'S')[0]

# Create a paths board to count paths
paths = np.zeros(board.shape, dtype=int)
paths[start[0], start[1]] = 1

# Process row by row from top to bottom
for row in range(board.shape[0] - 1):
    for col in range(board.shape[1]):
        if paths[row, col] == 0:
            continue
            
        # Check if current position is a splitter
        if board[row, col] == '^':
            # Split: go down-left and down-right
            if col > 0:
                paths[row + 1, col - 1] += paths[row, col]
            if col < board.shape[1] - 1:
                paths[row + 1, col + 1] += paths[row, col]
        else:
            # Normal: go straight down
            paths[row + 1, col] += paths[row, col]

print(f"How many different paths exist? {sum(paths[-1, :])}")
# 80158285728929