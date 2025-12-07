import numpy as np
from math import prod
import re

puzzle_input = "2025/inputs/06_input.txt"
#puzzle_input = "2025/inputs/06_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    board = []
    for line in lines[:-1]:
        line = line.replace("\n","")
        line = re.sub(r'\s', '.', line)
        board.append(list(line))
    
    board = np.array(board)
    board = board.astype(str)

    ops = lines[-1].split(" ")
    ops = [sym for sym in ops if len(sym)>0]

    return board, ops

board, ops = read_puzzle_input(puzzle_input)
only_dot_columns = [
    col_idx 
    for col_idx in range(len(board[0])) 
    if all(row[col_idx] == '.' for row in board)
]
only_dot_columns.append(board.shape[1])
prev_max_col_len=0
col_totals = []

for j in range(len(ops)):
    # Find correct numbers
    col_numbers = []
    max_col_len = only_dot_columns[j]

    for u in range(prev_max_col_len, max_col_len):
        number_str = ''
        for number in board[:,u]:
            if number != '.':
                number_str = number_str + number
        
        col_numbers.append(int(number_str))
    
    prev_max_col_len = max_col_len + 1
    #print(f"New column is {col_numbers} with op {ops[j]}")

    # Proceed with the operations
    if ops[j] == '+':
        col_totals.append(sum(col_numbers))
    elif ops[j] == '*':
        col_totals.append(prod(col_numbers))
    else:
        print(f'Operation {ops[j]} not found.')

print(f"What is the grand total found by adding together all of the answers to the individual problems? {sum(col_totals)}")
# sample = 3263827
# 8674740488592