"""Solution for day 2 part 2"""

def check_reports(reports_diffs):
    for diffs in reports_diffs:
        if check_safe(diffs):
            break
    else:
        return False
    return True



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
    current_reports = []
    for i in range(len(report)):
        current = None
        previous = None
        diff = None
        diffs = []
        for j ,number in enumerate(report):
            if (i == j):
                continue
            if current is None:
                current = int(number)
                continue
            previous = current
            current = int(number)
            diff = current - previous

            diffs.append(diff)
        current_reports.append(diffs)
        print(current_reports)
    if check_reports(current_reports):
        safe += 1

print(safe)
