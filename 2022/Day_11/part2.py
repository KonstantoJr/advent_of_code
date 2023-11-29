from collections import defaultdict


class Monkey:
    def __init__(self, id, startingItems, operation, divisable, throw):
        self.id = int(id)
        self.startingItems = startingItems
        self.operation = operation
        self.divisable = divisable
        self.throw = throw
        self.inspectCount = 0

    def inspect(self):
        global allDivisors
        self.inspectCount += 1
        item = self.startingItems.pop(0)
        # print(self.operation)
        if '*' in self.operation:
            number = self.operation.split('*')[1]
            if number == ' old':
                number = item
            else:
                number = int(number)
            item *= number
            # item = item // 3
            item = item % allDivisors
        elif '+' in self.operation:
            number = self.operation.split('+')[1]
            if number == ' old':
                number = item
            else:
                number = int(number)
            item += number
            # item = item // 3
            item = item % allDivisors

        if item % self.divisable == 0:
            return (item, self.throw[0])

        return (item, self.throw[1])


with open('input.txt', 'r') as f:
    data = f.read().splitlines()


monkeys = []
singleMonkey = []
allDivisors = 1
for line in data:
    if line != '':
        singleMonkey.append(line)
    else:
        id = singleMonkey[0].split(' ')[1][0]
        startingItems = singleMonkey[1].split(':')[1].split(',')
        startingItems = [int(x) for x in startingItems]
        operation = singleMonkey[2].split('=')[1]
        divisable = int(singleMonkey[3].split('by')[1])
        trueOperation = singleMonkey[4].split('monkey')[1]
        falseOperation = singleMonkey[5].split('monkey')[1]
        print(id, startingItems, operation, divisable,
              trueOperation, falseOperation)
        monkeys.append(Monkey(id, startingItems, operation,
                       divisable, (trueOperation, falseOperation)))
        allDivisors *= divisable
        singleMonkey = []

previousInspection = [0 for _ in range(len(monkeys))]
for _ in range(10_000):
    for monkey in monkeys:
        while len(monkey.startingItems) > 0:
            item, id = monkey.inspect()
            monkeys[int(id)].startingItems.append(item)

ans = []
for monkey in monkeys:
    print(monkey.id, monkey.inspectCount)
    ans.append(monkey.inspectCount)
ans.sort()
print(ans[-1] * ans[-2])
