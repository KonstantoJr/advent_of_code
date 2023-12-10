"""Day 10 part 2"""
import matplotlib.pyplot as plt


PIPES = {
    '|': ('N', 'S'),
    '-': ('E', 'W'),
    'L': ('N', 'E'),
    'J': ('N', 'W'),
    '7': ('S', 'W'),
    'F': ('S', 'E'),
}


def input_parse():
    with open('input.txt', 'r', encoding='utf-8') as f:
        return [[char for char in line.strip()] for line in f.readlines()]


def find_path(grid):
    # Find S in the grid
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
    path = [(start[0], start[1])]
    current = start
    direction = PIPES[start_pipe][0]
    came_from = None
    print(direction)
    print(start_pipe)
    print(start)

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
            raise Exception('Invalidprint(x, y) pipe')
        if grid[current[0]][current[1]] not in PIPES:
            raise Exception('Invalid pipe')

        # Add the pipe to the path
        path.append((current[0], current[1]))

        # Change direction
        direction = PIPES[grid[current[0]][current[1]]][0]
        if direction == came_from:
            direction = PIPES[grid[current[0]][current[1]]][1]

    return path


def path_to_edges(path):
    edges = []
    direction = None
    for i, point in enumerate(path):
        if i == 0:
            edges.append([point, None])
            continue
        if i == 1:
            # find if the direction is on the x or y axis
            if point[0] == path[0][0]:
                direction = 'x'
            elif point[1] == path[0][1]:
                direction = 'y'
            else:
                raise Exception('Invalid path')
            continue

        current_direction = None
        if point[0] == path[i - 1][0]:
            current_direction = 'x'
        elif point[1] == path[i - 1][1]:
            current_direction = 'y'
        else:
            raise Exception('Invalid path')

        if current_direction != direction:
            if edges[-1][1] is None:
                edges[-1][1] = path[i - 1]
            edges.append([path[i - 1], None])
            direction = current_direction
    edges[-1][1] = path[-1]
    return edges


def is_inside(edges, xp, yp):
    cnt = 0
    for edge in edges:
        (x1, y1), (x2, y2) = edge
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            cnt += 1
    return cnt % 2 == 1


def points_inside(edges, grid, path):
    path = set(path)
    points = []
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if (i, j) in path:
                continue
            if is_inside(edges, i, j):
                points.append((i, j))
    return points


if __name__ == '__main__':
    GRID = input_parse()
    PATH = find_path(GRID)
    PATH.append(PATH[0])
    EDGES = path_to_edges(PATH)
    INSIDE = points_inside(EDGES, GRID, PATH)
    print(len(INSIDE))
    # Plot the path
    plt.figure(figsize=(10, 10))
    EDGES_POINTS = []

    for edge in EDGES:
        if edge[1] is None:
            EDGES_POINTS.append(edge[0])
        else:
            EDGES_POINTS.append(edge[0])
            EDGES_POINTS.append(edge[1])
    plt.plot([x[1] for x in EDGES_POINTS], [-x[0] for x in EDGES_POINTS], 'bo')
    plt.plot([x[1] for x in INSIDE], [-x[0] for x in INSIDE], 'go')
    plt.plot([PATH[0][1]], [-PATH[0][0]], 'ro')
    plt.plot([x[1] for x in PATH], [-x[0] for x in PATH])
    plt.show()
