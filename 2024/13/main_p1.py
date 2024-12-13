import re
import sympy as sp

puzzle_input = "2024/inputs/13_input.txt"
#puzzle_input = "2024/inputs/13_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

# Parse lines into X, Y and prize
X = []
Y = []
prizes = []
new_prize = False
xx = []
yy = []

for line in lines:
    if "Button A" in line:
        button_a = re.findall(r'\d+', line)
        xx.append(int(button_a[0]))
        yy.append(int(button_a[1]))
        new_prize = False
    
    elif "Button B" in line:
        button_b = re.findall(r'\d+', line)
        xx.append(int(button_b[0]))
        yy.append(int(button_b[1]))
    
    elif "Prize" in line:
        prize = re.findall(r'\d+', line)
        prizes.append([int(prize[0]), int(prize[1])])
        new_prize = True
    
    if new_prize:
        X.append(xx)
        Y.append(yy)
        xx = []
        yy = []
        new_prize = False

tokens = 0
a, b = sp.symbols('a b')

# For each prize, check if the equation is solvable
for i in range(len(prizes)):
    
    # Check if the equation is solvable
    eq1 = sp.Eq(X[i][0]*a + X[i][1]*b, prizes[i][0])
    eq2 = sp.Eq(Y[i][0]*a + Y[i][1]*b, prizes[i][1])

    # Solve the system of equations
    solution = sp.solve((eq1, eq2), (a, b))
    
    # Check if the solution is integer and less than 100
    if (solution[a].is_integer and solution[b].is_integer) and (solution[a]<100 and solution[b]<100):
        tokens = tokens + (solution[a]*3 + solution[b])

print(f"What is the fewest tokens you would have to spend to win all possible prizes? {tokens}")
#29201