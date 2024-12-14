import re

puzzle_input = "2024/inputs/14_input.txt"
#puzzle_input = "2024/inputs/14_sample.txt"

board_width = 101
board_height = 103

#board_width = 11
#board_height = 7

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

# Parse the robot positions and velocity
positions = []
velocities = []

for line in lines:
        digits = re.findall(r'-*\d+', line)
        positions.append([int(digits[0]), int(digits[1])])
        velocities.append([int(digits[2]), int(digits[3])])

simulation_time = 100 #seconds

# Simulate the movement of the robots after simulation_time
for i in range(len(positions)):
    #print(f"Robot {i} starts at {positions[i]} and has velocity {velocities[i]}")
    positions[i][0] = (positions[i][0] + (velocities[i][0] * simulation_time)) % board_width
    positions[i][1] = (positions[i][1] + (velocities[i][1] * simulation_time)) % board_height
    #print(f"Robot {i} ends at {positions[i]}")

# Count the number of robots in each quadrant
quadrants = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

for i in range(len(positions)):
    #print(f"Robot {i} is at {positions[i]}")
    if positions[i][0] < board_width//2 and positions[i][1] < board_height//2:
        quadrants["Q1"] = quadrants["Q1"] + 1
        #print(f"Robot {i} is in Q1")
    elif positions[i][0] > board_width//2 and positions[i][1] < board_height//2:
        quadrants["Q2"] = quadrants["Q2"] + 1
        #print(f"Robot {i} is in Q2")
    elif positions[i][0] < board_width//2 and positions[i][1] > board_height//2:
        quadrants["Q3"] = quadrants["Q3"] + 1
        #print(f"Robot {i} is in Q3")
    elif positions[i][0] > board_width//2 and positions[i][1] > board_height//2:
        quadrants["Q4"] = quadrants["Q4"] + 1
        #print(f"Robot {i} is in Q4")

# Multiply the values of the quadrants
safety = quadrants["Q1"] * quadrants["Q2"] * quadrants["Q3"] * quadrants["Q4"]

print(f"What will the safety factor be after exactly 100 seconds have elapsed? {safety}")
#222901875