# Opening the list of numbers and converting them to integers
with open('input.txt', 'r') as f:
    numbers = f.read().splitlines()
numbers = [int(x) for x in numbers]

# Looping over list contents to find m, n that sum to 2020
for n in numbers:
    m = 2020 - n
    if m in numbers:
        print("m = {}".format(m))
        print("n = {}".format(n))
        print("product = {}".format(m * n))
        break