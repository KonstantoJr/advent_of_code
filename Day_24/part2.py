with open('input.txt', 'r') as f:
    data = f.read().splitlines()
data = [list(i) for i in data]

directions = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1),
    'W': (0, 0),
}

PERIOD = len(data[0]) * len(data)


def nextGrid(currentGrid):
    newGrid = [list('.'*len(currentGrid[0]))
               for _ in range(len(currentGrid))]
    for i in range(len(currentGrid)):
        for j in range(len(currentGrid[0])):
            if currentGrid[i][j] == '#':
                newGrid[i][j] = '#'
            elif currentGrid[i][j] != '.':
                blizzards = list(currentGrid[i][j])
                for b in range(len(blizzards)):
                    direction = directions[blizzards[b]]
                    x = j + direction[0]
                    y = i + direction[1]
                    if currentGrid[y][x] == '#':
                        if blizzards[b] == '>':
                            x = 1
                        elif blizzards[b] == '<':
                            x = len(currentGrid[0]) - 2
                        elif blizzards[b] == '^':
                            y = len(currentGrid) - 2
                        elif blizzards[b] == 'v':
                            y = 1
                    if newGrid[y][x] == '.':
                        newGrid[y][x] = blizzards[b]
                    else:
                        newGrid[y][x] += blizzards[b]
    return newGrid


def bfs(start, finish, grid):
    global grids
    moves = []
    history = {}
    solution = []

    moves.append(["", start[0], start[1], grid])
    cle = (finish[0], finish[1], grid)
    history[cle] = 1

    while len(moves) > 0:
        nextMoves = []

        for i in range(len(moves)):
            etat = moves[i]
            if (etat[1], etat[2]) == finish:
                solution.append(etat[0])
                break

            newGrid = (etat[3] + 1) % PERIOD
            if newGrid not in grids:
                grids[newGrid] = nextGrid(grids[etat[3]])

            x, y = etat[1], etat[2]

            for direction in directions:
                a = x + directions[direction][0]
                b = y + directions[direction][1]
                if a < 0 or a >= len(grids[newGrid][0]) or b < 0 or b >= len(grids[newGrid]):
                    continue
                if grids[newGrid][b] and grids[newGrid][b][a] == '.':
                    cle = (a, b, newGrid)
                    if cle not in history:
                        history[cle] = 1
                        nextMoves.append([etat[0] + direction, a, b, newGrid])
        moves = nextMoves

    solution = sorted(solution, key=lambda x: len(x))
    return solution[0]


grids = {}
grids[0] = data
start = (1, 0)
finish = (len(data[-1]) - 2, len(data) - 1)

firstTrip = bfs(start, finish, 0)
print('Done with first trip')
secondTrip = bfs(finish, start, len(firstTrip))
print('Done with second trip')
thirdTrip = bfs(start, finish, len(firstTrip) + len(secondTrip))
print('Done with third trip')
print(len(firstTrip) + len(secondTrip) + len(thirdTrip))
