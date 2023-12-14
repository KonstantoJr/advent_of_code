"""Day 14 part 2"""


def input_parse():
    """Parse input into list of tuples"""
    with open("input.txt", "r", encoding='utf-8') as f:
        return [list(line.strip()) for line in f.readlines()]


def move_rock_north(grid, x, y):
    """Move rock north"""
    cur_x = x
    cur_y = y
    while cur_y > 0 and grid[cur_y - 1][cur_x] == '.':
        cur_y -= 1

    if cur_x == x and cur_y == y:
        return

    grid[cur_y][cur_x] = 'O'
    grid[y][x] = '.'


def move_rock_south(grid, x, y):
    """Move rock south"""
    cur_x = x
    cur_y = y
    while cur_y < len(grid) - 1 and grid[cur_y + 1][cur_x] == '.':
        cur_y += 1

    if cur_x == x and cur_y == y:
        return

    grid[cur_y][cur_x] = 'O'
    grid[y][x] = '.'


def move_rock_east(grid, x, y):
    """Move rock east"""
    cur_x = x
    cur_y = y
    while cur_x < len(grid[0]) - 1 and grid[cur_y][cur_x + 1] == '.':
        cur_x += 1

    if cur_x == x and cur_y == y:
        return

    grid[cur_y][cur_x] = 'O'
    grid[y][x] = '.'


def move_rock_west(grid, x, y):
    """Move rock west"""
    cur_x = x
    cur_y = y
    while cur_x > 0 and grid[cur_y][cur_x - 1] == '.':
        cur_x -= 1

    if cur_x == x and cur_y == y:
        return

    grid[cur_y][cur_x] = 'O'
    grid[y][x] = '.'


def calculate_score(grid):
    """ For each rock, add the number of rows it is from the bottom"""
    score = 0
    for y, row in enumerate(grid):
        for _, col in enumerate(row):
            if col == 'O':
                score += len(grid) - y

    return score


def cycle(grid):

    c = [move_rock_north, move_rock_west, move_rock_south, move_rock_east]

    for i, direction in enumerate(c):
        if i in (0, 1):
            for y, row in enumerate(grid):
                for x, col in enumerate(row):
                    if col == 'O':
                        direction(grid, x, y)
        if i in (2, 3):
            for y in range(len(grid) - 1, -1, -1):
                for x in range(len(grid[0]) - 1, -1, -1):
                    if grid[y][x] == 'O':
                        direction(grid, x, y)


def main():
    grid = input_parse()
    cycles = 1_000_000_000

    total = {}

    for i in range(cycles):
        print(f'Cycle {i+1} / {cycles}')
        cycle(grid)
        grid_copy = tuple(tuple(row) for row in grid)
        if grid_copy in total:
            print(f'Found cycle at {i}')
            # we found a cycle
            cycle_length = i - total[grid_copy]
            # skip ahead
            remaining = cycles - i - 1
            skip = remaining % cycle_length
            print(f'Skipping {remaining} cycles')
            print(f'Cycle length {cycle_length}')
            print(f'Remaining {remaining}')
            print(f'Cycles to reach {cycles} state is {skip}')
            for _ in range(skip):
                cycle(grid)

            break
        total[grid_copy] = i

    print(calculate_score(grid))


if __name__ == "__main__":
    main()
