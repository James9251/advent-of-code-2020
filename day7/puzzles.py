import re

# Opening the list of baggage rules into a list
with open('input.txt', 'r') as f:
    rules = f.read().splitlines()

# A dictionary to contain each bag's contents
bag_contents = {}
for rule in rules:
    bag_list = re.findall(r'([a-z]* [a-z]*) bag', rule)
    number_list = [int(x) for x in re.findall(r' ([0-9])* ', rule)]
    if 'no other' in bag_list:
        bag_contents.update({bag_list[0]:[[],[]]})
    else:
        bag_contents.update({bag_list[0]:[bag_list[1:], number_list]})

def can_contain_shiny_gold(bag_colour):
    '''
    Recursive function that returns True when this bag colour can eventually
    hold a shiny gold bag.
    But does a shiny gold bag contain itself? No, bags must follow the axiom of regularity.
    '''
    if 'shiny gold' in bag_contents[bag_colour][0]:
        return True
    for bag in bag_contents[bag_colour][0]:
        if can_contain_shiny_gold(bag):
            return True
    return False

bag_count = 0
for bag in bag_contents.keys():
    if can_contain_shiny_gold(bag):
        bag_count += 1

print("The number of bags that can eventually hold shiny gold is {}".format(bag_count))

def number_of_contained_bags(bag_colour):
    '''
    Returns the number of bags that must be contained with a bag of the given colour
    '''
    bag_colours, bag_numbers = bag_contents[bag_colour]
    if len(bag_colours) == 0:
        return 0
    bag_count = 0
    for bag, number in zip(bag_colours, bag_numbers):
        bag_count += number * (1 + number_of_contained_bags(bag))
    return bag_count

number_required_bags = number_of_contained_bags('shiny gold')
print("The number of bags contained within one shiny gold bag is {}.".format(number_required_bags))