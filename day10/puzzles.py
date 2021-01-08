# Opening the file containing joltage information
with open('input.txt', 'r') as f:
    joltages = f.read().splitlines()
joltages = [int(x) for x in joltages]
joltages.sort()
# This accounts for the socket and output joltage
joltages = [0] + joltages + [joltages[-1] + 3]

differences_of_1 = 0
differences_of_3 = 0

for i, j in zip(joltages[:-1], joltages[1:]):
    diff = abs(i - j)
    if diff == 1:
        differences_of_1 += 1
    if diff == 3:
        differences_of_3 += 1

product = differences_of_1 * differences_of_3
print("Product of 1 and 3 jolt frequencies is {}".format(product))

# The dictionary "combinations" holds the number of combinations
# possible for each joltage i where the final joltage in the chain is i.
# It's wasteful to keep all but 4 entries, but there's no need to get
# rid of them for a small dataset.
maximum_joltage = joltages[-1]
combinations = dict(zip(joltages, [0] * len(joltages)))
combinations[0] = 1 # Base step in the induction, 1 way to connect 0 adapters
for i in range(maximum_joltage + 1):
    if i in combinations.keys():
        for j in range(1, 4):
            if i - j in combinations.keys():
                combinations[i] += combinations[i - j]
    else:
        continue
print("Number of combinations = {}".format(combinations[maximum_joltage]))