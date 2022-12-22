with open('input.txt', 'r') as f:
    data = f.read().splitlines()

directions = []
dir = ""
for char in data[-1]:
    if char.isdigit():
        dir += char
    else:
        directions.append(int(dir))
        dir = ""
        directions.append(char)
if dir != "":
    directions.append(int(dir))


grid = {}
curPos = None
for y, line in enumerate(data, start=1):
    for x, val in enumerate(line, start=1):
        if val in '.#':
            if val == '.' and curPos is None:
                curPos = (x, y)
            grid[x, y] = val

# print(directions)


facing = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}

dx = 1
dy = 0
x, y = curPos
for step in directions:
    if isinstance(step, int):
        for _ in range(step):
            nx, ny = x+dx, y+dy
            cell = grid.get((nx, ny))
            if cell is None:
                # WRAP
                nnx, nny = x, y
                while (nnx, nny) in grid:
                    nx, ny = nnx, nny
                    nnx -= dx
                    nny -= dy
                cell = grid[nx, ny]
            if cell == '#':
                break  # Hit a wall!
            x, y = nx, ny
    elif step == 'R':
        dy, dx = dx, -dy
    elif step == 'L':
        dx, dy = dy, -dx


print(1000 * y + 4 * x + facing[(dx, dy)])
