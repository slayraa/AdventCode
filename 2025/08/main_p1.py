import numpy as np
import re

puzzle_input = "2025/inputs/08_input.txt"
#puzzle_input = "2025/inputs/08_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    jct_boxes = []
    for line in lines:
        coords = re.findall(r'\d+', line)
        jct_boxes.append(coords)
    
    jct_boxes = np.array(jct_boxes).astype(float)
    
    return jct_boxes

def find_n_closest_pairs(boxes, triu_indices, pairs_distances, n):
    
    n_closest_pairs = []

    # Get n-th closest pairs
    n_smallest_idx = np.argpartition(pairs_distances, min(n, len(pairs_distances)-1))[:n]
    n_smallest_sorted = n_smallest_idx[np.argsort(pairs_distances[n_smallest_idx])]

    for idx in n_smallest_sorted:
        i = triu_indices[0][idx]
        j = triu_indices[1][idx]
        n_closest_pairs.append((boxes[i], boxes[j]))

    return n_closest_pairs

def dist_matrix(boxes):

    distances = boxes[:, None, :] - boxes[None, :, :]
    dist_matrix = np.linalg.norm(distances, axis=2)

    #Set diagonal to infinity
    np.fill_diagonal(dist_matrix, np.inf)

    # Get upper triangle to avoid duplicates
    triu_indices = np.triu_indices_from(dist_matrix, k=1)
    pairs_distances = dist_matrix[triu_indices]

    return triu_indices, pairs_distances


jct_boxes = read_puzzle_input(puzzle_input)
n_shortest_connections = 1000
triu_indices, pairs_distances = dist_matrix(jct_boxes)
n_closest_pairs = find_n_closest_pairs(jct_boxes, triu_indices, pairs_distances,n=n_shortest_connections)
connected_boxes = []

for pair in n_closest_pairs:
    circuit_with_0 = None
    circuit_with_1 = None

    # Find which circuits contain pair[0] and pair[1]
    for circuit in connected_boxes:
        if any(np.array_equal(pair[0], connected_box) for connected_box in circuit):
            circuit_with_0 = circuit
        if any(np.array_equal(pair[1], connected_box) for connected_box in circuit):
            circuit_with_1 = circuit

    # Case 1: Both elements are in different circuits - merge them
    if circuit_with_0 is not None and circuit_with_1 is not None and circuit_with_0 is not circuit_with_1:
        # Add all elements from circuit_with_1 to circuit_with_0 (avoiding duplicates)
        for box in circuit_with_1:
            if not any(np.array_equal(box, existing_box) for existing_box in circuit_with_0):
                circuit_with_0.append(box)
        # Remove circuit_with_1 from connected_boxes using index
        idx_to_remove = next(i for i, circuit in enumerate(connected_boxes) if circuit is circuit_with_1)
        connected_boxes.pop(idx_to_remove)

    # Case 2: Only pair[0] is in a circuit - add pair[1]
    elif circuit_with_0 is not None and circuit_with_1 is None:
        if not any(np.array_equal(pair[1], connected_box) for connected_box in circuit_with_0):
            circuit_with_0.append(pair[1])

    # Case 3: Only pair[1] is in a circuit - add pair[0]
    elif circuit_with_1 is not None and circuit_with_0 is None:
        if not any(np.array_equal(pair[0], connected_box) for connected_box in circuit_with_1):
            circuit_with_1.append(pair[0])

    # Case 4: Neither element is in any circuit - create new circuit
    elif circuit_with_0 is None and circuit_with_1 is None:
        connected_boxes.append(list(pair))

top_3_longest = sorted(connected_boxes, key=len, reverse=True)[:3]
circuit_sizes = [len(circuit) for circuit in top_3_longest]

print(f"what do you get if you multiply together the sizes of the three largest circuits? {np.prod(circuit_sizes)}")
# 90036
