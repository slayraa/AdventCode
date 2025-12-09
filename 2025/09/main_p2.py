import numpy as np
import re
from shapely.geometry import Point, Polygon

puzzle_input = "2025/inputs/09_input.txt"
#puzzle_input = "2025/inputs/09_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    squares = []
    for line in lines:
        coords = re.findall(r'\d+', line)
        squares.append(coords)
    
    squares = np.array(squares).astype(float)
    
    return squares

squares = read_puzzle_input(puzzle_input)
square_polygon = Polygon(squares)

# For each pair of points, calculate the distance between them
dist_pairs = {}
for i in range(len(squares)):
    for j in range(i+1, len(squares)):
        pair = [squares[i], squares[j]]
        dist = (np.abs(squares[j][0] - squares[i][0]) + 1) * (np.abs(squares[j][1] - squares[i][1]) + 1)
        dist_pairs[(i,j)] = dist

# sort pairs by values (distance)
sorted_dist_keys = sorted(dist_pairs, key=dist_pairs.get, reverse=True)

# For each pair, check if the rectangle defined by the pair is fully within the polygon
for key in sorted_dist_keys:
    p1 = squares[key[0]]
    p2 = squares[key[1]]
    
    rectangle = Polygon(
        [(p1[0], p1[1]),
        (p1[0], p2[1]),
        (p2[0], p2[1]),
        (p2[0], p1[1])]
        )
    
    if square_polygon.contains(rectangle):
        best_pair = [squares[key[0]], squares[key[1]]]
        best_distance = dist_pairs[key]
        break

print(f"what is the largest area of any rectangle you can make using only red and green tiles? {best_distance}")
# 1572047142