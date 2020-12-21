# Opening the list of numbers and converting them to integers
with open('input.txt', 'r') as f:
    numbers = f.read().splitlines()
numbers = [int(x) for x in numbers]

# This will find all triples in the list that add to 2020
# Triples will appear only once with no reordering
length = len(numbers)
for i in range(length - 2):
    a = numbers[i]
    for j in range(i + 1, length - 1):
        b = numbers[j]
        for k in range(j + 2, length):
            c = numbers[k]
            if a + b + c == 2020:
                print("a = {}".format(a))
                print("b = {}".format(b))
                print("c = {}".format(c))
                print("product = {}".format(a * b * c))