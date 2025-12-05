puzzle_input = "2025/inputs/05_input.txt"
#puzzle_input = "2025/inputs/05_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    ranges = []

    for line in lines:
        if line == "\n":
            break
        else:     
            line = line.replace('\n','')
            min_range, max_range = line.split("-")
            min_range = int(min_range)
            max_range = int(max_range)
            ranges.append([min_range, max_range])

    return ranges

ranges = read_puzzle_input(puzzle_input)

# Sort the ranges by the starting number. 
ranges.sort() 
merged_ranges = [ranges[0]]

for current_start, current_end in ranges[1:]:

    last_start, last_end = merged_ranges[-1]
    
    # Check for overlap
    if current_start <= last_end + 1: 
        # Merge
        new_end = max(last_end, current_end)
        merged_ranges[-1] = (last_start, new_end)
    else:
        # No merge
        merged_ranges.append((current_start, current_end))

# Calculate the total count from the clean, non-overlapping list
total_fresh = 0
for start, end in merged_ranges:
    total_fresh = total_fresh + (end - start + 1)

print(f"How many of the available ingredient IDs are fresh? {total_fresh}")
# 352509891817881