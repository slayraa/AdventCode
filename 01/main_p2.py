puzzle_input = "01/input.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

sum = []
sum_temp = 0

for line in lines:

    if line == "\n":
        sum.append(sum_temp)
        sum_temp = 0
    else:
        sum_temp = sum_temp + int(line.replace("\n",""))

sum.append(sum_temp)
sum.sort()
top_3 = sum[-3] + sum[-2] + sum[-1]

print(f"How many Calories are those Elves carrying in total? Answer: {top_3}")