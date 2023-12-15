"""Day 15 part 1"""


def input_parse():
    """Parse input into list of ints"""
    steps = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            steps.extend(line.strip().split(','))
    return steps


def hash_step(step: str):
    """Hash a step"""
    c_value = 0
    for char in step:
        c_value += ord(char)
        c_value *= 17
        c_value = c_value % 256
    return c_value


def main():

    steps = input_parse()
    total = 0
    for step in steps:
        total += hash_step(step)
    print(total)


if __name__ == "__main__":
    main()
