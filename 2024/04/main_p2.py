
puzzle_input = "2024/inputs/04_input.txt"
#puzzle_input = "2024/inputs/04_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()

board = []
for line in lines:
    board.append(list(line.replace("\n","")))

def find_xmas(i, j, board, verbose=False):
    # find all directions the word "XMAS" appears in board
    xmas = 0

    # find right down right up
    try:
        if (i+1) < len(board) and (i-1) >= 0 and (j+1) < len(board[i]) and (j-1) >= 0:
            if board[i-1][j-1] == "M" and board[i-1][j+1] == "S" \
                and board[i+1][j-1] == "M" and board[i+1][j+1] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found X-MAS right down right up")
    except IndexError:
        pass
    
    # find right down left down
    try:
        if (i+1) < len(board) and (i-1) >= 0 and (j+1) < len(board[i]) and (j-1) >= 0:
            if board[i-1][j-1] == "M" and board[i-1][j+1] == "M" \
                and board[i+1][j-1] == "S" and board[i+1][j+1] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found X-MAS right down left down")
    except IndexError:
        pass

    # find left up left down
    try:
        if (i+1) < len(board) and (i-1) >= 0 and (j+1) < len(board[i]) and (j-1) >= 0:
            if board[i-1][j-1] == "S" and board[i-1][j+1] == "M" \
                and board[i+1][j-1] == "S" and board[i+1][j+1] == "M":
                xmas = xmas + 1
                if verbose:
                    print(f"Found X-MAS left up left down")
    except IndexError:
        pass

    # find left up right up
    try:
        if (i+1) < len(board) and (i-1) >= 0 and (j+1) < len(board[i]) and (j-1) >= 0:
            if board[i-1][j-1] == "S" and board[i-1][j+1] == "S" \
                and board[i+1][j-1] == "M" and board[i+1][j+1] == "M":
                xmas = xmas + 1
                if verbose:
                    print(f"Found X-MAS left up right up")
    except IndexError:
        pass

    return xmas


sum_xmas = 0
for row in range(len(board)):
    
    #Find all Xs in the row
    x_index = [i for i in range(len(board[row])) if board[row][i] == "A"]
    
    for col in x_index:
        sum_xmas = sum_xmas + find_xmas(i=row, j=col, board=board, verbose=False)

print(f"How many times does an X-MAS appear? {sum_xmas}")
#2003