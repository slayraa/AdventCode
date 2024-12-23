
from collections import defaultdict

puzzle_input = "2024/inputs/22_input.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

secret_numbers = [int(line.replace("\n","")) for line in lines]

def mix_number(secret_number, current_number):
    return (current_number^int(secret_number))

def prune_number(current_number, constant=16777216):
    return (current_number % constant)

def calculate_new_secret_number(secret_number, iterations):

    digits = []
    
    for i in range(iterations):
        # Multiply the secret number by 64, then mix and prune
        secret_number = mix_number(secret_number=secret_number, current_number=(secret_number*64))
        secret_number = prune_number(current_number=secret_number)

        # Divide the secret number by 32, round the result down to the nearest integer, then mix and prune
        secret_number = mix_number(secret_number=secret_number, current_number=(secret_number // 32))
        secret_number = prune_number(current_number=secret_number)

        # Multiply the secret number by 2048, then mix and prune
        secret_number = mix_number(secret_number=secret_number, current_number=(secret_number * 2048))
        secret_number = prune_number(current_number=secret_number)

        digits.append(int(str(secret_number)[-1]))

    return digits


#secret_numbers = [1, 2, 3, 2024]
iterations = 2000
secret_numbers_price = dict()
#secret_numbers_diff = dict()
for sn in secret_numbers:
    res = calculate_new_secret_number(secret_number=sn, iterations=iterations)
    secret_numbers_price[sn] = res
    res.insert(0, int(str(sn)[-1]))
    #secret_numbers_diff[sn] = [res[i+1] - res[i] for i in range(len(res) - 2)]

secret_numbers_diff = [[b - a for a, b in zip(p, p[1:])] for p in secret_numbers_price.values()]

amount_seq = defaultdict(int)
for sn_idx, change in enumerate(secret_numbers_diff):
    keys = set()
    for i in range(len(change)-3):
        key = tuple(change[i:(i+4)])
        if key in keys:
            continue
        amount_seq[key] = amount_seq[key] + secret_numbers_price[secret_numbers[sn_idx]][i+4]
        keys.add(key)

max_amount = max(amount_seq.values())
print(f"What is the most bananas you can get? {max_amount}")
# 1614
