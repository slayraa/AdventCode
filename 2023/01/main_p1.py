import re

puzzle_input = "2023/inputs/01.txt"
#puzzle_input = "2023/inputs/01_sample.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

to_sum = []
for line in lines:
    numbers = re.findall(r'\d', line.replace("\n",""))
    to_sum.append(numbers[0] + numbers[-1])

sum_f = sum([int(num) for num in to_sum])

print(f"What is the sum of all of the calibration values? Answer: {sum_f}")
#56397