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
        str_i = str(i)
        len_str_i = len(str_i)

        if (len(set(str_i)) == 1) and (len_str_i > 1):
            invalid_ids.append(i)
            #print(f"1. Found invalid ID: {i}")
        else:
            for j in range(2, int(len_str_i/2)+1):
                size_str = int(len_str_i/j)
                if len_str_i % size_str == 0:
                    is_invalid = True
                    for k in range(int(len_str_i/size_str)-1):
                        if str_i[k*size_str:k*size_str+size_str] != str_i[k*size_str+size_str:k*size_str+2*size_str]:
                            is_invalid = False
                            break
                    if is_invalid and (len_str_i > 3):
                        invalid_ids.append(i)
                        #print(f"2. Found invalid ID: {i}")
                        break

print(f"What do you get if you add up all of the invalid IDs? {sum(invalid_ids)}")
# sample: 4174379265
# answer: 14582313461