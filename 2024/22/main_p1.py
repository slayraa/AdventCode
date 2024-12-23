
puzzle_input = "2024/inputs/22_input.txt"
#puzzle_input = "2024/inputs/22_sample.txt"

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

    return secret_number


iterations = 2000
secret_numbers_dic = dict()
for sn in secret_numbers:
    res = calculate_new_secret_number(secret_number=sn, iterations=iterations)
    secret_numbers_dic[sn] = res

print(f"What is the sum of the 2000th secret number generated by each buyer? {sum(secret_numbers_dic.values())}")
# 14726157693