import re


def get_value(str):
    a = int(str.split("(")[1].split(",")[0])
    b = int(str.split(",")[1].split(")")[0])
    return a * b


pattern = r"mul\(\d{1,3},\d{1,3}\)"


with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()


muls = []
for line in data:
    if re.search(pattern, line):
        matches = re.findall(pattern, line)
        # append all matches to the list
        muls.extend(matches)

solution = 0
for i in muls:
    solution += get_value(i)
print(solution)
