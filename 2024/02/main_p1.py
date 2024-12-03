import re

puzzle_input = "2024/inputs/02_input.txt"
#puzzle_input = "2024/inputs/02_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()

reports = []
for line in lines:
    numbers = re.findall(r'\d+', line.replace("\n",""))
    reports.append(numbers)

# Find safe reports
min_sep = 1
max_sep = 3
safe_reports = 0

for report in reports:

    safe = True
    first_diff = int(report[1]) - int(report[0])
    
    # all increasing
    if first_diff < 0:
        report = report[::-1]

    for i in range(len(report)-1):
        diff = int(report[i+1]) - int(report[i])
        # if report not safe, stop
        if diff < min_sep or diff > max_sep:
            safe = False
            break

    if safe:
        safe_reports = safe_reports + 1

print(f"How many reports are safe? Answer: {safe_reports}")
#257