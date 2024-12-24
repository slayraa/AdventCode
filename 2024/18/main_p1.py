import networkx as nx

puzzle_input = "2024/inputs/18_input.txt"
puzzle_input = "2024/inputs/18_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

bytes = []
for line in lines:
    bytes.append([int(line.split(",")[1].strip()), 
                  int(line.split(",")[0].strip())])

# Create a graph where each node is a cell on the board that is not corrupted
len_board = 70
number_bytes = 1024

G = nx.Graph()
for i in range(len_board+1):
    for j in range(len_board+1):
        if [i,j] not in bytes[:(number_bytes)]:
            # Add an edge between node [i,j] and its neighbouts if not a byte
            if i > 0 and [i-1,j] not in bytes[:(number_bytes)]:
                G.add_edge((i,j),(i-1,j))
            if i < len_board-1 and [i+1,j] not in bytes[:(number_bytes)]:
                G.add_edge((i,j),(i+1,j))
            if j > 0 and [i,j-1] not in bytes[:(number_bytes)]:
                G.add_edge((i,j),(i,j-1))
            if j < len_board-1 and [i,j+1] not in bytes[:(number_bytes)]:
                G.add_edge((i,j),(i,j+1))

# Find the shortest path from the start to the end
start = (0,0)
end = (len_board,len_board)
steps = nx.shortest_path_length(G, source=start, target=end)

print(f"What is the minimum number of steps needed to reach the exit? {steps}")
# 270