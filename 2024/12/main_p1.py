import numpy as np

puzzle_input = "2024/inputs/12_input.txt"
#puzzle_input = "2024/inputs/12_sample.txt"
#puzzle_input = "2024/inputs/12_sample_1.txt"
#puzzle_input = "2024/inputs/12_sample_2.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

board = []
for line in lines:
    # Convert each line into a list of characters
    board.append(list(line.replace("\n","")))

board = np.array(board)

def find_adjacent_symbols(board, pos, curr_symbol, visited=None):

    dirs = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    if visited[pos[0]][pos[1]]:
        return []
    
    visited[pos[0]][pos[1]] = True
    adjacent_symbols = [pos]
    
    for dir in dirs:
        r, c = pos[0] + dir[0], pos[1] + dir[1]
        if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] == curr_symbol:
            adjacent_symbols.extend(find_adjacent_symbols(board, [r, c], curr_symbol, visited))

    return adjacent_symbols


symbols = np.unique(board)
area = []
perimeter = []

for i in range(len(board)):
    for j in range(len(board[i])):
        curr_symbol = board[i][j]
        visited = np.zeros(board.shape, dtype=bool)

        if curr_symbol != "o":
            # Find all adjacent symbols that are the same as the current symbol
            # If there are no adjacent symbols, the area is 1
            adjacent_symbols = find_adjacent_symbols(board, [i, j], curr_symbol, visited)
            area.append(len(adjacent_symbols))

            if len(adjacent_symbols) == 1:
                perimeter.append(4)
            else:
                # Calculate the perimeter of the region
                perim_adjacent = 0
                for symb in adjacent_symbols:
                    if symb[0] - 1 >= 0 and board[symb[0]-1][symb[1]] != curr_symbol:
                        perim_adjacent = perim_adjacent + 1
                    if symb[1] - 1 >= 0 and board[symb[0]][symb[1]-1] != curr_symbol:
                        perim_adjacent = perim_adjacent + 1
                    if symb[0] + 1 < len(board) and board[symb[0]+1][symb[1]] != curr_symbol:
                        perim_adjacent = perim_adjacent + 1
                    if symb[1] + 1 < len(board[symb[0]]) and board[symb[0]][symb[1]+1] != curr_symbol:
                        perim_adjacent = perim_adjacent + 1

                    # If the current symbol is at the edge of the board, add 1 to the perimeter
                    if symb[1]+1 >= len(board[symb[0]]):
                        perim_adjacent = perim_adjacent + 1
                    
                    if symb[0]+1 >= len(board):
                        perim_adjacent = perim_adjacent + 1
                    
                    if symb[1]-1 < 0:
                        perim_adjacent = perim_adjacent + 1
                    
                    if symb[0]-1 < 0:
                        perim_adjacent = perim_adjacent + 1
                    
                perimeter.append(perim_adjacent)
                
            #print(f"Symbol: {curr_symbol}, Area: {len(adjacent_symbols)}, Perimeter: {perimeter[-1]}")

            # Change the adjacent symbols in board to show as visited
            for symb in adjacent_symbols:
                board[symb[0]][symb[1]] = "o"

price = 0
for i in range(len(area)):
    #print(f"Area: {a}, Perimeter: {p}")
    price = price + (area[i] * perimeter[i])

print(f"What is the total price of fencing all regions on your map? {price}")
#1477924

