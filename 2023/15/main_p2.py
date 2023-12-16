import re

puzzle_input = "2023/inputs/15.txt"
#puzzle_input = "2023/inputs/15_sample.txt"

# Read the text file
with open(puzzle_input, "r") as f:
    lines = f.read().splitlines()

lines = lines[0].split(",")


def hashmap(line):

    curr_val = 0
    for ch in line:
        curr_val = curr_val + ord(ch)
        curr_val = curr_val * 17
        curr_val = curr_val % 256
    
    return curr_val


boxes = dict()
for line in lines:

    # Split line on = or -     
    line_parts = re.split(r"=|-", line)
    label = line_parts[0]
    box = hashmap(label)

    # If "=" then change focus if exists, or append if it doesn't
    if "=" in line:
        focus = int(line_parts[1])

        # Check if it already exists
        lens_exists = False
        if boxes.get(box) is None:
            boxes[box] = [[label, focus]]
        
        else:
            for pair in boxes.get(box):
                if pair[0] == label:
                    pair[1] = focus
                    lens_exists = True
                    break
        
            # If not add it last
            if not lens_exists:
                boxes[box].append([label, focus])
    
    # If "-" then remove the lens
    else:
        if boxes.get(box) is not None:
            for pair in boxes.get(box):
                if pair[0] == label:
                    boxes.get(box).remove(pair)
                    break


# Calculate the focusing power of all boxes   
focus_power = 0
for kbox in boxes.keys():
    
    for ipair in range(len(boxes.get(kbox))):
        curr_value = (kbox+1)*(ipair+1)*boxes.get(kbox)[ipair][1]
        focus_power = focus_power + curr_value

print(f"What is the focusing power of the resulting lens configuration? Answer: {focus_power}")
# Sample is 145
# 243747
