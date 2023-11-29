def drawGrid():
    global grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='')
        print()


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

grid = [['.' for _ in range(800)] for _ in range(200)]
maxY = 0
for row in data:
    direction = row.split('->')
    for i in range(len(direction)-1):
        x1, y1 = direction[i].split(',')
        x2, y2 = direction[i+1].split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        x1 = x1
        x2 = x2
        maxY = max(maxY, y1, y2)
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                grid[y][x1] = '#'
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                grid[y1][x] = '#'

for i in range(len(grid[0])):
    grid[maxY + 2][i] = '#'
# drawGrid()


def placeSand(x, y):
    global grid, done, start
    if grid[start[1]][start[0]] == 'o':
        done = True
        return
    if grid[y+1][x] == '#' or grid[y+1][x] == 'o':
        if grid[y+1][x-1] == '#' or grid[y+1][x-1] == 'o':
            if grid[y+1][x+1] == '#' or grid[y+1][x+1] == 'o':
                grid[y][x] = 'o'
                return
            else:
                placeSand(x+1, y+1)
        else:
            placeSand(x-1, y+1)
    else:
        placeSand(x, y+1)
    return


start = (500, 0)
sand = 0
done = False
while not done:
    for y in range(start[1], len(grid)):
        if grid[y][start[0]] == '#' or grid[y][start[0]] == 'o':
            break
    pos = (start[0], y-1)
    # print(pos)
    # drawGrid()
    sand += 1
    placeSand(pos[0], pos[1])


# drawGrid()
print(sand - 1)
