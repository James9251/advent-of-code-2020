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