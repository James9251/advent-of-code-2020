# The starting numbers given were small enough here
starting_numbers = [2, 0, 1, 9, 5, 19]

def new_turn(history, next_number):
    '''
    Takes as input a dictionary of previously said numbers as keys,
    so that history[n] is how many turns ago n was said.
    Takes the next_number to be played, and plays it.
    Returns the updated history dictionary and the new next_number.
    Avoids keeping a huge list of turns.
    '''
    for key in history.keys():
        history[key] += 1
    if next_number in history.keys():
        x = history[next_number]
        history[next_number] = 0
        return (history, x)
    history.update({next_number:0})
    return (history, 0)

# No need to keep a giant list
history = {}
# Play the start of game rules
for n in starting_numbers:
    history, next_number = new_turn(history, n)
# Now play the main game
for i in range(len(starting_numbers) + 1, 2020):
    history, next_number = new_turn(history, next_number)
print("Solution to puzzle 1 = {}".format(next_number))