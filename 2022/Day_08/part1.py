with open('input.txt', 'r') as f:
    grid = []
    for line in f:
        grid.append([])
        line = line.strip()
        for tree in line:
            grid[-1].append(int(tree))

# print(len(grid))
# print(len(grid[0]))
visibleOutside = (len(grid)*len(grid[0])) - \
    ((len(grid) - 2)*(len(grid[0]) - 2))
# print(visibleOutside)
visible = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
            continue
        currentHeight = grid[i][j]
        for k in range(i):
            if grid[k][j] >= currentHeight:
                break
        else:
            visible += 1
            continue
        for k in range(i + 1, len(grid)):
            if grid[k][j] >= currentHeight:
                break
        else:
            visible += 1
            continue
        for k in range(j):
            if grid[i][k] >= currentHeight:
                break
        else:
            visible += 1
            continue
        for k in range(j + 1, len(grid[0])):
            if grid[i][k] >= currentHeight:
                break
        else:
            visible += 1
            continue

print(visibleOutside + visible)
print(visible)

# for i in grid:
#     for j in i:
#         print(j, end='')
#     print()
