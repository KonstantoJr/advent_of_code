
with open('input.txt', 'r') as f:
    grid = []
    for line in f:
        grid.append([])
        line = line.strip()
        for tree in line:
            grid[-1].append(int(tree))

viewingDistace = {}
scenincScore = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        scenincScore[(i, j)] = 1
        viewingDistace[(i, j)] = [0, 0, 0, 0]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
            continue
        currentHeight = grid[i][j]
        for k in range(i-1, -1, -1):
            viewingDistace[(i, j)][0] += 1
            if grid[k][j] >= currentHeight:
                break
        for k in range(i + 1, len(grid)):
            viewingDistace[(i, j)][1] += 1
            if grid[k][j] >= currentHeight:
                break
        for k in range(j - 1, -1, -1):
            viewingDistace[(i, j)][2] += 1
            if grid[i][k] >= currentHeight:
                break
        for k in range(j + 1, len(grid[0])):
            viewingDistace[(i, j)][3] += 1
            if grid[i][k] >= currentHeight:
                break


for i in viewingDistace:
    for j in range(4):
        if viewingDistace[i][j] == 0:
            continue
        scenincScore[i] *= viewingDistace[i][j]

print(max(scenincScore.items(), key=lambda x: x[1]))
