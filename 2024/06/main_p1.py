import numpy as np

puzzle_input = "2024/inputs/06_input.txt"
#puzzle_input = "2024/inputs/06_sample.txt"

#If there is something directly in front of you, turn right 90 degrees.
#Otherwise, take a step forward.

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

room = []
for line in lines:
    # Convert lines into a numpy matrix
    room.append(list(line.replace("\n","")))

room = np.array(room)

def new_direction(curr_dir):

    if curr_dir == "up":
        new_dir = "right"
    elif curr_dir == "right":
        new_dir = "down"
    elif curr_dir == "down":
        new_dir = "left"
    elif curr_dir == "left":
        new_dir = "up"

    return new_dir


def is_out_room(pos, room):
    if pos[0] < 0 or pos[0] >= room.shape[0] or pos[1] < 0 or pos[1] >= room.shape[1]:
        return True
    return False


# Find starting position marked as "^" and obstacles marked as "#"
i,j = np.where(room == "^")
obstacles = np.where(room == "#")
positions = set()
positions.add((i.tolist()[0], j.tolist()[0]))
curr_dir = "up"

while is_out_room([i, j], room) == False:
    
    # Move forward
    if curr_dir == "up":
        new_pos = [i-1, j]
    elif curr_dir == "right":
        new_pos = [i, j + 1]
    elif curr_dir == "down":
        new_pos = [i+1, j]
    elif curr_dir == "left":
        new_pos = [i, j - 1]

    # Check if the guard is facing an obstacle
    if (new_pos[0], new_pos[1]) in list(zip(obstacles[0], obstacles[1])):
        #print(f"Obstacle at position {new_pos}")
        # Turn right
        curr_dir = new_direction(curr_dir)
        #print(f"New direction: {curr_dir}")
    else:
        positions.add((new_pos[0].tolist()[0], new_pos[1].tolist()[0]))
        #print(f"Positions {positions}")
        i, j = new_pos

print(f"How many distinct positions will the guard visit before leaving the mapped area? {len(positions)-1}")
#5208