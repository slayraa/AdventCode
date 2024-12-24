import networkx as nx

puzzle_input = "2024/inputs/18_input.txt"
#puzzle_input = "2024/inputs/18_sample.txt"

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
start = (0,0)
end = (len_board,len_board)


for number_bytes in range(len(bytes),0,-1):
    G = nx.Graph()

    if number_bytes % 20 == 0:
        print(f"Number of bytes: {number_bytes}")
    
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
    
    try: 
        if nx.has_path(G, source=start, target=end):
            coords = bytes[number_bytes]
            break
    except:
        continue

print(f"What are the coordinates of the first byte that will prevent the exit from being reachable from your starting position? {coords[1], coords[0]}")
# 51,40