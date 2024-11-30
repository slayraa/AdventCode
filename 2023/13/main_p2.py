
import numpy as np

puzzle_input = "2023/inputs/13.txt"
#puzzle_input = "2023/inputs/13_sample.txt"

# Read the text file
with open(puzzle_input, "r") as f:
    lines = f.read().splitlines()

# Divide the puzzles
puzzles = []
puzzle = []
for line in lines:
    if len(line) != 0:
        puzzle.append(line)
    else:
        puzzles.append(puzzle)
        puzzle = []
puzzles.append(puzzle)

lines = []
columns = []
puzzle_dict = {}
ct = 0
for puzzle in puzzles:

    # Convert puzzle into numpy matrix
    m_puzzle = np.array([list(line.replace("\n","").strip()) for line in puzzle])
    
    # Check horizontal
    is_horizontal = False
    for i in range(m_puzzle.shape[0]-1):
        if np.all(m_puzzle[i,:] == m_puzzle[i+1,:]):
            max_ref = min((m_puzzle.shape[0] - (i+1)), (i+1))

            if max_ref == (i+1):
                above = m_puzzle[:max_ref, :]
                below = m_puzzle[max_ref:(max_ref+i+1), :]
            else:
                above = m_puzzle[(i+1-max_ref):(i+1), :]
                below = m_puzzle[(i+1):m_puzzle.shape[0]]
            
            if np.all(np.flip(above, axis=0) == below):
                lines.append(i+1)
                is_horizontal = True
                ct = ct+1
                puzzle_dict[ct] = (i+1, "")
                break
    
    if not is_horizontal:
        for i in range(m_puzzle.shape[1]-1):
            if np.all(m_puzzle[:,i] == m_puzzle[:,i+1]):
                max_ref = min((m_puzzle.shape[1] - (i+1)), (i+1))

                if max_ref == (i+1):
                    left = m_puzzle[:, :max_ref]
                    right = m_puzzle[:, max_ref:(max_ref+i+1)]
                else:
                    left = m_puzzle[:, (i+1-max_ref):(i+1)]
                    right = m_puzzle[:, (i+1):m_puzzle.shape[1]]
                
                if np.all(np.flip(left, axis=1) == right):
                    columns.append(i+1)
                    ct = ct+1
                    puzzle_dict[ct] = ("", i+1)
                    break

final_sum = np.sum(columns) + np.sum(lines)*100

print(f"What number do you get after summarizing all of your notes? Answer: {final_sum}")
# Sample is 400
# 