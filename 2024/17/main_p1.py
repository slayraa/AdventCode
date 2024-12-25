import re

puzzle_input = "2024/inputs/17_input.txt"
#puzzle_input = "2024/inputs/17_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

computer = {}
computer["A"] = int(re.findall(r"\d+", lines[0])[0])
computer["B"] = int(re.findall(r"\d+", lines[1])[0])
computer["C"] = int(re.findall(r"\d+", lines[2])[0])
computer["prog"] = [int(i) for i in lines[4].split(":")[1].split(",")]

def combo_operand(opr, computer):
    if opr in range(4):
        return opr
    elif opr == 4:
        return computer["A"]
    elif opr == 5:
        return computer["B"]
    elif opr == 6:
        return computer["C"]
    return -1

def instructions(opcode, opr, computer):

    new_pointer = None
    output = []

    if opcode == 0: #adv
        cb = combo_operand(opr, computer)
        res = computer["A"]/(2**cb)
        res, _ = divmod(res, 1)
        computer["A"] = int(res)
    
    elif opcode == 1: #bxl
        computer["B"] = computer["B"] ^ opr
    
    elif opcode == 2: #bst
        computer["B"] = combo_operand(opr, computer) % 8
    
    elif opcode == 3: #jnz
        if computer["A"] != 0:
            new_pointer = opr
    
    elif opcode == 4: #bxc
        computer["B"] = computer["B"] ^ computer["C"]
    
    elif opcode == 5: #out
        output.append(combo_operand(opr, computer) % 8)
 
    elif opcode == 6: #bdv
        cb = combo_operand(opr, computer)
        res = computer["A"]/(2**cb)
        res, _ = divmod(res, 1)
        computer["B"] = int(res)

    elif opcode == 7: #cdv
        cb = combo_operand(opr, computer)
        res = computer["A"]/(2**cb)
        res, _ = divmod(res, 1)
        computer["C"] = int(res)

    return new_pointer, output


pt = 0
output = []
while pt < len(computer["prog"]):

    new_pointer, res = instructions(opcode=computer["prog"][pt], 
                                    opr=computer["prog"][pt+1],
                                    computer=computer)

    output.extend(res)

    if new_pointer is None:
        pt = pt + 2
    else:
        pt = new_pointer

output_str = ",".join(str(item) for item in output) 
print(f"What do you get if you use commas to join the values it output into a single string? {output_str}")
#1,3,5,1,7,2,5,1,6