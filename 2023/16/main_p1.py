
puzzle_input = "2023/inputs/15.txt"
#puzzle_input = "2023/inputs/15_sample.txt"

# Read the text file
with open(puzzle_input, "r") as f:
    lines = f.read().splitlines()

lines = lines[0].split(",")

results = []
for line in lines:
    curr_val = 0

    for ch in line:
        curr_val = curr_val + ord(ch)
        curr_val = curr_val * 17
        curr_val = curr_val % 256
    
    results.append(curr_val)
        

print(f"What is the sum of the results? Answer: {sum(results)}")
# Sample is 1320
# 505427