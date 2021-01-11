import re

# TODO - needs a whole load of tidying

# Open the bitmask and memory instructions
with open('input.txt', 'r') as f:
    instructions = f.read().splitlines()

def decode_mask_instruction(mask_instruction):
    '''
    Returns a tuple (x, y) representation of the mask instruction
    x is the integer with 1's in the 1's places of the mask, 0's elsewhere
    y is the integer with 0's in the 0's places of the mask, 1's elsewhere
    To apply the mask to a number n: n_masked = (n | x) & y
    '''
    mask = mask_instruction[-36:]
    x = int(''.join('1' if x == '1' else '0' for x in mask), 2)
    y = int(''.join('0' if x == '0' else '1' for x in mask), 2)
    return (x, y)

def decode_memory_instruction(mem_instruction):
    '''
    Returns a tuple (add, var) of address and variable integers
    '''
    match = re.search(r'\[([0-9]*)\]', mem_instruction)
    add = int(match.groups()[0])
    match = re.search(r' ([0-9]*)$', mem_instruction)
    var = int(match.groups()[0])
    return (add, var)

# Use a dictionary to simulate the memory since we don't need 2^36 addresses
mem = {}
# Run through the instructions
for inst in instructions:
    if inst[:4] == 'mask':
        x, y = decode_mask_instruction(inst)
        continue
    add, var = decode_memory_instruction(inst)
    var = (var | x) & y
    mem[add] = var
# Sum the values at all memory addresses for solution
solution = sum(mem[x] for x in mem.keys())
print("Puzzle 1 solution = {}".format(solution))

def apply_mask_to_address(add, mask_instruction):
    '''
    Takes the memory address add and one full mask_instruction as input
    Iterates through all possible addresses where 0/1 replace 'X' in the mask
    1 in a mask position add to 1 in that position
    Uses the yield keyword so addresses can be looped through like an iterable
    '''
    mask = mask_instruction[-36:]
    limit = 1 << mask.count('X')
    a = int(''.join('0' if x == 'X' else '1' for x in mask), 2) # 1 everywhere but the X's
    b = add | int(''.join('1' if x == 'X' else x for x in mask), 2) # Replace X's with 1's, OR with input address
    c = a
    for i in range(limit):
        yield c & b
        c = (c + 1) | a

# Use a dictionary to simulate the memory since we don't need 2^36 addresses
mem = {}
# Run through the instructions
for inst in instructions:
    if inst[:4] == 'mask':
        mask = inst
        continue
    add, var = decode_memory_instruction(inst)
    for new_add in apply_mask_to_address(add, mask): # Treated as an iterable
        mem[new_add] = var
# Sum the values at all memory addresses for solution
solution = sum(mem[x] for x in mem.keys())
print("Puzzle 2 solution = {}".format(solution))