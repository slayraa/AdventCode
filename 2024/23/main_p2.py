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
cliques = [x for x in nx.enumerate_all_cliques(G)]
max_len = max([len(x) for x in cliques])
max_clique = sorted([x for x in cliques if len(x) == max_len][0])
password = ','.join(max_clique)

print(f"What is the password to get into the LAN party? {password}")
#as,bu,cp,dj,ez,fd,hu,it,kj,nx,pp,xh,yu