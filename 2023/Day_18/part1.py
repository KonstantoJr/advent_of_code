"""Day 18 part 1"""


def input_parse(filename):
    """Parse the input"""
    with open(filename, 'r', encoding='utf-8') as file:
        return tuple(tuple((direction, int(distance), color)) for
                     direction, distance, color in (line.strip().split(" ") for line in file))


def dig(instructions):
    """Dig"""
    start = (0, 0)
    points = set()
    points.add(start)
    current = list(start)
    for direction, distance, _ in instructions:
        if direction == "R":
            for _ in range(distance):
                current[0] += 1
                points.add(tuple(current))
        elif direction == "L":
            for _ in range(distance):
                current[0] -= 1
                points.add(tuple(current))
        elif direction == "U":
            for _ in range(distance):
                current[1] += 1
                points.add(tuple(current))
        elif direction == "D":
            for _ in range(distance):
                current[1] -= 1
                points.add(tuple(current))
    return points


def main():
    """Main"""
    instructions = input_parse("example.txt")
    points = dig(instructions)


if __name__ == '__main__':
    main()
