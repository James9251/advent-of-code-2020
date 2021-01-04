# Opening the file containing instruction information
with open('input.txt', 'r') as f:
    boot_code = f.read().splitlines()

def decode(instruction):
    '''
    Takes a line from the boot code and interprets it as opcode followed
    by an integer argument
    returns a tuple of the opcode and the integer
    '''
    opcode = instruction[:3]
    argument = int(instruction[4:])
    return (opcode, argument)

def execute(opcode, argument, acc, instruction_pointer):
    '''
    Executes the opcode with the given argument
    Takes current value of acc and instruction_pointer
    Returns a tuple containing the new values of acc and instruction_pointer
    Returns None when execution isn't successful
    '''
    if opcode == 'acc':
        acc += argument
        instruction_pointer += 1
    elif opcode == 'jmp':
        instruction_pointer += argument
    elif opcode == 'nop':
        instruction_pointer += 1
    else:
        # Invalid opcode
        return None
    # successful execution
    return (acc, instruction_pointer)

def execute_code(code):
    '''
    Takes boot code in the form of an array and attempts to execute it.
    If an infinite loop is reached, this returns a tuple containing the
    values of acc and instruction_pointer just before the line that would
    be first to execute twice.
    If the program runs successfully it returns a tuple containing the 
    current acc value and instruction pointer which will point to the last
    array element +1 (for the next instruction)
    If the program's instruction pointer is out of bounds if will return
    a tuple of acc and instruction_pointer values at that point
    '''
    # The lines of the boot code that have been reached
    reached_lines = set()
    # The upper limit of what the instruction pointer can be
    upper_limit = len(boot_code)
    # The initial value of the accumulator and instruction pointer
    acc = 0
    instruction_pointer = 0

    while True:
        # Check the instruction pointer is within limits
        if instruction_pointer < 0 or instruction_pointer >= upper_limit:
            break
        # Just before we run the command we check for duplication
        if instruction_pointer in reached_lines:
            break
        reached_lines.add(instruction_pointer)
        # Fetch the next instruction
        instruction = boot_code[instruction_pointer]
        # Decode and execute
        opcode, argument = decode(instruction)
        # This raises an error when execute returns None
        acc, instruction_pointer = execute(opcode, argument, acc, instruction_pointer)
    return (acc, instruction_pointer)

# Puzzle 1
acc, instruction_pointer = execute_code(boot_code)
print("Instruction {} was executed twice".format(instruction_pointer))
print("Current accumulator value = {}\n".format(acc))

# Puzzle 2
target = len(boot_code)
for i in range(len(boot_code)):
    command = boot_code[i]
    op = command[:3]
    if op == 'acc':
        continue
    # Trialling replacing each jmp or nop operation
    new_command = 'jmp' + command[3:]
    if op == 'jmp':
        new_command = 'nop' + command[3:]
    boot_code[i] = new_command
    acc, ip = execute_code(boot_code)
    if ip == target:
        print("Error on line {}".format(i))
        print("Opcode = {}".format(command))
        print("Accumulator value = {}".format(acc))
    boot_code[i] = command










