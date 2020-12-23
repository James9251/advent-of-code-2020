import re

# Opening the list of baggage rules into a list
with open('input.txt', 'r') as f:
    rules = f.read().splitlines()

# A dictionary to contain each bag's contents
bag_contents = {}
for rule in rules:
    bag_list = re.findall(r'([a-z]* [a-z]*) bag', rule)
    if 'no other' in bag_list:
        bag_contents.update({bag_list[0]:[]})
    else:
        bag_contents.update({bag_list[0]:bag_list[1:]})

def can_contain_shiny_gold(bag_colour):
    '''
    Recursive function that returns True when this bag colour can eventually
    hold a shiny gold bag.
    But does a shiny gold bag contain itself?
    '''
    if 'shiny gold' in bag_contents[bag_colour]:
        return True
    for bag in bag_contents[bag_colour]:
        if can_contain_shiny_gold(bag):
            return True
    return False

bag_count = 0
for bag in bag_contents.keys():
    if can_contain_shiny_gold(bag):
        bag_count += 1

print("The number of bags that can eventually hold shiny gold is {}".format(bag_count))