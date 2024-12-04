import re

puzzle_input = "2024/inputs/03_input.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()

# Convert into a single string
s = "".join(lines)
#s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def calculate_mul(s):
    """Calculate the sum of all mul(X,Y) values in the string s"""
    
    res = 0

    # Find all mul(X,Y) values
    mul_values = re.findall(r'mul\((\d+),(\d+)\)', s)
    for val in mul_values:
        res = res + (int(val[0]) * int(val[1]))

    return res


enable = [match.span()[0] for match in re.finditer(r'do\(\)', s)]
disable = [match.span()[0] for match in re.finditer(r'don\'t\(\)', s)]
full_list = sorted(enable + disable)


last_e = 0
sum = 0
enabled = True

# Loop through enable and disable indexes
for i in full_list:

    if (i in enable) and (not enabled):
        enabled = True
        last_e = i
    
    elif (i in disable) and enabled:
        sum = sum + calculate_mul(s[last_e:i])
        enabled = False

# Check the last string if it ends enabled
if enabled:
    sum = sum + calculate_mul(s[last_e:len(s)])


print(f"What do you get if you add up all of the results of the multiplications? Answer: {sum}")
#107862689