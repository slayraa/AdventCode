import numpy as np

puzzle_input = "03/input.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

# Remove new lines
lines = [line.replace('\n','') for line in lines]

# Give priority to letters
dict_priority = {}
for x, y in ((x + 1, chr(ord('a') + x)) for x in range(26)):
    dict_priority[y] = x

for x in range(27, 53):
    l = chr(ord('A') + x - 27)
    dict_priority[l] = x

common_list = []
for c in range(0, len(lines), 3):

    c1 = lines[c]
    c2 = lines[c+1]
    c3 = lines[c+2]

    common_letter = (set(c1).intersection(set(c2))).intersection(set(c3))
    common_list.extend(common_letter)

score = [dict_priority[x] for x in common_list]

print(f"What is the sum of the priorities? Answer: {sum(score)}")