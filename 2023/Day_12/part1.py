"""Day 12 part1 """

from itertools import product


def input_parse():
    """Parse input file"""
    with open("input.txt", 'r', encoding='utf-8') as file:
        return [line.strip().split() for line in file]


def find_arrangement(data: list[str, str]):
    """Find arrangement"""

    arrangement = data[0]
    condition = data[1]

    unknown = arrangement.count('?')
    total = 0
    if unknown == 0:
        return 0
    possible = list(product(['.', '#'], repeat=unknown))

    for p in possible:
        new_arrangement = arrangement
        for i in range(unknown):
            new_arrangement = new_arrangement.replace('?', p[i], 1)
        if check_valid(new_arrangement, condition):
            total += 1
    return total


def check_valid(arrangement: str, condition: str):
    """Check if arrangement is valid"""
    groups = condition.split(',')
    cur_arr = arrangement.split('.')
    group_p = 0
    arr_p = 0
    while group_p < len(groups):
        if arr_p >= len(cur_arr):
            return False
        if cur_arr[arr_p] == "":
            arr_p += 1
            continue
        tags = cur_arr[arr_p].count('#')
        if tags == int(groups[group_p]):
            group_p += 1
            arr_p += 1
        else:
            return False

    while arr_p < len(cur_arr):
        if cur_arr[arr_p] != "":
            return False
        arr_p += 1

    return True


def main():
    """Main"""
    data = input_parse()
    total = 0
    for i, d in enumerate(data):
        print(f'Processing {i+1}/ {len(data)}')
        total += find_arrangement(d)
    print(total)


if __name__ == "__main__":
    main()
