"""Solution for Day 1."""

from collections import defaultdict


def left_list(data):
    left = []
    for i in data:
        num = ""
        for s in i:
            if s == ' ':
                break
            num += s
        left.append(int(num))
    return left


def right_list(data):
    right = []
    for i in data:
        num = ""
        for s in i[::-1]:
            if s == ' ':
                break
            num += s
        right.append(int(num[::-1]))
    return right


def part_1(data):
    left = left_list(data)
    right = right_list(data)
    left.sort()
    right.sort()
    solution = 0
    for i, _ in enumerate(left):
        solution += abs(left[i] - right[i])
    return solution


def part2(data):
    left = left_list(data)
    right = right_list(data)

    counter = defaultdict(int)
    for i in right:
        counter[i] += 1

    solution = 0

    for i in left:
        if i not in counter:
            continue
        solution += i * counter[i]
    return solution


with open('input.txt', 'r', encoding='UTF-8') as f:
    data = f.read().splitlines()


print(part_1(data))
print(part2(data))
