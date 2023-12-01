import numpy as np

#puzzle_input = "08/sample.txt"
puzzle_input = "08/input.txt"

data = np.genfromtxt(puzzle_input, dtype=str)

# Build forest
forest = []
for row in data:
    forest.append([int(i) for i in row])

forest = np.array(forest)


def scenic_score(t, arr):
    ct = 0
    for i in arr:
        if i < t:
            ct = ct + 1
        elif i >= t:
            return ct + 1

    return ct


# scenic score
high_score = 0
for i in range(1, len(forest)-1):
    for j in range(1, len(forest[0])-1):
        tree = forest[i, j]
        
        # left
        scl = scenic_score(tree, np.flip(forest[i, 0:j]))
        
        if scl > 0:
            #right
            scr = scenic_score(tree, forest[i, j+1:len(forest[0])])

            if scr > 0:
                #up
                scu = scenic_score(tree, np.flip(forest[0:i, j]))

                if scu > 0:
                    scd = scenic_score(tree, forest[i+1:len(forest), j])

                    if scd > 0:
                        curr_score = scl*scr*scu*scd

                        if curr_score > high_score:
                            high_score = curr_score

print(f"What is the highest scenic score possible for any tree? Answer: {high_score}")
# 263670
