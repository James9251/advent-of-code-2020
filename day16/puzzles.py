import re

# Open the file containing ticket information
with open('input.txt', 'r') as f:
    ticket_information = f.read().splitlines()

# Extract the relevant information into a useful format
fields = {}
for i in range(19):
    field_info = ticket_information[i]
    field_name = field_info.split(':')[0]
    field_ranges = re.findall('([0-9]*)-([0-9]*)', field_info)
    fields.update({field_name: [(int(a), int(b)) for a, b in field_ranges]})    
your_ticket = [int(x) for x in ticket_information[22].split(',')]
tickets = [[int(x) for x in ticket_information[i].split(',')] for i in range(25, 270)]

# Create a set of viable ticket field numbers
valid_numbers = set()
for k in fields.keys():
    for x in fields[k]:
        a, b = x
        for i in range(a, b + 1):
            valid_numbers.add(i)

# Calculate the solution to puzzle 1
ticket_scanning_error_rate = 0
for ticket in tickets:
    for n in ticket:
        if n in valid_numbers:
            continue
        ticket_scanning_error_rate += n
print("Solution to puzzle 1: {}".format(ticket_scanning_error_rate))