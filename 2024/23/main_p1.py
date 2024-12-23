import networkx as nx
import re

puzzle_input = "2024/inputs/23_input.txt"
#puzzle_input = "2024/inputs/23_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

G = nx.Graph()

for line in lines:
    nodes = re.findall(r"\w+", line)
    G.add_edge(nodes[0], nodes[1])

# Find all the connected components of length x
max_len = 3
letter = 't'

nodes_l = [n for n in G.nodes if n[0] == letter]
tri_cliques = [x for x in nx.enumerate_all_cliques(G) if len(x)==max_len]

# Find all paths of max_len that connect to nodes_t
t_cycles = 0
for path in tri_cliques:
    if sum([n in path for n in nodes_l]) > 0:
        t_cycles = t_cycles + 1


print(f"How many contain at least one computer with a name that starts with t? {t_cycles}")
#1083