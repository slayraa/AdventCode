import re
from collections import Counter
from matplotlib import pyplot as plt

puzzle_input = "2024/inputs/14_input.txt"

board_width = 101
board_height = 103

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

# Parse the robot positions and velocity
positions = []
velocities = []

#for line in lines:
#        digits = re.findall(r'-*\d+', line)
#        positions.append([int(digits[0]), int(digits[1])])
#        velocities.append([int(digits[2]), int(digits[3])])

def draw_fig(simulation_time, positions, save=True):
    # Print board and maintain aspect ratio
    fig, ax = plt.subplots()

    _ = plt.xlim(0, board_width)
    _ = plt.ylim(0, board_height)

    for robot in positions:
        _ = ax.annotate('#', (robot[1], robot[0]), color='black', fontsize=10, ha='center', va='center')

    if save:
        plt.savefig(f'2024/14/images/output_image_{simulation_time}.png', bbox_inches='tight', pad_inches=0)
        plt.close(fig)
    else:
        plt.show()
    plt.close

    print(f"Image saved at 2024/14/images/output_image_{simulation_time}.png")


for simulation_time in range(10000):

    positions = []
    velocities = [] 
    for line in lines:
        digits = re.findall(r'-*\d+', line)
        positions.append([int(digits[0]), int(digits[1])])
        velocities.append([int(digits[2]), int(digits[3])])

    # Simulate the movement of the robots after simulation_time
    for i in range(len(positions)):
        positions[i][0] = (positions[i][0] + (velocities[i][0] * simulation_time)) % board_width
        positions[i][1] = (positions[i][1] + (velocities[i][1] * simulation_time)) % board_height
    
    # Find a long horizontal or vertical line in the board
    vert = Counter([pos[0] for pos in positions])
    horiz = Counter([pos[1] for pos in positions])

    if (vert.most_common(2)[0][1] > 35) and ((vert.most_common(2)[1][1] > 30)):
        draw_fig(simulation_time, positions)
    
    if (horiz.most_common(2)[0][1] > 35) and ((horiz.most_common(2)[1][1] > 30)):
        draw_fig(simulation_time, positions)


print(f"What is the fewest number of seconds that must elapse for the robots to display the Easter egg?")
#6243