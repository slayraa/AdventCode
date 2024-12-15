puzzle_input = "1750884 193 866395 7 1158 31 35216 0"
#puzzle_input = "0 1 10 99 999"
#puzzle_input = "125 17"

# Separate input into a list
stones = puzzle_input.split(" ")

blink_times = 25
for b in range(blink_times):
    
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == "0":
            new_stones.append("1")
        
        elif len(stones[i]) % 2 == 0:
            new_stones.append(str(int(stones[i][:len(stones[i])//2])))
            new_stones.append(str(int(stones[i][len(stones[i])//2:])))
        
        else:
            new_stones.append(str(int(stones[i])*2024))
        
    #print(f"For blink {b+1}, stones are: {new_stones}")
    stones = new_stones

print(f"How many stones will you have after blinking 25 times? {len(stones)}")
#231278
