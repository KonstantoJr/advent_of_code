"""Solution for day 2 part 2"""

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

print(safe)
