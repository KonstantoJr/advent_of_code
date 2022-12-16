class Pipe:
    def __init__(self, name, rate, lead) -> None:
        self.name = name
        self.rate = rate
        self.lead = lead
        self.open = False

    def __repr__(self) -> str:
        return f'{self.name} {self.rate} {self.lead}'


def find_path_to_highest_rate_pipe(pipes, pos):
    temp = [pipe for pipe in pipes.values() if not pipe.open]
    temp.sort(key=lambda x: x.rate, reverse=True)
    print(temp)
    destination = temp[0]
    path = dfs(pipes, pos, destination, [pos])
    print(path)
    return path[1]


def dfs(pipes, pos, destination, path):
    if pos == destination.name:
        return path
    for lead in pipes[pos].lead:
        if lead in path:
            continue
        path.append(lead)
        result = dfs(pipes, lead, destination, path)
        if result:
            return result
        path.pop()
    return None


def calculate_pressure(pipes):
    pressure = 0
    for pipe in pipes.values():
        if pipe.open:
            print(pipe.name, end=" ")
            pressure += pipe.rate
    print()
    return pressure


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
    pipes[name] = (Pipe(name, rate, lead))

pos = "AA"
pressure = 0
for remaining in range(1, 31):
    pipe = pipes[pos]
    if pipe.rate > 0 and not pipe.open:
        pipe.open = True
    else:
        pos = find_path_to_highest_rate_pipe(pipes, pos)
    print(f'Minute {remaining}')
    pressure += calculate_pressure(pipes)
    print(f'move to {pos}')
