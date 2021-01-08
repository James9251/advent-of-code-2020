def iterate_state_1(state):
    '''
    Returns a list the same length as the input, whose elements
    are the updated rows as strings according to the rules of puzzle 1
    '''
    # All rows are assumed to be equal length, with at least 1 row
    width = len(state[0])
    length = len(state)
    new_state = []
    for i in range(length):
        new_row = ''
        for j in range(width):
            # i, j are the seat coordinates
            current_occupant = state[i][j]
            if current_occupant == '.':
                new_row += '.'
                continue

            # Find the number of neighbouring occupied seats
            # These bounds account for edges
            down_bound = max(0, i - 1)
            up_bound = min(length, i + 2)
            left_bound = max(0, j - 1)
            right_bound = min(width, j + 2)
            neighbours = ''
            for k in range(down_bound, up_bound):
                neighbours += state[k][left_bound: right_bound]
            # neighbour_count and current_occupant are input for the automaton rules
            neighbour_count = neighbours.count('#') # Includes the seat occupant

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
# Opening the file containing the seating layout
with open('input.txt', 'r') as f:
    new_state = f.read().splitlines()
# Iterate until nothing changes
# Assumes the initial state will reach a fixed point
while old_state != new_state:
    new_state, old_state = iterate_state_1(new_state), new_state
number_occupied_seats = sum(x.count('#') for x in new_state)
print("Puzzle 1 answer = {}".format(number_occupied_seats))

def iterate_state_2(state):
    '''
    Returns a list the same length as the input, whose elements
    are the updated rows as strings according to the rules of puzzle 2
    '''
    # All rows are assumed to be equal length, with at least 1 row
    width = len(state[0])
    length = len(state)
    new_state = []
    for i in range(length):
        new_row = ''
        for j in range(width):
            # i, j are the seat coordinates
            current_occupant = state[i][j]
            if current_occupant == '.':
                new_row += '.'
                continue
                
            # Calculate the neighbours in line of sight
            # a and b define the direction from seat (i, j)
            neighbours = ''
            for a in range(-1, 2):
                for b in range(-1, 2):
                    x = i + a
                    y = j + b
                    while (0 <= x and x < length and 0 <= y and y < width):
                        if state[x][y] != '.':
                            neighbours += state[x][y]
                            break
                        x += a
                        y += b
            # neighbour_count and current_occupant are input for the automaton rules
            neighbour_count = neighbours.count('#') # Includes the seat occupant

            # The rules of the cellular automaton:
            if current_occupant == '#':
                if neighbour_count >= 5 + 1: # Avoids counting the occupant
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
# Reopening the file containing the seating layout
with open('input.txt', 'r') as f:
    new_state = f.read().splitlines()
# Iterate until nothing changes
# Assumes the initial state will reach a fixed point
while old_state != new_state:
    new_state, old_state = iterate_state_2(new_state), new_state
number_occupied_seats = sum(x.count('#') for x in new_state)
print("Puzzle 2 answer = {}".format(number_occupied_seats))
