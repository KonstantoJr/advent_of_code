"""Day 11 part 2"""
from itertools import combinations
DISTANCE = 999_999


def input_parse():
    with open("input.txt", "r", encoding='utf-8') as f:
        return [list(line.strip()) for line in f.readlines()]


def update_galaxies(grid: list[list[str]]):
    empty_rows = 0
    galaxies = {}
    for i, row in enumerate(grid):
        if '#' not in row:
            empty_rows += 1
        else:
            for j, col in enumerate(row):
                if col == '#':
                    galaxies[(i, j)] = (i + (empty_rows * DISTANCE), j)

    empty_cols = 0
    for i, _ in enumerate(grid[0]):
        col = [row[i] for row in grid]
        if '#' not in col:
            empty_cols += 1
        else:
            for j, _ in enumerate(grid):
                if grid[j][i] == '#':
                    galaxies[(j, i)] = (galaxies[(j, i)][0],
                                        i + (empty_cols * DISTANCE))
    return galaxies


def galaxy_pairs(galaxies: dict[tuple[int, int], tuple[int, int]]):
    return set(combinations(galaxies.values(), 2))


def find_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def part2(pairs):
    total = 0
    for i, j in pairs:
        total += find_distance(i, j)
    return total


def main():
    grid = input_parse()
    galaxies = update_galaxies(grid)
    pairs = galaxy_pairs(galaxies)
    print(part2(pairs))


if __name__ == "__main__":
    main()
