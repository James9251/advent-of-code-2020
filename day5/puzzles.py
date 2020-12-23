import sys

# Opening the file containing seat numbers
with open('input.txt', 'r') as f:
    seating_file = f.read().splitlines()

def seat_position_to_id(seat_position):
    '''
    Takes a binary space partitioned seat position as input:
    seat_position is a string of 10 letters, all in "FBRL"
    '''
    to_binary = {'F':'0', 'B':'1', 'L':'0', 'R':'1'}
    binary_string = ''.join(to_binary[x] for x in seat_position)
    return int(binary_string, 2)

seat_ids = [seat_position_to_id(seat_position) for seat_position in seating_file]
max_seat_id = max(seat_ids)
min_seat_id = min(seat_ids)
print("The highest seat id on the flight is {}".format(max_seat_id))

# We don't worry about the bounds here as they don't include the seat we're searching for
for i in range(min_seat_id, max_seat_id):
    if not i in seat_ids:
        print("Seat id {} is missing from the manifest".format(i))