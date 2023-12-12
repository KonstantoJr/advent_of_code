"""Day 12 part 2"""

from functools import cache


def input_parse():
    """Parse input file"""
    with open("input.txt", 'r', encoding='utf-8') as file:
        return [line.strip().split() for line in file]


@cache
def find_arrangement(arrangement: str, groups: tuple[int], condition: int = 0):
    """Find arrangement"""
    if not arrangement:
        # if the arrangement is empty, we probably found a valid one
        # if there are still groups left, it's not valid
        # if there are still conditions left, it means the current group
        # is not satisfied
        return not groups and not condition
    n = 0
    if arrangement[0] in ('#', '?'):
        n += find_arrangement(arrangement[1:], groups, condition + 1)
    if arrangement[0] in ('.', '?') and (groups and groups[0] == condition or not condition):
        n += find_arrangement(arrangement[1:],
                              groups[1:] if condition else groups)
    return n


def main():
    """Main"""
    data = input_parse()

    data = [(pipes, tuple(int(n) for n in groups.split(",")))
            for pipes, groups in data]

    total = 0
    for i, d in enumerate(data):
        print(f'Processing {i+1}/ {len(data)}')
        total += find_arrangement("?".join([d[0]] * 5) + '.', d[1] * 5)
    print(total)


if __name__ == "__main__":
    main()
