from functools import lru_cache


class Pipe:
    def __init__(self, name, rate, lead) -> None:
        self.name = name
        self.rate = rate
        self.lead = lead

    def __repr__(self) -> str:
        return f'{self.name} {self.rate} {self.lead}'


@lru_cache(maxsize=None)
def findMaxFlow(pipe, opened, min_left):
    global pipes
    if min_left <= 0:
        return 0
    best = 0
    if pipe not in opened:
        val = (min_left - 1) * pipes[pipe].rate
        cur_opened = tuple(sorted(opened + (pipe,)))
        for neighbor in pipes[pipe].lead:
            if pipe not in opened and val:
                best = max(best, val + findMaxFlow
                           (neighbor,
                            cur_opened, min_left - 2))
            best = max(best,  findMaxFlow
                       (neighbor, opened, min_left - 1))
    else:
        for neighbor in pipes[pipe].lead:
            best = max(best, findMaxFlow
                       (neighbor, opened, min_left - 1))
    return best


@lru_cache(maxsize=None)
def findMaxFlowWithElephant(pipe, opened, min_left):
    global pipes
    if min_left <= 0:
        # print(opened)
        return findMaxFlow('AA', opened, 26)

    best = 0
    if pipe not in opened:
        val = (min_left - 1) * pipes[pipe].rate
        cur_opened = tuple(sorted(opened + (pipe,)))
        for neighbor in pipes[pipe].lead:
            if pipe not in opened and val:
                best = max(best, val + findMaxFlowWithElephant
                           (neighbor,
                            cur_opened, min_left - 2))
            best = max(best,  findMaxFlowWithElephant
                       (neighbor, opened, min_left - 1))
    else:
        for neighbor in pipes[pipe].lead:
            best = max(best, findMaxFlowWithElephant
                       (neighbor, opened, min_left - 1))
    return best


with open('test.txt', 'r') as f:
    data = f.read().splitlines()

pipes = {}

for line in data:
    word = line.split()
    name = word[1]
    rate = int(word[4][5:-1])
    lead = word[9:]
    for i in range(len(lead)):
        lead[i] = lead[i].replace(",", "")
    # print(name, rate, lead)
    pipes[name] = (Pipe(name, rate, lead))


print(findMaxFlowWithElephant('AA', (), 26))
