
puzzle_input = "2023/inputs/04.txt"
#puzzle_input = "2023/inputs/04_sample.txt"

# Read the text file
dict_cards = {}
with open(puzzle_input, "r") as file:
    ct = 1
    for line in file:
        line.replace('\n','')
        card = line.split(":")[1]
        winning_numbers = card.split("|")[0].strip().split(" ")
        scratch_numbers = card.split("|")[1].strip().split(" ")

        # Remove " " from the list winning_numbers
        winning_numbers = [int(num) for num in winning_numbers if num.isdigit()]
        scratch_numbers = [int(num) for num in scratch_numbers if num.isdigit()]
        
        # Convert string to int
        power = len(set(scratch_numbers).intersection(set(winning_numbers)))
        dict_cards[ct] = (2 ** (power-1) if power > 0 else 0)
        ct = ct + 1

print(f"How many points are they worth in total? Answer: {sum(dict_cards.values())}")
# Sample is 13
# 24542