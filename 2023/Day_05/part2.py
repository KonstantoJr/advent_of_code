"""Day 5 part 2"""


def parse_input():
    """Parse input.txt"""
    seeds = []
    maps = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == 0:
                seeds = line.split(':')[1].strip().split(' ')
                seeds = [int(x) for x in seeds]
            else:
                line = line.strip()
                if line == '':
                    continue
                if "map" in line:
                    maps.append([])
                else:
                    #
                    destination = int(line.split(' ')[0].strip())
                    source = int(line.split(' ')[1].strip())
                    length = int(line.split(' ')[2].strip())
                    maps[-1].append([[source, source + length - 1],
                                    [destination, destination + length - 1]])

    for i, m in enumerate(maps):
        maps[i] = sorted(m)
    return seeds, maps


def location_to_seed(maps, loc):
    """Convert location to seed"""
    for m in maps[::-1]:
        for (source, destination) in m:
            if destination[0] <= loc <= destination[1]:
                loc = loc-destination[0] + source[0]
                break
    return loc


def seed_in_ranges(ranges, seed):
    """Check if seed is in ranges"""
    for r in ranges:
        if seed in r:
            return True
    return False


def seeds_to_ranges(seeds):
    """Convert seeds to ranges"""
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))
    return ranges


def solution(seed_ranges, maps):
    """Find solution"""
    for loc in range(1_000_000_000):
        if loc % 1_000_000 == 0:
            print(loc)
        seed = location_to_seed(maps, loc)
        if seed_in_ranges(seed_ranges, seed):
            print('Solution:', loc)
            break


if __name__ == '__main__':
    SEEDS, MAPS = parse_input()
    SEED_RANGES = seeds_to_ranges(SEEDS)
    solution(SEED_RANGES, MAPS)
