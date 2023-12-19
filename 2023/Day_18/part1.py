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
    edges = []
    points.add(start)
    edges.append(start)
    current = list(start)
    for direction, distance, _ in instructions:
        if direction == "R":
            for i in range(distance):
                current[0] += 1
                if i == distance - 1:
                    edges.append(tuple(current))
                points.add(tuple(current))
        elif direction == "L":
            for i in range(distance):
                current[0] -= 1
                if i == distance - 1:
                    edges.append(tuple(current))
                points.add(tuple(current))
        elif direction == "U":
            for i in range(distance):
                current[1] += 1
                if i == distance - 1:
                    edges.append(tuple(current))
                points.add(tuple(current))
        elif direction == "D":
            for i in range(distance):
                current[1] -= 1
                if i == distance - 1:
                    edges.append(tuple(current))
                points.add(tuple(current))
    return points, edges


def find_grid_size(points):
    """Find the grid size"""
    x_min = min(points, key=lambda x: x[0])[0]
    x_max = max(points, key=lambda x: x[0])[0]
    y_min = min(points, key=lambda x: x[1])[1]
    y_max = max(points, key=lambda x: x[1])[1]
    return x_min, x_max, y_min, y_max


def is_inside(edges, xp, yp):
    cnt = 0
    for edge in edges:
        (x1, y1), (x2, y2) = edge
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            cnt += 1
    return cnt % 2 == 1


def points_inside(edges, path, x_min, x_max, y_min, y_max):
    path = set(path)
    points = []
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            print(f"Progress {i}/{x_max} {j}/{y_max}")
            if (i, j) in path:
                continue
            if is_inside(edges, i, j):
                points.append((i, j))
    return points


def edges_to_pairs(edges):
    pairs = []
    for i in range(len(edges) - 1):
        pairs.append((edges[i], edges[i+1]))
    return pairs


def main():
    """Main"""
    instructions = input_parse("input.txt")
    points, edges = dig(instructions)
    edges = edges_to_pairs(edges)
    for edge in edges:
        print(edge)
    total = len(points)
    x_min, x_max, y_min, y_max = find_grid_size(points)
    print(x_min, x_max, y_min, y_max)
    inside = points_inside(edges,  points, x_min, x_max, y_min, y_max)
    total += len(inside)

    print(total)


if __name__ == '__main__':
    main()
