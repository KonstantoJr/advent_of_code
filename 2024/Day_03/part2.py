import re

MUL = r'mul\(\d{1,3},\d{1,3}\)'
DO = r'do\(\)'
DONT = r"don't\(\)"


with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()

data = "".join(data)

# find the index of all the instances of the string "do()" and "don't()"

dos = [{'value': m.start(), 'name': 'do'} for m in re.finditer(DO, data)]
donts = [{'value': m.start(), 'name': 'dont'} for m in re.finditer(DONT, data)]

# combine the two lists and sort them by the index value
all = dos + donts
all.sort(key=lambda x: x['value'])

# loop through the all list and remove everything that comes after the dont() string but before the do() string
new_data = ""
previous = {
    'name': 'do',
    'value': 0
}
for i, _ in enumerate(all):
    if all[i]['name'] == 'dont' and previous['name'] == 'do':
        new_data += data[previous['value']:all[i]['value']]
    if all[i]['name'] == 'do' and previous['name'] == 'do':
        new_data += data[previous['value']:all[i]['value']]
    previous = all[i]

if previous['name'] == 'do':
    new_data += data[previous['value']:]


print(len(new_data), len(data))
muls = []
for line in new_data.splitlines():
    if re.search(MUL, line):
        matches = re.findall(MUL, line)
        muls.extend(matches)

solution = 0
for i in muls:
    a = int(i.split("(")[1].split(",")[0])
    b = int(i.split(",")[1].split(")")[0])
    solution += a * b
print(solution)
