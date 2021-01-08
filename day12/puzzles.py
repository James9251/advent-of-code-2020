from math import pi, sin, cos

# Open the file containing direction instructions
with open('input.txt', 'r') as f:
    directions = f.read().splitlines()

def decode(direction):
    '''
    Takes as input a string representing a direction
    Return a tuple containing the letter and integer parts
    '''
    letter = direction[0]
    scalar = int(direction[1:])
    return (letter, scalar)

def follow_direction_1(x, y, theta, direction):
    '''
    Takes as input x, y coordinates and an angle theta
    These values are adjusted depending on the direction input
    Returns the new tuple (x, y, theta)
    Follows the directions according to the rules in puzzle 1.
    '''
    letter, scalar = decode(direction)
    degrees_to_radians = pi / 180
    two_pi = 2 * pi
    if letter == 'N':
        y += scalar
        return (x, y, theta)
    elif letter == 'S':
        y -= scalar
        return (x, y, theta)
    elif letter == 'E':
        x += scalar
        return (x, y, theta)
    elif letter == 'W':
        x -= scalar
        return (x, y, theta)
    elif letter == 'L':
        theta = (theta + degrees_to_radians * scalar) % two_pi
        return (x, y, theta)
    elif letter == 'R':
        theta = (theta - degrees_to_radians * scalar) % two_pi
        return (x, y, theta)
    elif letter == 'F':
        x += scalar * cos(theta)
        y += scalar * sin(theta)
        return (x, y, theta)
    return
    
x = 0
y = 0
theta = 0 # As in conventional polar coordinates to face East
for direction in directions:
    x, y, theta = follow_direction_1(x, y, theta, direction)
manhattan_distance = abs(x) + abs(y)
print("Puzzle 1 Manhattan distance from starting point = {}".format(manhattan_distance))

def follow_direction_2(ship_x, ship_y, wp_x, wp_y, direction):
    '''
    Takes inputs ship_x, ship_y: the ship's coordinates
    Takes inputs wp_x, wp: the waypoint's coordinates
    Direction is interpreted as per puzzle 2 instructions
    Returns the new tuple (x, y, theta)
    Follows the directions according to the rules in puzzle 1.
    '''
    letter, scalar = decode(direction)
    degrees_to_radians = pi / 180
    two_pi = 2 * pi
    cos_s = cos(scalar * degrees_to_radians)
    sin_s = sin(scalar * degrees_to_radians)
    # The waypoint's relative position
    rel_x = wp_x - ship_x
    rel_y = wp_y - ship_y
    if letter == 'N':
        wp_y += scalar
        return (ship_x, ship_y, wp_x, wp_y)
    elif letter == 'S':
        wp_y -= scalar
        return (ship_x, ship_y, wp_x, wp_y)
    elif letter == 'E':
        wp_x += scalar
        return (ship_x, ship_y, wp_x, wp_y)
    elif letter == 'W':
        wp_x -= scalar
        return (ship_x, ship_y, wp_x, wp_y)
    elif letter == 'L':
        wp_x = ship_x + cos_s * rel_x - sin_s * rel_y
        wp_y = ship_y + sin_s * rel_x + cos_s * rel_y
        return (ship_x, ship_y, wp_x, wp_y)
    elif letter == 'R':
        wp_x = ship_x + cos_s * rel_x + sin_s * rel_y
        wp_y = ship_y - sin_s * rel_x + cos_s * rel_y
        return (ship_x, ship_y, wp_x, wp_y)
    elif letter == 'F':
        x_displacement = scalar * rel_x
        y_displacement = scalar * rel_y
        ship_x += x_displacement
        ship_y += y_displacement
        wp_x += x_displacement
        wp_y += y_displacement
        return (ship_x, ship_y, wp_x, wp_y)
    return

# Ship and waypoint starting coordinates    
ship_x = 0
ship_y = 0
wp_x = 10
wp_y = 1
for direction in directions:
    ship_x, ship_y, wp_x, wp_y = follow_direction_2(ship_x, ship_y, wp_x, wp_y, direction)
manhattan_distance = abs(ship_x) + abs(ship_y)
print("Puzzle 2 Manhattan distance from starting point = {}".format(manhattan_distance))