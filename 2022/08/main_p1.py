import numpy as np

#puzzle_input = "08/sample.txt"
puzzle_input = "08/input.txt"

data = np.genfromtxt(puzzle_input, dtype=str)

# Build forest
forest = []
for row in data:
    forest.append([int(i) for i in row])

forest = np.array(forest)

# count trees at grid
grid_trees = (len(forest) + len(forest[0]))*2-4

#count visible trees
visible = 0
for i in range(1, len(forest)-1):
    for j in range(1, len(forest[0])-1):
        tree = forest[i, j]
        vis = False
        
        # left
        if forest[i, 0:j].max() < tree:
            vis = True
        
        #right
        elif forest[i, j+1:len(forest[0])].max() < tree:
            vis = True
        
        #up
        elif forest[0:i, j].max() < tree:
            vis = True
        
        # down
        elif forest[i+1:len(forest), j].max() < tree:
            vis = True
        
        if vis:
            visible = visible + 1

ans = grid_trees + visible
print(f"how many trees are visible from outside the grid? Answer: {ans}")
# 1835    
