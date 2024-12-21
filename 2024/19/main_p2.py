# Description: Day 19: Towel Day
puzzle_input = "2024/inputs/19_input.txt"
#puzzle_input = "2024/inputs/19_sample.txt"

# Read puzzle input
def read_input(file):
    f = open(file,"r")
    lines = f.readlines()
    f.close()
    return lines

def breakdown_lines(lines):
    towels = lines[0].replace("\n","").split(",")
    towels = [towel.strip() for towel in towels]

    patterns = []
    for line in lines[2:]:
        # Convert each line into a list of characters
        patterns.append(line.replace("\n",""))
    
    return towels, patterns
    

lines = read_input(puzzle_input)
towels, patterns = breakdown_lines(lines)


def is_valid(pat, towels, found):

    if pat in found:
        return found[pat]

    if len(pat) == 0:
        return 1

    isvalid_ctr = 0
    valid_towels = [towel for towel in towels if (towel in pat) and (towel == pat[:len(towel)])]
    
    for tw in valid_towels:
        isvalid_temp = is_valid(pat[len(tw):], towels, found)
        isvalid_ctr = isvalid_ctr + isvalid_temp
    
    found[pat] = isvalid_ctr
    #print(found)

    return isvalid_ctr


found = {}
count_designs = 0

for pat in patterns:
    if patterns.index(pat) % 10 == 0:
        print(f"Checking design: {patterns.index(pat)} out of {len(patterns)-1} ({round(patterns.index(pat)/(len(patterns)-1)*100,2)}%)")
    count_designs = count_designs + is_valid(pat, towels, found)
    #print(f"Found design: {pat}")

print(f"What do you get if you add up the number of different ways you could make each design? {count_designs}")
#950763269786650