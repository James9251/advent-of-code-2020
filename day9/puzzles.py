# Opening the file containing cipher information
with open('input.txt', 'r') as f:
    cipher = f.read().splitlines()
cipher = [int(x) for x in cipher]

preamble_length = 25
cipher_length = len(cipher)

def valid_sum(possible_numbers, target):
    '''
    Returns True iff a distinct pair of elements in possible_numbers
    add to produce target.
    '''
    for i in range(len(possible_numbers)):
        if target - possible_numbers[i] in possible_numbers[:i]:
            return True
        if target - possible_numbers[i] in possible_numbers[i+1:]:
            return True
    return False

first_invalid_number = 0
for i in range(preamble_length, cipher_length):
    if valid_sum(cipher[i - preamble_length: i], cipher[i]):
        continue
    first_invalid_number = cipher[i]
    break
print("First number without sum property is {}".format(first_invalid_number))

for i in range(len(cipher)):
    j = i + 2
    while sum(cipher[i: j]) < first_invalid_number and j < cipher_length:
        j += 1
    if sum(cipher[i: j]) == first_invalid_number:
        print("Solution found")
        smallest = min(cipher[i:j])
        largest = max(cipher[i:j])
        solution = smallest + largest
        print("Sum of first and last = {}".format(solution))