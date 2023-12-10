"""Day 10 part 1"""
PIPES = {
    '|': ('N', 'S'),
    '-': ('E', 'W'),
    'L': ('N', 'E'),
    'J': ('N', 'W'),
    '7': ('S', 'W'),
    'F': ('S', 'E'),
}


def input_parse():
    with open('example.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


def main():
    # Find S in the grid
    grid = input_parse()
    for i, row in enumerate(grid):
        if 'S' in row:
            start = (i, row.index('S'))
            break

    # Find the direction of the pipe
    # Check the surrounding pipes
    # And check if it connects to the start
    is_connected_from_top = False
    is_connected_from_bottom = False
    is_connected_from_left = False
    is_connected_from_right = False

    # Check top
    if start[0] - 1 >= 0:
        if grid[start[0] - 1][start[1]] in PIPES:
            if PIPES[grid[start[0] - 1][start[1]]][0] == 'S' or PIPES[grid[start[0] - 1][start[1]]][1] == 'S':
                is_connected_from_top = True
    # Check bottom
    if start[0] + 1 < len(grid):
        if grid[start[0] + 1][start[1]] in PIPES:
            if PIPES[grid[start[0] + 1][start[1]]][0] == 'N' or PIPES[grid[start[0] + 1][start[1]]][1] == 'N':
                is_connected_from_bottom = True
    # Check left
    if start[1] - 1 >= 0:
        if grid[start[0]][start[1] - 1] in PIPES:
            if PIPES[grid[start[0]][start[1] - 1]][0] == 'E' or PIPES[grid[start[0]][start[1] - 1]][1] == 'E':
                is_connected_from_left = True
    # Check right
    if start[1] + 1 < len(grid[0]):
        if grid[start[0]][start[1] + 1] in PIPES:
            if PIPES[grid[start[0]][start[1] + 1]][0] == 'W' or PIPES[grid[start[0]][start[1] + 1]][1] == 'W':
                is_connected_from_right = True

    # Determin the starting pipe
    if is_connected_from_top and is_connected_from_bottom:
        start_pipe = '|'
    elif is_connected_from_left and is_connected_from_right:
        start_pipe = '-'
    elif is_connected_from_top and is_connected_from_right:
        start_pipe = 'L'
    elif is_connected_from_top and is_connected_from_left:
        start_pipe = 'J'
    elif is_connected_from_bottom and is_connected_from_left:
        start_pipe = '7'
    elif is_connected_from_bottom and is_connected_from_right:
        start_pipe = 'F'
    else:
        raise Exception('Invalid starting pipe')

    # Find the path
    path = [grid[start[0]][start[1]]]
    current = start
    direction = PIPES[start_pipe][0]
    came_from = None
    # The end of the path is the start

    while True:
        # Move to the next pipe
        if direction == 'N':
            current = (current[0] - 1, current[1])
            came_from = 'S'
        elif direction == 'S':
            current = (current[0] + 1, current[1])
            came_from = 'N'
        elif direction == 'E':
            current = (current[0], current[1] + 1)
            came_from = 'W'
        elif direction == 'W':
            current = (current[0], current[1] - 1)
            came_from = 'E'
        else:
            raise Exception('Invalid direction')

        # Check if the pipe is valid
        if current == start:
            break
        if current[0] < 0 or current[0] >= len(grid):
            raise Exception('Invalid pipe')
        if current[1] < 0 or current[1] >= len(grid[0]):
            raise Exception('Invalid pipe')
        if grid[current[0]][current[1]] not in PIPES:
            raise Exception('Invalid pipe')

        # Add the pipe to the path
        path.append(grid[current[0]][current[1]])

        # Change direction
        direction = PIPES[grid[current[0]][current[1]]][0]
        if direction == came_from:
            direction = PIPES[grid[current[0]][current[1]]][1]

    return path


if __name__ == '__main__':
    PATH = main()
    print(''.join(PATH))
    print(len(PATH))
    print(f'Solution: {len(PATH) / 2}')
