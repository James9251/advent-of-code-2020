# Opening the file containing the seating layout
with open('input.txt', 'r') as f:
    rows = f.read().splitlines()

def iterate_state(state):
    '''
    Returns a list the same length as the input, whose elements
    are the updated rows as strings according to the AoC Game of Life rules
    '''
    # All rows are assumed to be equal length, with at least 1 row
    width = len(state[0])
    length = len(state)
    new_state = []
    for i in range(length):
        row = state[i]
        new_row = ''
        for j in range(width):
            # i, j are the seat coordinates
            if row[j] == '.':
                new_row += '.'
                continue
            neighbours = ''
            down_bound = max(0, i - 1)
            up_bound = min(length, i + 2)
            left_bound = max(0, j - 1)
            right_bound = min(width, j + 2)
            for k in range(down_bound, up_bound):
                neighbours += state[k][left_bound: right_bound]
            # neighbour_count and current_occupant are input for the automaton rules
            neighbour_count = neighbours.count('#') # Includes the seat occupant
            current_occupant = row[j]
            # The rules of the cellular automaton
            if current_occupant == '#':
                if neighbour_count >= 4 + 1: # Avoids counting the occupant
                    new_row += 'L'
                else:
                    new_row += '#'
            elif current_occupant == 'L':
                if neighbour_count == 0:
                    new_row += '#'
                else:
                    new_row += 'L'
        new_state.append(new_row)
    return new_state

old_state = []
new_state = rows
# Iterate until nothing changes
# Assumes the initial state will reach a fixed point
while old_state != new_state:
    new_state, old_state = iterate_state(new_state), new_state
number_occupied_seats = sum(x.count('#') for x in new_state)
print("Total number of occupied seats = {}".format(number_occupied_seats))