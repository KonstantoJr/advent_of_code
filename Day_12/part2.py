def aStarAlgo(start_node, stop_node):
    global Graph_nodes
    open_set = set((start_node,))
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes
    # distance of starting node from itself is zero
    g[start_node] = 0
    # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        # node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # for each node m,compare its distance from start i.e g(m) to the
                # from start through n node
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n
                        # if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            # print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            # print('Path found: {}'.format(path))
            return path
        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)
    # print('Path does not exist!')
    return None

# define fuction to return neighbor and its distance
# from the passed node


def get_neighbors(v):
    global Graph_nodes
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def getDistance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def heuristic(n):
    global end
    x1, y1 = n
    x2, y2 = end
    return getDistance(x1, y1, x2, y2)


starts = []
with open('input.txt', 'r') as f:
    grid = []
    for i, line in enumerate(f):
        row = []
        for j, c in enumerate(line.strip()):
            if c == 'a':
                starts.append((i, j))
            if c == 'S':
                start = (i, j)
                starts.append((i, j))
                row.append('a')
                continue
            elif c == 'E':
                end = (i, j)
                row.append('z')
                continue
            row.append(c)
        grid.append(row)

# for i in grid:
#     print(i)

Graph_nodes = {}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        neighbors = []
        if i > 0:
            if ord(grid[i][j]) >= ord(grid[i-1][j]):
                neighbors.append(((i-1, j), 1))
            elif ord(grid[i][j]) + 1 == ord(grid[i-1][j]):
                neighbors.append(((i-1, j), 1))
        if i < len(grid)-1:
            if ord(grid[i][j]) >= ord(grid[i+1][j]):
                neighbors.append(((i+1, j), 1))
            elif ord(grid[i][j]) + 1 == ord(grid[i+1][j]):
                neighbors.append(((i+1, j), 1))
        if j > 0:
            if ord(grid[i][j]) >= ord(grid[i][j-1]):
                neighbors.append(((i, j-1), 1))
            elif ord(grid[i][j]) + 1 == ord(grid[i][j-1]):
                neighbors.append(((i, j-1), 1))
        if j < len(grid[0])-1:
            if ord(grid[i][j]) >= ord(grid[i][j+1]):
                neighbors.append(((i, j+1), 1))
            elif ord(grid[i][j]) + 1 == ord(grid[i][j+1]):
                neighbors.append(((i, j+1), 1))

        Graph_nodes[(i, j)] = neighbors

# for i in Graph_nodes:
#     print(i, Graph_nodes[i])
totalSteps = []
starts = sorted(starts, key=lambda x: heuristic(x))
print(starts)
for i, start in enumerate(starts):
    print(f'Progres {i} out of {len(starts)}')
    path = aStarAlgo(start, end)
    if path:
        totalSteps.append(len(path) - 1)


print(min(totalSteps))
