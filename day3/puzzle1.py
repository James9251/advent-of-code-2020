# Opening the file containing the tree map
with open('input.txt', 'r') as f:
    rows = f.read().splitlines()


row_length = len(rows[0]) # Assumes all rows are the same length
index = 0
tree_count = 0
for row in rows:
    if row[index] == '#':
        tree_count += 1
    index = (index + 3) % row_length

print("Number of trees encountered = {}".format(tree_count))