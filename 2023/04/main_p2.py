
puzzle_input = "2023/inputs/04.txt"
#puzzle_input = "2023/inputs/04_sample.txt"

# Read the text file
dict_cards = {}
with open(puzzle_input, "r") as file:
    # initiate the dictionary
    lines = file.readlines()
    for i in range(len(lines)):
        dict_cards[i+1] = 1

with open(puzzle_input, "r") as file:
    ct = 1
    for line in file:
        line.replace('\n','')
        card = line.split(":")[1]
        winning_numbers = card.split("|")[0].strip().split(" ")
        scratch_numbers = card.split("|")[1].strip().split(" ")

        # Convert string to int
        winning_numbers = [int(num) for num in winning_numbers if num.isdigit()]
        scratch_numbers = [int(num) for num in scratch_numbers if num.isdigit()]
        
        # Calculate the power
        power = len(set(scratch_numbers).intersection(set(winning_numbers)))

        for i in range(1, power+1):
            dict_cards[ct+i] = dict_cards[ct+i] + (1*dict_cards[ct])

        ct = ct + 1

print(f"How many points are they worth in total? Answer: {sum(dict_cards.values())}")
# Sample is 30
# 8736438