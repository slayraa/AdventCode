
puzzle_input = "2024/inputs/05_input.txt"
#puzzle_input = "2024/inputs/05_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

rules = []
updates = []
for line in lines:
    if "|" in line:
        rules.append(line.replace("\n","").split("|"))
    elif len(line) > 1:
        updates.append(line.replace("\n","").split(","))

def is_valid_update(line, rules):
    for page in line:
        find_rules = [rule for rule in rules if (rule[1] == page) and (rule[0] in line)]

        for rule in find_rules:
            if line.index(rule[0]) > line.index(rule[1]):
                return False

    return True

# Check that the updates are in the correct order
middle_pages = []
for update in updates:
    if is_valid_update(update, rules):
        middle_pages.append(int(update[len(update) // 2]))

print(f"What do you get if you add up the middle page number from those correctly-ordered updates? {sum(middle_pages)}")
#5991