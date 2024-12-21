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
        return True

    isvalid = False
    valid_towels = [towel for towel in towels if (towel in pat) and (towel == pat[:len(towel)])]
    for tw in valid_towels:
        isvalid_temp = is_valid(pat[len(tw):], towels, found)
        isvalid = (isvalid or isvalid_temp)
    
    found[pat] = isvalid
    #print(found)

    return isvalid


designs = 0
found = {}
for pat in patterns:
    if patterns.index(pat) % 10 == 0:
        print(f"Checking design: {patterns.index(pat)} out of {len(patterns)-1} ({round(patterns.index(pat)/(len(patterns)-1)*100,2)}%)")
    if is_valid(pat, towels, found):
        #print(f"Found design: {pat}")
        designs = designs + 1

print(f"How many designs are possible? {designs}")
#330