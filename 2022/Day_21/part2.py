import re


class Monkey:
    def __init__(self, *kwargs):
        if len(kwargs) == 1:
            self.number = kwargs[0]
        else:
            self.number = None
            self.monkey1 = kwargs[0]
            self.operation = kwargs[1]
            self.monkey2 = kwargs[2]

    def __str__(self):
        if self.number:
            return self.number
        else:
            return f'{self.monkey1} {self.operation} {self.monkey2}'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()


monkeys = {}


for monkey in data:
    monkey = monkey.split()
    name = monkey[0][:-1]
    # print(monkey)
    if len(monkey) <= 2:
        monkeys[name] = Monkey(monkey[1])
    else:
        monkeys[name] = Monkey(monkey[1], monkey[2], monkey[3])


monkey1 = monkeys['root'].monkey1
monkey2 = monkeys['root'].monkey2
print(monkey1, monkey2)

# find which monkeys helped monkey1 and monkey2 find their numbers


def find_monkeys(monkey):
    if monkeys[monkey].number:
        return monkey
    else:
        return (find_monkeys(monkeys[monkey].monkey1), monkeys[monkey].operation, find_monkeys(monkeys[monkey].monkey2))


def unpack(monkey):
    monkeys = []
    for m in monkey:
        if isinstance(m, tuple):
            monkeys.extend(unpack(m))
        else:
            monkeys.append(m)
    return monkeys


monkeys1 = unpack(find_monkeys(monkey1))
monkeys2 = unpack(find_monkeys(monkey2))
if 'humn' in monkeys1:
    temp = str(find_monkeys(monkey1))
else:
    temp = str(find_monkeys(monkey2))
#
while monkeys['root'].number == None:
    for monkey in monkeys:
        if monkeys[monkey].number == None:
            # Check if monkey1 and monkey2 are numbers
            if monkeys[monkeys[monkey].monkey1].number and monkeys[monkeys[monkey].monkey2].number:
                if monkeys[monkey].operation == '+':
                    monkeys[monkey].number = int(
                        monkeys[monkeys[monkey].monkey1].number) + int(monkeys[monkeys[monkey].monkey2].number)
                elif monkeys[monkey].operation == '*':
                    monkeys[monkey].number = int(
                        monkeys[monkeys[monkey].monkey1].number) * int(monkeys[monkeys[monkey].monkey2].number)
                elif monkeys[monkey].operation == '-':
                    monkeys[monkey].number = int(
                        monkeys[monkeys[monkey].monkey1].number) - int(monkeys[monkeys[monkey].monkey2].number)
                elif monkeys[monkey].operation == '/':
                    monkeys[monkey].number = int(
                        monkeys[monkeys[monkey].monkey1].number) / int(monkeys[monkeys[monkey].monkey2].number)


# print(monkeys[monkey1].number, 'humn' in monkeys1)
# print(monkeys[monkey2].number, 'humn' in monkeys2)
# find what humn number must be so monkey1.number == monkey2.number
temp = temp.replace(',', '')
# print(temp)

# write regex to find stuff inside '' in the following format and replace it with the correct number
# (('sllz', '+', ('ljgn', '*', ('humn', '-', 'dvpt'))), '/', 'lfqf')
# regex to find all stuff inside ' '
inside = re.findall(r"'(.*?)'", temp)
for i in inside:
    if i in monkeys and i != 'humn':
        # print(f"'{i}'")
        temp = temp.replace(f"'{i}'", monkeys[i].number)
    if i in ['+', '-', '*', '/']:
        temp = temp.replace(f"'{i}'", i)


monkeys['humn'].number = 3_220_993_869_433
while monkeys[monkey1].number != monkeys[monkey2].number:
    # print(monkeys[monkey1].number,
    #   monkeys[monkey2].number, monkeys['humn'].number)
    if 'humn' in monkeys1:
        new_temp = temp.replace('humn', str(monkeys['humn'].number))
        new_temp = new_temp.replace("'", '')
        monkeys[monkey1].number = int(eval(new_temp))
    else:
        new_temp = temp.replace('humn', str(monkeys['humn'].number))
        new_temp = new_temp.replace("'", '')
        monkeys[monkey2].number = int(eval(new_temp))
    monkeys['humn'].number += 1
print(monkeys['humn'].number - 1)
