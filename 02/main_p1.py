# First column: A for Rock, B for Paper, and C for Scissors
# Second column: X for Rock, Y for Paper, and Z for Scissors
# Score: 1 for Rock, 2 for Paper, and 3 for Scissors plus the score for the outcome 
# of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

puzzle_input = "02/input.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

points_dic = {'R': 1, 'P': 2, 'S': 3}
conv_p1 = {'A': 'R', 'B': 'P', 'C': 'S'}
conv_p2 = {'X': 'R', 'Y': 'P', 'Z': 'S'}

def win(p1, p2):

    if p2 == 'R' and p1 == 'S':
        return True
    
    elif p2 == 'P' and p1 == 'R':
        return True
    
    elif p2 == 'S' and p1 == 'P':
        return True

    return False

def final_score(p1, p2):

    # draw
    if p1 == p2:
        return 3
    elif win(p1, p2):
        return 6
    else:
        return 0

score = 0
for line in lines:

    p1 = conv_p1[line[0]]
    p2 = conv_p2[line[2]]

    score = score + points_dic[p2] + final_score(p1, p2)

    #print(f"For the play {line} the player made {points_dic[p2] + final_score(p1, p2)}")

print(f"What is the total score? Answer: {score}")