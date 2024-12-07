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


# Find starting position marked as "^" and obstacles marked as "#"
obstacles = np.where(room == "#")
obstacles = set(zip(obstacles[0], obstacles[1]))
loops = 0

for obsti in range(len(room)):
    for obstj in range(len(room[0])):

        #print(f"Checking for obstacle {(obsti,obstj)}")

        i,j = np.where(room == "^")
        obstacles_new = obstacles.copy()
        obstacles_new.add((obsti,obstj))
        count_dir = 0
        loop = False
        curr_dir = "up"
        positions_dict = {}
        positions_dict[(i.tolist()[0], j.tolist()[0])] = curr_dir

        while (loop == False) and (is_out_room([i, j], room) == False):
            
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
            if {(new_pos[0].tolist()[0], new_pos[1].tolist()[0])}.issubset(obstacles_new):
                #print(f"Obstacle at position {new_pos}")
                # Turn right
                curr_dir = new_direction(curr_dir)
            
            else:
                new_pos_easy = (new_pos[0].tolist()[0], new_pos[1].tolist()[0])
                if new_pos_easy in positions_dict.keys():

                    if (positions_dict.get(new_pos_easy) == curr_dir) and is_adjacent(new_pos, [obsti, obstj]):
                        loop = True
                        loops = loops + 1
                        #print(f"Loop for obstacle {(obsti,obstj)} looping at position {new_pos_easy}")
                
                i, j = new_pos
                positions_dict[new_pos_easy] = curr_dir

print(f"How many different positions could you choose for this obstruction? {loops}")
#5208