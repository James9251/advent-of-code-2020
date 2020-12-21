# Opening the list of rules and passwords into a list
with open('input.txt', 'r') as f:
    passwords = f.read().splitlines()

def valid_password(rule_and_password):
    '''
    Takes a string input and returns True iff the password is valid
    string must be of the form
    <pos 1>-<pos 1> <letter>: <password>
    <password> is valid when <letter> occurs in precisely one of
    either position <pos 1> or <pos 2>, indexed from 1
    Assumes password is sufficiently long so as not to raise
    index errors
    '''
    t = rule_and_password.split(' ')
    pos_1, pos_2 = [int(x) - 1 for x in t[0].split('-')]
    letter = t[1][0]
    password = t[2]
    in_pos_1 = password[pos_1] == letter
    in_pos_2 = password[pos_2] == letter
    return in_pos_1 != in_pos_2

count = 0
for password in passwords:
    if valid_password(password):
        count += 1
        
print("Number of valid passwords = {}".format(count))