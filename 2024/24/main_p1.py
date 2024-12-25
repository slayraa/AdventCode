
puzzle_input = "2024/inputs/24_input.txt"
#puzzle_input = "2024/inputs/24_sample.txt"

# Read puzzle input
f = open(puzzle_input,"r")
lines = f.readlines()
f.close()

wires = {}
gates = {} # gates wire: [wire1, operation, wire2], operation in AND, OR, XOR 
for line in lines:
    if ":" in line:
        wire = line.split(":")[0]
        wires[wire] = line.split(":")[1].strip()
    elif "->" in line:
        wire = line.split("->")[1].strip()
        gates[wire] = line.split("->")[0].split(" ")[:-1]

gates_to_calculate = list(gates.keys())
while gates_to_calculate:
    for wire in gates_to_calculate:

        # Check if the needed wires have been calculated yet
        if sum([x in wires.keys() for x in gates[wire]])==2:
            if "AND" in gates[wire]:
                wires[wire] = int(wires[gates[wire][0]]) & int(wires[gates[wire][2]])
            elif "OR" in gates[wire]:
                wires[wire] = int(wires[gates[wire][0]]) | int(wires[gates[wire][2]])
            elif "XOR" in gates[wire]:
                wires[wire] = int(wires[gates[wire][0]]) ^ int(wires[gates[wire][2]])
            
            gates_to_calculate.remove(wire)

starts_with = "z"
wires_l = [wire for wire in wires.keys() if wire.startswith(starts_with)]
wires_l.sort(reverse=True)
output = "".join([str(wires[wire]) for wire in wires_l])

print(f"What decimal number does it output on the wires starting with z? {int(output,2)}")
# 36902370467952