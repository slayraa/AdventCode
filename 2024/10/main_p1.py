import networkx as nx
import numpy as np

puzzle_input = "2024/inputs/10_input.txt"
#puzzle_input = "2024/inputs/10_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

board = [list(line.replace("\n","")) for line in lines]
board = np.array(board)

def add_edges(G, trailhead, board):

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (i == 0 and j == 0) or (i*j != 0):
                continue
            elif (trailhead[0] + i) < len(board) and (trailhead[0] + i) >= 0 \
                and (trailhead[1] + j) < len(board[0]) and (trailhead[1] + j) >= 0:
                
                if int(board[trailhead[0] + i][trailhead[1] + j]) == (int(board[trailhead]) + 1):
                    G.add_node((trailhead[0] + i, trailhead[1] + j))
                    G.add_edge(trailhead, (trailhead[0] + i, trailhead[1] + j))
    
    return G


trailheads = np.where(board == "0")
trailheads = list(zip(trailheads[0], trailheads[1]))
scores = dict()
height = 9

# Create a graph per trailhead where there is a connector between two nodes if their difference is 1
for trailhead in trailheads:
    G = nx.Graph()
    G.add_node(trailhead)

    new_trailheads = [trailhead]
    curr_height = 0

    while (len(new_trailheads) > 0) and (curr_height < (height+1)):
        
        new_trailheads = [node for node in G.nodes if int(board[node]) == curr_height]
        for th in new_trailheads:
            G = add_edges(G, th, board)
        
        curr_height += 1
    
    if curr_height == 10:
        scores[trailhead] = len(new_trailheads)

print(f"What is the sum of the scores of all trailheads on your topographic map? {sum(scores.values())}")
#786