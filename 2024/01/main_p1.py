import re

puzzle_input = "2024/inputs/01_input.txt"
#puzzle_input = "2024/inputs/01_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()

left_list = []
right_list = []
for line in lines:
    numbers = re.findall(r'\d+', line.replace("\n",""))
    left_list.append(numbers[0])
    right_list.append(numbers[1])

# Find the difference between the smallest value of the lists
sum = 0
while len(left_list)>0:
    min_left = min(left_list)
    min_right = min(right_list)
    sum = sum + abs(int(min_left)-int(min_right))

    left_list.remove(min_left)
    right_list.remove(min_right)

print(f"What is the total distance between your lists? Answer: {sum}")
#2430334