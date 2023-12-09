
puzzle_input = "2023/inputs/09.txt"
#puzzle_input = "2023/inputs/09_sample.txt"

# Read the input
with open(puzzle_input) as f:
    lines = f.read().splitlines()

# Convert each line to integer
oasis = []
for line in lines:
    oasis.append([int(num) for num in line.split(" ")])


estimates = []
final_estimates = []

for line in oasis:

    estimates = [line[-1]]
    # find the next line
    next_line = line.copy()
    while set(next_line) != {0}:
        new_line = []
        for i in range(1, len(next_line)):
            new_line.append(next_line[i] - next_line[i-1])

        # Keep the last element of next_line
        estimates.append(new_line[-1])
        next_line = new_line.copy()

    # estimate the missing final number from the initial line
    for i in range(len(estimates)-1, 0, -1):
        estimates[i-1] = estimates[i-1] + estimates[i]
    
    final_estimates.append(estimates[0])

sum_estimates = sum(final_estimates)
print(f"What is the sum of these extrapolated values? Answer: {sum_estimates}")

# Sample is 114
# 1725987467