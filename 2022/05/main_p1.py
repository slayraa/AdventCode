"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3  
 """

cargo_sample = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
    ]

cargo = [
    ['Z', 'P', 'M', 'H', 'R'],
    ['P', 'C', 'J', 'B'],
    ['S', 'N', 'H', 'G', 'L', 'C', 'D'],
    ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'],
    ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
    ['T', 'F', 'S', 'Z', 'B', 'G'],
    ['N', 'R', 'V'],
    ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'],
    ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
]

puzzle_input = "05/input.txt"

f = open(puzzle_input,"r")
lines = f.readlines()

# Remove new lines
lines = [line.replace('\n','') for line in lines]

for line in lines:

    get_numbers = [int(x) for x in line.split(' ') if x.isnumeric()]
    numb_items = get_numbers[0]
    stack_from = get_numbers[1]
    stack_to = get_numbers[2]

    for i in range(numb_items):
        item = cargo[stack_from-1].pop()
        cargo[stack_to-1].append(item)

ans = ''
for i in range(len(cargo)):
    if len(cargo[i]) > 0:
        ans = ans + cargo[i][-1]

print(f"What crate ends up on top of each stack? Answer: {ans}")
