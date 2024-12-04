
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

    # find vertically
    try:
        if (i+3) < len(board):
            if board[i+1][j] == "M" and board[i+2][j] == "A" and board[i+3][j] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found XMAS down")
    except IndexError:
        pass

    try:
        if (i-3) >= 0:
            if board[i-1][j] == "M" and board[i-2][j] == "A" and board[i-3][j] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found XMAS up")
    except IndexError:
        pass

    # find horizontally
    try:
        if (j+3) < len(board[i]):
            if board[i][j+1] == "M" and board[i][j+2] == "A" and board[i][j+3] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found XMAS right")
    except IndexError:
        pass
        
    try:
        if (j-3) >= 0:
            if board[i][j-1] == "M" and board[i][j-2] == "A" and board[i][j-3] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found XMAS left")
    except IndexError:
        pass
    
    # find diagonally
    try:
        if (i+3) < len(board) and (j+3) < len(board[i]):
            if board[i+1][j+1] == "M" and board[i+2][j+2] == "A" and board[i+3][j+3] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found XMAS down right")
    except IndexError:
        pass
        
    try:
        if ((i-3)>=0) and (j-3)>=0:
            if board[i-1][j-1] == "M" and board[i-2][j-2] == "A" and board[i-3][j-3] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found XMAS up left")
    except IndexError:
        pass
        
    try:
        if (i+3) < len(board) and (j-3) >= 0:
            if board[i+1][j-1] == "M" and board[i+2][j-2] == "A" and board[i+3][j-3] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found XMAS down left")
    except IndexError:
        pass

    try:
        if (i-3) >= 0 and (j+3) < len(board[i]):
            if board[i-1][j+1] == "M" and board[i-2][j+2] == "A" and board[i-3][j+3] == "S":
                xmas = xmas + 1
                if verbose:
                    print(f"Found XMAS up right")
    except IndexError:
        pass

    return xmas


sum_xmas = 0
for row in range(len(board)):
    
    #Find all Xs in the row
    x_index = [i for i in range(len(board[row])) if board[row][i] == "X"]
    
    for col in x_index:
        sum_xmas = sum_xmas + find_xmas(i=row, j=col, board=board, verbose=False)

print(f"How many times does XMAS appear? {sum_xmas}")
#2549