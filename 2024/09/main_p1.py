puzzle_input = "2024/inputs/09_input.txt"
#puzzle_input = "2024/inputs/09_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

s = lines[0]
#s = '1234'
s_ = [0]*int(s[0])

# Find the string of files
for i in range(1, len(s)):
    # if i is even then it's a space, otherwise it's a file
    if i % 2 == 0:
        s_ = s_ + [i//2]*int(s[i])

# Fill the spaces
s_final = [0]*int(s[0])
s_ = s_[len(s_final):]

for i in range(1, len(s)):
    
    empty_spaces = int(s[i])
    s_ = s_[::-1]

    if i % 2 == 0:
        s_final.extend(s_[:empty_spaces])
        s_ = s_[empty_spaces:]
    else:
        if empty_spaces > 0:
            s_final.extend(s_[:empty_spaces])
            s_ = s_[empty_spaces:]

# Multiply each character by its index and sum the string
checksum = 0
for i in range(len(s_final)):
    checksum = checksum + i*int(s_final[i])
    #print(f"{i} * {s_final[i]} = {i*int(s_final[i])}")

print(f"What is the resulting filesystem checksum? {checksum}")
#6367087064415
