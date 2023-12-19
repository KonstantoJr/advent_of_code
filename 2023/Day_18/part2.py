"""Day 18 part 2"""


def input_parse(filename):
    """Parse the input"""
    with open(filename, 'r', encoding='utf-8') as file:
        return tuple(tuple((direction, int(distance), color)) for
                     direction, distance, color in (line.strip().split(" ") for line in file))


def color_to_distance_and_direction(color):
    color = color.replace("#", "")
    color = color.replace("(", "")
    color = color.replace(")", "")
    # The first 5 digits are the distance in meters as a hex number
    distance = int(color[:5], 16)
    # The last digits is the direction 0-3
    direction = int(color[5:])
    if direction == 0:
        direction = "R"
    elif direction == 1:
        direction = "D"
    elif direction == 2:
        direction = "L"
    elif direction == 3:
        direction = "U"

    return distance, direction


def dig(instructions):
    """Dig"""
    start = (0, 0)
    points = 0
    edges = []
    edges.append(start)
    current = list(start)
    for _, _, color in instructions:
        distance, direction = color_to_distance_and_direction(color)
        if direction == "R":
            points += distance
            current = (current[0] + distance, current[1])
            edges.append(current)
        elif direction == "L":
            points += distance
            current = (current[0] - distance, current[1])
            edges.append(current)
        elif direction == "U":
            points += distance
            current = (current[0], current[1] + distance)
            edges.append(current)
        elif direction == "D":
            points += distance
            current = (current[0], current[1] - distance)
            edges.append(current)
    return points, edges


def shoe_lace(points):
    """Shoe lace"""
    total = 0
    for i in range(len(points) - 1):
        total += points[i][0] * points[i+1][1] - points[i][1] * points[i+1][0]
    total += points[-1][0] * points[0][1] - points[-1][1] * points[0][0]
    return abs(total) / 2


def main():
    """Main"""
    instructions = input_parse("input.txt")
    points, edges = dig(instructions)

    total = points // 2 + shoe_lace(edges) + 1
    print(int(total))


if __name__ == '__main__':
    main()
