import numpy as np
import re
from math import prod

puzzle_input = "2025/inputs/06_input.txt"
#puzzle_input = "2025/inputs/06_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    board = []
    for line in lines:
        numbers = re.findall(r'\d+', line)

        if len(numbers)>0:
            board.append(numbers)
        else:
            ops = line.split(" ")
            ops = [sym for sym in ops if len(sym)>0]
    
    board = np.array(board)
    board = board.astype(np.int64)

    return board, ops

board, ops = read_puzzle_input(puzzle_input)
col_totals = []

for i in range(len(ops)):
    if ops[i] == '+':
        col_totals.append(board[:,i].sum())
    elif ops[i] == '*':
        col_totals.append(prod(board[:,i]))
    else:
        print(f'Operation {ops[i]} not found.')

print(f"What is the grand total found by adding together all of the answers to the individual problems? {sum(col_totals)}")
# 4878670269096