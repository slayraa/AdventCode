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
    
    # Calculate full circles
    revolutions = int(inst[1:]) // 100
    
    # Remove those full circles from the step instruction
    step = int(inst[1:]) % 100
    
    if inst[0] == "L":
        # FIX: Add "and curr_pos > 0"
        if (curr_pos - step) <= 0 and curr_pos > 0:
            revolutions = revolutions + 1
            
        curr_pos = (curr_pos - step) % 100
        
    else: # Right
        if (curr_pos + step) >= 100:
            revolutions = revolutions + 1
            
        curr_pos = (curr_pos + step) % 100
        
    numb_0 = numb_0 + revolutions

    #print(f"Dial is now at {curr_pos}. Passed zero {revolutions} times.")

print(f"What's the actual password to open the door? {numb_0}")
# 6458 - too high
# 6357 - too high
# 6354 - too high
# 6289
