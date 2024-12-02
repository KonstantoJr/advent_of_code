"""Solution for day 2 part 1"""


def check_safe(differences):
    ascending = None
    first = differences[0]

    if (first > 0) and first in {1, 2, 3}:
        ascending = True
    elif (first < 0) and first in {-1, -2, -3}:
        ascending = False
    else:
        return False

    for diff in differences:
        if ascending:
            if diff not in {1, 2, 3}:
                return False
        else:
            if diff not in {-1, -2, -3}:
                return False

    return True


with open('input.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()


for i, d in enumerate(data):
    data[i] = d.split(' ')

safe = 0

for report in data:
    current = None
    previous = None
    diff = None
    diffs = []
    for number in report:
        if current is None:
            current = int(number)
            continue
        previous = current
        current = int(number)
        diff = current - previous
        diffs.append(diff)
    if check_safe(diffs):
        safe += 1

print(safe)
