"""Day 11 part 1"""
from itertools import combinations


def input_parse():
    with open("input.txt", "r", encoding='utf-8') as f:
        return [list(line.strip()) for line in f.readlines()]


def add_row(grid):
    new_grid = []
    for _, row in enumerate(grid):
        new_grid.append(row)
        if '#' not in row:
            new_grid.append(row)
    return new_grid


def add_column(grid):
    new_grid = [[] for _ in range(len(grid))]
    for i, _ in enumerate(grid[0]):
        col = [row[i] for row in grid]
        if '#' not in col:
            for j, _ in enumerate(grid):
                new_grid[j].append(grid[j][i])
                new_grid[j].append(grid[j][i])
        else:
            for j, _ in enumerate(grid):
                new_grid[j].append(grid[j][i])
    return new_grid


def find_galaxies(grid):
    galaxies = set()
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '#':
                galaxies.add((i, j))
    return galaxies


def galaxy_pairs(galaxies: set[tuple[int, int]]):
    return set(combinations(galaxies, 2))


def find_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def part1(pairs):
    total = 0
    for i, j in pairs:
        total += find_distance(i, j)
    return total


def main():
    grid = input_parse()
    grid = add_row(grid)
    grid = add_column(grid)
    galaxies = find_galaxies(grid)
    pairs = galaxy_pairs(galaxies)
    print(part1(pairs))


if __name__ == "__main__":
    main()
