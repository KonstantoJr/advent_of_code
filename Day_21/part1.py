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
print(monkeys['root'].number)
