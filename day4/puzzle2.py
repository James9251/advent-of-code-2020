import re

# Opening the file containing passport information
with open('input.txt', 'r') as f:
    passport_file = f.read().splitlines()

# Parsing the passports file into a list of passports' fields
passports = []
new_passport = {}
for line in passport_file:
    if line == '':
        passports.append(new_passport)
        new_passport = {}
        continue
    # Using regexes and groups to do this, could also
    # split lines on ' ' and then fields/values on ':'
    field_names = re.findall(r'(...):', line)
    field_values = re.findall(r':([^ ]*)', line)
    new_passport.update(zip(field_names, field_values))
if new_passport != []:
    passports.append(new_passport)

def valid_passport(passport):
    '''
    Takes a dictionary as input whose keys are passport field names
    Returns True iff the required fields are present and the values are valid
    '''
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields_present = passport.keys()
    # Checks the required fields are present
    for field in required_fields:
        if not field in fields_present:
            return False
    # Check the 'byr' field
    if not re.match(r'[0-9]{4}', passport['byr']):
        print(passport)###
        return False
    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        return False
    # Check the 'iyr' field
    if not re.match(r'[0-9]{4}', passport['iyr']):
        return False
    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False
    # Check the 'eyr' field
    if not re.match(r'[0-9]{4}', passport['eyr']):
        return False
    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False
    # Check the 'hgt' field
    hgt_match = re.match(r'([0-9]*)([a-z]{2})', passport['hgt'])
    if not hgt_match:
        return False
    height = int(hgt_match.group(1))
    units = hgt_match.group(2)
    if units == 'cm':
        if height < 150 or height > 193:
            return False
    elif units == 'in':
        if height < 59 or height > 76:
            return False
    else:
        return False
    # Chech the 'hcl' field
    hcl_match = re.match(r'#[0-9a-f]{6}', passport['hcl'])
    if not hcl_match:
        return False
    # Check the 'ecl' field
    valid_ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not passport['ecl'] in valid_ecls:
        return False
    # Check the 'pid' field
    pid_match = bool(re.match(r'[0-9]{9}', passport['pid']))
    if not pid_match:
        return False
    return True
    
# Checking the list of passports and counting the number that are valid
number_valid_passports = 0
for passport in passports:
    if valid_passport(passport):
        number_valid_passports += 1

print("The number of valid passports is {}".format(number_valid_passports))