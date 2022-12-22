def wrap(x, y, dx, dy):
    if dx == 1:
        # Right
        if x == 150:
            return 100, 151-y, -1, 0
        if x == 100:
            if 51 <= y <= 100:
                return 100 + (y - 50), 50, 0, -1
            if 101 <= y <= 150:
                return 150, 51 - (y - 100), -1, 0
        if x == 50:
            return 50 + (y - 150), 150, 0, -1
    elif dx == -1:
        # Left
        if x == 51:
            if 1 <= y <= 50:
                return 1, 151 - y, 1, 0
            if 51 <= y <= 100:
                return y - 50, 101, 0, 1
        if x == 1:
            if 101 <= y <= 150:
                return 51, 1 + (150 - y), 1, 0
            if 151 <= y <= 200:
                return y - 150 + 50, 1, 0, 1
    elif dy == 1:
        # Down
        if y == 50:
            return 100, x - 50, -1, 0
        if y == 150:
            return 50, x + 100, -1, 0
        if y == 200:
            return x + 100, 1, 0, 1
    elif dy == -1:
        # Up
        if y == 1:
            if 51 <= x <= 100:
                return 1, x+100, 1, 0
            if 101 <= x <= 150:
                return x-100, 200, 0, -1
        if y == 101:
            return 51, x+50, 1, 0


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
                nx, ny, ndx, ndy = wrap(x, y, dx, dy)
                cell = grid[nx, ny]
                if cell == '#':
                    break  # Hit a wall!
                x, y = nx, ny
                dx, dy = ndx, ndy
            elif cell == '#':
                break
            x, y = nx, ny
    elif step == 'R':
        dy, dx = dx, -dy
    elif step == 'L':
        dx, dy = dy, -dx


print(1000 * y + 4 * x + facing[(dx, dy)])
