with open('input.txt', 'r') as f:
    data = f.read().splitlines()

cubeCoords = set()
for line in data:
    x, y, z = line.split(',')
    cubeCoords.add((int(x), int(y), int(z)))


# return the neighbors of a cube
def getNeighbors(cube):
    x, y, z = cube
    return [
        (x+1, y, z), (x-1, y, z),
        (x, y+1, z), (x, y-1, z),
        (x, y, z+1), (x, y, z-1)
    ]


xmin, *_, xmax = sorted(cubeCoords, key=lambda x: x[0])
ymin, *_, ymax = sorted(cubeCoords, key=lambda x: x[1])
zmin, *_, zmax = sorted(cubeCoords, key=lambda x: x[2])

outside = set([
    (xmin[0] - 1, ymin[1]-1, zmin[2]-1),
    (xmax[0] + 1, ymax[1]+1, zmax[2]+1),
])

while True:
    inside = set()
    for cube in outside:
        for neighbor in getNeighbors(cube):
            x, y, z = neighbor
            if neighbor not in cubeCoords:
                if xmin[0] - 1 <= x <= xmax[0] + 1 and \
                   ymin[1] - 1 <= y <= ymax[1] + 1 and \
                   zmin[2] - 1 <= z <= zmax[2] + 1:
                    inside.add(neighbor)

    if all([cube in outside for cube in inside]):
        break
    outside |= inside

totalsurfaces = 0
for cube in cubeCoords:
    for cube1 in getNeighbors(cube):
        if cube1 in outside:
            totalsurfaces += 1
print(totalsurfaces)
