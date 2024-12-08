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


def is_adjacent(pos, obstacle):
    if [pos[0] + 1, pos[1]] == obstacle:
        return True
    elif [pos[0] - 1, pos[1]] == obstacle:
        return True
    elif [pos[0], pos[1] + 1] == obstacle:
        return True
    elif [pos[0], pos[1] - 1] == obstacle:
        return True
    return False


def is_loop(start_pos, start_dir, room, obstacles):

    curr_dir = start_dir
    i, j = start_pos
    positions_dict = {}
    positions_dict[(i.tolist()[0], j.tolist()[0])] = curr_dir
    
    while (is_out_room([i, j], room) == False):
    
        # Move forward
        if curr_dir == "up":
            new_pos = [i-1, j]
        elif curr_dir == "right":
            new_pos = [i, j + 1]
        elif curr_dir == "down":
            new_pos = [i+1, j]
        elif curr_dir == "left":
            new_pos = [i, j - 1]
        
        new_pos_easy = (new_pos[0].tolist()[0], new_pos[1].tolist()[0])

        # Check if the guard is facing an obstacle
        if {new_pos_easy}.issubset(obstacles):
            #print(f"Obstacle at position {new_pos}")
            # Turn right
            curr_dir = new_direction(curr_dir)

        else:
            if new_pos_easy in positions_dict.keys():
                if positions_dict.get(new_pos_easy) == curr_dir:
                    return True
            
            positions_dict[new_pos_easy] = curr_dir
            i, j = new_pos
    
    return False


# Find starting position marked as "^" and obstacles marked as "#"
i,j = np.where(room == "^")
start_pos = np.where(room == "^")
obstacles = np.where(room == "#")
positions = set()
positions.add((i.tolist()[0], j.tolist()[0]))
curr_dir = "up"
loops = set()

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
        # Turn right
        curr_dir = new_direction(curr_dir)

    else:
        # Check if current new position can be a new obstacle for loops
        new_pos_easy = (new_pos[0].tolist()[0], new_pos[1].tolist()[0])
        new_obstacles = list(zip(obstacles[0], obstacles[1])).copy()
        new_obstacles.append(new_pos_easy)

        if is_loop(start_pos, "up", room, new_obstacles):
            loops.add(new_pos_easy)
            print(f"Loop at position {new_pos_easy}")

        positions.add(new_pos_easy)
        #print(f"Positions {positions}")
        i, j = new_pos

print(f"How many different positions could you choose for this obstruction? {len(loops)}")
#1972