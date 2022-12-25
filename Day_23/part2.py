def getAdjacent(x, y):
    adj = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            adj.append((x+i, y+j))
    return adj


def findRectangle(minX, maxX, minY, maxY):
    # return the points inside the rectangle
    # row length
    rowLength = maxX - minX + 1
    # column length
    colLength = maxY - minY + 1
    # number of points
    return rowLength * colLength


def getNorth(x, y):
    return [(x-1, y), (x-1, y-1), (x-1, y+1)]


def getSouth(x, y):
    return [(x+1, y), (x+1, y-1), (x+1, y+1)]


def getWest(x, y):
    return [(x, y-1), (x-1, y-1), (x+1, y-1)]


def getEast(x, y):
    return [(x, y+1), (x-1, y+1), (x+1, y+1)]


def findMovement(elf, round, moves, elves):
    # if the elves has no elves in north he moves north
    # if the elves has no elves in south he moves south
    # if the elves has no elves in west he moves west
    # if the elves has no elves in east he moves east
    nextStep = elf
    for _ in range(4):
        move = moves[round % 4]
        round += 1
        if move == 'north':
            adj = getNorth(*elf)
            nextStep = (elf[0]-1, elf[1])
        elif move == 'south':
            adj = getSouth(*elf)
            nextStep = (elf[0]+1, elf[1])
        elif move == 'west':
            adj = getWest(*elf)
            nextStep = (elf[0], elf[1]-1)
        elif move == 'east':
            adj = getEast(*elf)
            nextStep = (elf[0], elf[1]+1)
        if not any(a in elves for a in adj):
            return nextStep
    return elf


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

elves = set()

for x in range(len(data)):
    for y in range(len(data[x])):
        if data[x][y] == '#':
            elves.add((x, y))

moves = ['north', 'south', 'west', 'east']

numberOfElves = len(elves)
print(numberOfElves)
round = 0
while True:
    proposed = {}
    noMoves = 0
    # First half
    for elf in elves:
        adj = getAdjacent(*elf)
        for a in adj:
            if a in elves:
                proposed[elf] = findMovement(elf, round, moves, elves)
                break
        else:
            noMoves += 1
            proposed[elf] = elf
    if noMoves == numberOfElves:
        break
    # Second half
    newPositions = list(proposed.values())
    for elf in proposed:
        if newPositions.count(proposed[elf]) > 1:
            proposed[elf] = elf
    elves = set(list(proposed.values()))
    round += 1
    print("Round: " + str(round) + " No moves: " + str(noMoves))

print(round + 1)


# minX = min(elves, key=lambda x: x[0])[0]
# minY = min(elves, key=lambda x: x[1])[1]
# maxX = max(elves, key=lambda x: x[0])[0]
# maxY = max(elves, key=lambda x: x[1])[1]

# print(findRectangle(minX, maxX, minY, maxY) - len(elves))

# for x in range(minX, maxX+1):
#     for y in range(minY, maxY+1):
#         if (x, y) in elves:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()
