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
for line in lines:

    halfway = int(np.ceil(len(line)/2))
    c1 = line[:halfway]
    c2 = line[halfway:]

    common_list.extend(set(c1).intersection(set(c2)))

score = [dict_priority[x] for x in common_list]

print(f"What is the sum of the priorities? Answer: {sum(score)}")