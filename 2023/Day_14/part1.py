"""Day 14 part 1"""


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


def calculate_score(grid):
    """ For each rock, add the number of rows it is from the bottom"""
    score = 0
    for y, row in enumerate(grid):
        for _, col in enumerate(row):
            if col == 'O':
                score += len(grid) - y

    return score


def main():
    grid = input_parse()

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == 'O':
                move_rock_north(grid, x, y)

    print(calculate_score(grid))


if __name__ == "__main__":
    main()
