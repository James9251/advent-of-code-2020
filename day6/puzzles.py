import string

# Opening the file containing questionnaire information
with open('input.txt', 'r') as f:
    answer_file = f.read().splitlines()

# Lists of the two group answers in sets, under the different conditions
intersection_group_answers = []
union_group_answers = []
new_intersection_group = set(list(string.ascii_lowercase))
new_union_group = set()

for answer in answer_file:
    if answer == '':
        intersection_group_answers.append(new_intersection_group)
        union_group_answers.append(new_union_group)
        new_intersection_group = set(list(string.ascii_lowercase))
        new_union_group = set()
        continue
    new_intersection_group = new_intersection_group.intersection(set(list(answer)))
    new_union_group.update(set(list(answer)))

intersection_group_answers.append(new_intersection_group)
union_group_answers.append(new_union_group)
    
union_count = sum(len(x) for x in union_group_answers)
print('Part 1 total = {}'.format(union_count))
intersection_count = sum(len(x) for x in intersection_group_answers)
print('Part 2 total = {}'.format(intersection_count))