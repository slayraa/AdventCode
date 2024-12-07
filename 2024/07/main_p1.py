import re
import numpy as np
from itertools import product

puzzle_input = "2024/inputs/07_input.txt"
#puzzle_input = "2024/inputs/07_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

result = []
factors = []
for line in lines:
    # Convert lines into result and factors
    numbers = re.findall(r'\d+', line)
    result.append(int(numbers[0]))
    factors.append([int(number) for number in numbers[1:]])

def is_calibrated(res, fac):
    # A result is calibrated if it can be the sum or the product of the factors
    if res == np.sum(fac):
        #print(f"sum: {sum} == res: {res} for '+'")
        return True
    
    elif res == np.prod(fac):
        #print(f"sum: {sum} == res: {res} for '*'")
        return True
    
    else:
        symbols = ['+', '*']
        length = len(fac) - 1
        arrang = list(product(symbols, repeat=length))
        arrang = [v for v in arrang if len(np.unique(v)) > 1]

        for arr in arrang:
            # Reset the original values
            sum = fac[0]
            i = 1

            for oper in arr:
                if oper == '+':
                    sum = sum + fac[i]
                else:
                    sum = sum * fac[i]
                i = i + 1
            
            if sum == res:
                #print(f"sum: {sum} == res: {res} for operations {arr}")
                return True
    
    return False

calibrated = 0
for res, fac in zip(result, factors):
    #print(res, fac)
    
    if is_calibrated(res, fac):
        calibrated = calibrated + res

print(f"What is their total calibration result? {calibrated}")
#12940396350192