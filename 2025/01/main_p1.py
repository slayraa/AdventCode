puzzle_input = "2025/inputs/01_input.txt"
#puzzle_input = "2025/inputs/01_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    lines = [line.replace("\n","") for line in lines]
    
    return lines

curr_pos = 50
numb_0 = 0
instructions = read_puzzle_input(puzzle_input)

for inst in instructions:
    if inst[0] == "L":
        curr_pos = (curr_pos - int(inst[1:])) % 100
    elif inst[0] == "R":
        curr_pos = (curr_pos + int(inst[1:])) % 100
    
    if curr_pos == 0:
        numb_0 = numb_0 + 1

print(f"What's the actual password to open the door? {numb_0}")
# 1118