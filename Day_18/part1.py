with open('input.txt', 'r') as f:
    data = f.read().splitlines()

cubeCoords = []
for line in data:
    x, y, z = line.split(',')
    cubeCoords.append((int(x), int(y), int(z)))


# find if 2 cubes are adjacent
def isAdjacent(cube1, cube2):
    x1, y1, z1 = cube1
    x2, y2, z2 = cube2
    if (x1 == x2 and y1 == y2 and abs(z1 - z2) == 1) or \
       (x1 == x2 and z1 == z2 and abs(y1 - y2) == 1) or \
       (y1 == y2 and z1 == z2 and abs(x1 - x2) == 1):
        return True
    return False


totalSides = len(cubeCoords) * 6
print(totalSides)
for i, cube1 in enumerate(cubeCoords):
    for cube2 in cubeCoords[i+1:]:
        if isAdjacent(cube1, cube2):
            totalSides -= 2
print(totalSides)
