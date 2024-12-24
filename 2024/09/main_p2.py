puzzle_input = "2024/inputs/09_input.txt"
#puzzle_input = "2024/inputs/09_sample.txt"

f = open(puzzle_input,"r")
lines = f.readlines()
f.close()
s = list(lines[0])

def ind_find_space(f, spaces):
   for i in range(len(spaces)):
       if f <= int(spaces[i]):
           return i
   return -1


empty_slots = {i//2: [int(s[i]), []] for i in range(1, len(s), 2)}
empty_slots[len(s)//2] = [0, []]
ids_rep = {(i//2): int(s[i]) for i in range(0, len(s), 2)}

for pos in range(len(s)-1, 0, -2): # cycle through files in s in reverse
    rep = int(s[pos])
    f_id = (pos // 2)
    spaces = [v[0] for _, v in empty_slots.items()]
    idx_space = ind_find_space(rep, spaces[:f_id])

    # Move file to the new index position, and update the spaces
    if idx_space != -1:
        # update spaces
        empty_slots[idx_space][0] = empty_slots[idx_space][0] - rep
        empty_slots[f_id][0] = empty_slots[f_id][0] + rep
        empty_slots[idx_space][1].extend([f_id]*rep)


# Build the final string
moved_files = []
for sublist in [v[1] for _, v in empty_slots.items()]:
    for item in sublist:
        if item not in moved_files:
            moved_files.append(item)

s_final = []
for i in range(0, len(s)//2+1):

    # Add files
    if i not in moved_files:
        s_final.extend([i]*ids_rep[i])
    else:
        s_final.extend([0]*ids_rep[i])
        empty_slots[i][0] = empty_slots[i][0] - ids_rep[i]

    # Add spaces
    s_final.extend(empty_slots[i][1])
    if empty_slots[i][0] > 0:
        s_final.extend([0]*empty_slots[i][0])


# Calculate the checksum
checksum = 0
for i in range(len(s_final)):
    if s_final[i] != "0":
        checksum = checksum + i*int(s_final[i])
        #print(f"{i} * {s_final[i]} = {i*int(s_final[i])}")

print(f"What is the resulting filesystem checksum? {checksum}")
#6390781891880