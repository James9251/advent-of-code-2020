# Opening the file containing questionnaire information
with open('input.txt', 'r') as f:
    answer_file = f.read().splitlines()

group_answers = []
new_answers = set()
for answer in answer_file:
    if answer == '':
        group_answers.append(new_answers)
        new_answers = set()
        continue
    new_answers.update(set(list(answer)))
if len(new_answers) > 0:
    group_answers.append(new_answers)
    
count = sum(len(x) for x in group_answers)
print('Total = {}'.format(count))