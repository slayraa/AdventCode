puzzle_input = "04/input.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

# Remove new lines
lines = [line.replace('\n','') for line in lines]

counter = 0
for line in lines:

    break_line = line.replace('-',',').split(',')
    break_line = [int(x) for x in break_line]

    p1 = {x for x in range(break_line[0], break_line[1]+1)}
    p2 = {x for x in range(break_line[2], break_line[3]+1)}

    if p1.intersection(p2) != set():
        #print(f"Subsets: {p1} and {p2}")
        counter = counter + 1

print(f"In how many assignment pairs do the ranges overlap? Answer: {counter}")