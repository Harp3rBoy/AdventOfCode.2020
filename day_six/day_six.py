f = open("input.txt", "r")
lines = f.read().split("\n")
groups = []
group = ''
for line in lines:
    if line != '':
        group += line
    else:
        groups += [group]
        group = ''
groups += [group]
f.close()


def part1(file):
    group_answers = []
    for answers in file:
        answers_set = set(answers)
        group_answers.append(len(answers_set))
    return sum(group_answers)


print(part1(groups))
