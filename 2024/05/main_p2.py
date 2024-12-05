
from collections import Counter

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
    if not is_valid_update(update, rules):

        all_start_page = []
        for page in update:
            find_rules = [rule[0] for rule in rules if (rule[0] == page) and (rule[1] in update)]
            all_start_page.extend(find_rules)

        ordered_pages = Counter(all_start_page).most_common((len(update) // 2) + 1)
        middle_page = int(ordered_pages[-1][0])
        middle_pages.append(middle_page)
        #print(f"Found middle page {middle_page} in update {update}")
    
print(f"What do you get if you add up the middle page number from those correctly-ordered updates? {sum(middle_pages)}")
#5479 is too high