"""Day 17 part 1"""
from collections import defaultdict
from heapq import heappop, heappush


def djikstra(grid, start):
    """Djikstra's algorithm"""
    queue = [(0, start, (0, 0), 1)]
    distances = {
        (i, j): defaultdict(lambda: float("inf")) for i, row in enumerate(grid) for j, _ in enumerate(row)
    }
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        heatloss, (posx, posy), (drx, dry), steps = heappop(queue)
        for dx, dy in directions:
            new_steps = None
            if (dx, dy) == (-drx, -dry):
                new_steps = None
            if steps >= 4 or (drx, dry) == (0, 0):
                new_steps = 1
            if (dx, dy) == (drx, dry):
                new_steps = steps + 1
            if not new_steps or new_steps == 11:
                continue
            new_posx, new_posy = posx + dx, posy + dy
            if 0 <= new_posx < len(grid) and 0 <= new_posy < len(grid[0]):
                new_heat_loss = heatloss + grid[new_posx][new_posy]
                if new_heat_loss < distances[(new_posx, new_posy)][(dx, dy, new_steps)]:
                    distances[(new_posx, new_posy)][(
                        dx, dy, new_steps)] = new_heat_loss
                    heappush(
                        queue, (new_heat_loss, (new_posx, new_posy), (dx, dy), new_steps))
    return distances


def input_parse(filename):
    """Parse input"""
    with open(filename, "r", encoding="utf-8") as file:
        return tuple(tuple(int(char) for char in line.strip()) for line in file)


def main():
    """Main"""
    grid = input_parse("input.txt")
    distances = djikstra(grid, (0, 0))

    print(min(heat_loss for (_, _, steps), heat_loss in distances[(
        len(grid) - 1, len(grid[0]) - 1)].items() if steps >= 4) + 1)


if __name__ == "__main__":
    main()
