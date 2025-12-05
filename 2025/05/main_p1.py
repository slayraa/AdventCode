puzzle_input = "2025/inputs/05_input.txt"
#puzzle_input = "2025/inputs/05_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    ranges = []
    ingredients = []
    in_ranges = True

    for line in lines:
        if line == "\n":
            in_ranges = False
        else:     
            line = line.replace('\n','')
            if in_ranges:
                min_range, max_range = line.split("-")
                min_range = int(min_range)
                max_range = int(max_range)
                ranges.append([min_range, max_range])
            else:
                ingredients.append(int(line))

    return ranges, ingredients

ranges, ingredients = read_puzzle_input(puzzle_input)
is_fresh = set()

for ingredient in ingredients:
    for r in ranges:
        min_range = r[0]
        max_range = r[1]
        if ingredient >= min_range and ingredient <= max_range:
            is_fresh.add(ingredient)
            break

print(f"How many of the available ingredient IDs are fresh? {len(is_fresh)}")
# 674