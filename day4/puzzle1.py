import re

# Opening the file containing passport information
with open('input.txt', 'r') as f:
    passport_file = f.read().splitlines()

# Parsing the passports file into a list of passports' fields
passports = []
new_passport = []
for line in passport_file:
    if line == '':
        passports.append(new_passport)
        new_passport = []
        continue
    new_passport += re.findall(r'(...):', line)
if new_passport != []:
    passports.append(new_passport)

def valid_passport(passport_fields):
    '''
    Return True iff a passport is valid
    a passport if valid when it has all 7 fields
    '''
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in fields:
        if not field in passport_fields:
            return False
    return True

number_of_valid_passports = 0
for passport in passports:
    if valid_passport(passport):
        number_of_valid_passports += 1

print("Number of valid passports = {}".format(number_of_valid_passports))