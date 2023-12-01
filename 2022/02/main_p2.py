# First column: A for Rock, B for Paper, and C for Scissors
# Second column: X for lose, Y for a draw, and Z means you need to win
# Score: 1 for Rock, 2 for Paper, and 3 for Scissors plus the score for the outcome 
# of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

puzzle_input = "02/input.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

points_dic = {'R': 1, 'P': 2, 'S': 3}
conv_p1 = {'A': 'R', 'B': 'P', 'C': 'S'}

def choose_play(p1, p2):

    if p2 == 'Y':
        return p1

    if p1 == 'S':
        if p2 == 'X':
            return 'P'
        else:
            return 'R'
    
    elif p1 == 'R':
        if p2 == 'X':
            return 'S'
        else:
            return 'P'
    
    elif p1 == 'P':
        if p2 == 'X':
            return 'R'
        else:
            return 'S'

    return False

def final_score(p2):

    # draw
    if p2 == 'Y':
        return 3
    #win
    elif p2 == 'Z':
        return 6
    #loss
    else:
        return 0

score = 0
for line in lines:

    p1 = conv_p1[line[0]]
    p2 = choose_play(p1, line[2])

    score = score + points_dic[p2] + final_score(line[2])

    #print(f"For the play {line} the player made {points_dic[p2] + final_score(line[2])}")

print(f"What is the total score? Answer: {score}")