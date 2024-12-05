from collections import defaultdict


def check_correct_page(rules, page):
    for i, key in enumerate(page):
        for _, k in enumerate(page[i+1:]):
            if key in rules[k]:
                return False
    return True


def place_key(rules, page, key):
    for i in range(len(page)):
        for _, k in enumerate(page[i:]):
            if key in rules[k]:
                break
        else:
            page.insert(i, key)
            return
    page.append(key)


rules = defaultdict(set)
pages = []

with open('input.txt', 'r', encoding='utf-8') as f:
    ruling = True
    for line in f:
        if line == '\n':
            ruling = False
            continue
        if ruling:
            key, value = line.strip().split('|')
            key = int(key)
            value = int(value)
            rules[key].add(value)
        else:
            pages.append([int(i) for i in line.strip().split(',')])


correct_pages = []

for i, page in enumerate(pages):
    if check_correct_page(rules, page):
        continue
    current_page = list(page)
    temp_page = []
    temp_page.append(current_page.pop(0))
    while len(current_page) > 0:
        key = current_page.pop(0)
        place_key(rules, temp_page, key)

    correct_pages.append(temp_page)

# for i, page in enumerate(correct_pages):
#     print('Page {}: {}'.format(i, page))


middle_total = 0

for i, page in enumerate(correct_pages):
    middle_index = len(page) // 2
    middle_total += page[middle_index]

print(middle_total)
