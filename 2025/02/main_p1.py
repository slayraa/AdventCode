puzzle_input = "2025/inputs/02_input.txt"
#puzzle_input = "2025/inputs/02_sample.txt"

def read_puzzle_input(file):
    # Read puzzle input
    f = open(puzzle_input,"r")
    lines = f.readlines()
    f.close()

    lines = lines[0].split(',')
    
    return lines


ids = read_puzzle_input(puzzle_input)
invalid_ids = []

for id in ids:
    min_id, max_id = id.split('-')
    min_id = int(min_id)
    max_id = int(max_id)

    for i in range(min_id, max_id + 1):
        len_str_i = len(str(i))
        if (len_str_i % 2) == 0:
            str_i = str(i)
            if str_i[:int(len_str_i/2)] == str_i[int(len_str_i/2):]:
                invalid_ids.append(i)
                #print(f"Found invalid ID: {i}")

print(f"What do you get if you add up all of the invalid IDs? {sum(invalid_ids)}")
# sample: 1227775554
# answer: 13919717792