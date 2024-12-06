def guard_loop(grid, start):
    starting_position = tuple(start)
    direction ={
        'UP': (-1, 0),
        'DOWN': (1, 0),
        'LEFT': (0, -1),
        'RIGHT': (0, 1)
    }
    current_direction = 'UP'
    visited = {
        starting_position: [current_direction]
    }

    escaped = False
    loop = False
    while True:
        x , y = starting_position
        new_x, new_y = x + direction[current_direction][0], y + direction[current_direction][1]

        # Check if the new position is within the grid
        if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
            escaped = True
            break
        
        if (new_x, new_y) in visited and current_direction in visited[(new_x, new_y)]:
            loop = True
            break


        # Check if the new position is a wall
        if grid[new_x][new_y] == '#':
            # Turn right
            current_direction = {
                'UP': 'RIGHT',
                'RIGHT': 'DOWN',
                'DOWN': 'LEFT',
                'LEFT': 'UP'
            }[current_direction]
        else:
            starting_position = (new_x, new_y)
            visited.setdefault(starting_position, []).append(current_direction)

    if escaped:
        return False
    return loop



with open('input.txt', 'r', encoding='utf-8') as f:
    grid = f.read().splitlines()



starting_position = (0, 0)

for x , line in enumerate(grid):
    for y, char in enumerate(line):
        if char == '^':
            starting_position = (x, y)
            break
    if starting_position != (0, 0):
        break

obstacles = 0

for x , line in enumerate(grid):
    for y, char in enumerate(line):
        if char == '.':
            new_grid = [list(row) for row in grid]
            new_grid[x][y] = '#'
            if guard_loop(new_grid, starting_position):
                print(x, y)
                obstacles += 1

print(obstacles)