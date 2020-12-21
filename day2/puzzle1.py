# Opening the list of rules and passwords into a list
with open('input.txt', 'r') as f:
    passwords = f.read().splitlines()

def valid_password(rule_and_password):
    '''
    Takes a string input and returns True iff the password is valid
    string must be of the form
    <min>-<max> <letter>: <password>
    Passwords are valid when then contain between <min> and <max> 
    occurrences of <letter>
    '''
    t = rule_and_password.split(' ')
    minimum, maximum = [int(x) for x in t[0].split('-')]
    letter = t[1][0]
    password = t[2]
    frequency = password.count(letter)
    if frequency < minimum or frequency > maximum:
        return False
    return True

count = 0
for password in passwords:
    if valid_password(password):
        count += 1
        
print("Number of valid passwords = {}".format(count))