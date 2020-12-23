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

max_seat_id = 0
for seat_position in seating_file:
    seat_id = seat_position_to_id(seat_position)
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print("The highest seat id on the flight is {}".format(max_seat_id))