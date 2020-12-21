# Opening the file containing the tree map
with open('input.txt', 'r') as f:
    rows = f.read().splitlines()

def count_trees(slope):
    '''
    Returns the numbers of trees encountered when taking the route
    down the mountain given by "right some number, down some number"
    slope = (right, down)
    '''
    right, down = slope
    row_length = len(rows[0]) # Assumes all rows are the same length
    index = 0
    tree_count = 0
    for i in range(0, len(rows), down):
        row = rows[i]
        if row[index] == '#':
            tree_count += 1
        index = (index + right) % row_length
    return tree_count

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_encountered = []
for slope in slopes:
    trees_encountered.append(count_trees(slope))

p = 1
for n in trees_encountered:
    p *= n

print("Trees encountered for each slope, multiplied = {}".format(p))