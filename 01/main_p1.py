puzzle_input = "01/input.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

sum = 0
sum_temp = 0

for line in lines:

    if line == "\n":
        if sum < sum_temp:
            sum = sum_temp
        sum_temp = 0
    else:
        sum_temp = sum_temp + int(line.replace("\n",""))

print(f"How many total Calories is that Elf carrying? Answer: {sum}")