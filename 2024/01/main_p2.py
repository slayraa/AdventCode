import re

puzzle_input = "2023/inputs/01.txt"
#puzzle_input = "2023/inputs/01_p2_sample.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

numbers_list = r'(\d|zero|one|two|three|four|five|six|seven|eight|nine)'
numbers_list_reversed = r'(\d|orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)'
numbers_map = {
    'zero': '0',
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
    first_number = re.findall(numbers_list, line)[0]
    reversed_line = line[::-1]
    last_number = re.findall(numbers_list_reversed, reversed_line)[0][::-1]
    numbers = [first_number, last_number]
    numbers_mapped = [numbers_map.get(num) if num in numbers_map.keys() else num for num in numbers]
    #print(f"line: {line} numbers: {numbers} to_sum: {numbers_mapped[0] + numbers_mapped[-1]}")
    to_sum.append(numbers_mapped[0] + numbers_mapped[1])

sum_f = sum([int(num) for num in to_sum])

print(f"What is the sum of all of the calibration values? Answer: {sum_f}")
#55701