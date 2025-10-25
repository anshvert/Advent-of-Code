from collections import defaultdict

with open('input.txt', 'r') as f:
    instructions = f.read().splitlines()
    f.close()

vals = defaultdict(int)
vals['c'] = 1
ind = 0

while ind < len(instructions):
    instruction = instructions[ind]
    split_instruction = instruction.split()
    if split_instruction[0] == "inc":
        vals[split_instruction[1]] += 1
        ind += 1
    elif split_instruction[0] == "dec":
        vals[split_instruction[1]] -= 1
        ind += 1
    elif split_instruction[0] == "cpy":
        if split_instruction[1] in vals:
            vals[split_instruction[2]] = vals[split_instruction[1]]
        else:
            vals[split_instruction[2]] = int(split_instruction[1])
        ind += 1
    else:
        if (split_instruction[1].isnumeric() and int(split_instruction[1]) != 0) or vals[split_instruction[1]] != 0:
            ind += int(split_instruction[2])
        else:
            ind += 1

print("final value of a register", vals['a'])

