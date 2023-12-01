import re

puzzle_input = "2023/inputs/01.txt"
#puzzle_input = "2023/inputs/01_p2_sample.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

numbers_list = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
numbers_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

to_sum = []
for line in lines:
    numbers = re.findall(numbers_list, line.replace("\n",""))
    numbers = [numbers_map[num] if num in numbers_map else num for num in numbers]
    to_sum.append(numbers[0] + numbers[-1])

sum_f = sum([int(num) for num in to_sum])

print(f"What is the sum of all of the calibration values? Answer: {sum_f}")
#55725