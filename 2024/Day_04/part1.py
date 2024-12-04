
def find_xmas(lines, x , y, found):
    # when we find an X we need to check all the ways that 
    # the word xmas can appear in the grid
    # x , y are the coordinates of the X
    total = 0
    # check horizontal
    if y + 3 < len(lines[0]):
        if lines[x][y+1] == 'M' and lines[x][y+2] == 'A' and lines[x][y+3] == 'S':
            found.add((x,y))
            found.add((x, y+1))
            found.add((x, y+2))
            found.add((x, y+3))
            total += 1
    # check vertical
    if x + 3 < len(lines):
        if lines[x+1][y] == 'M' and lines[x+2][y] == 'A' and lines[x+3][y] == 'S':
            found.add((x,y))
            found.add((x+1, y))
            found.add((x+2, y))
            found.add((x+3, y))
            total += 1
    # check diagonal
    if x + 3 < len(lines) and y + 3 < len(lines[0]):
        if lines[x+1][y+1] == 'M' and lines[x+2][y+2] == 'A' and lines[x+3][y+3] == 'S':
            found.add((x,y))
            found.add((x+1, y+1))
            found.add((x+2, y+2))
            found.add((x+3, y+3))
            total += 1
    # check other diagonal
    if x + 3 < len(lines) and y - 3 >= 0:
        if lines[x+1][y-1] == 'M' and lines[x+2][y-2] == 'A' and lines[x+3][y-3] == 'S':
            found.add((x,y))
            found.add((x+1, y-1))
            found.add((x+2, y-2))
            found.add((x+3, y-3))
            total += 1
    # check other vertical
    if x - 3 >= 0:
        if lines[x-1][y] == 'M' and lines[x-2][y] == 'A' and lines[x-3][y] == 'S':
            found.add((x,y))
            found.add((x-1, y))
            found.add((x-2, y))
            found.add((x-3, y))
            total += 1
    # check other horizontal
    if y - 3 >= 0:
        if lines[x][y-1] == 'M' and lines[x][y-2] == 'A' and lines[x][y-3] == 'S':
            found.add((x,y))
            found.add((x, y-1))
            found.add((x, y-2))
            found.add((x, y-3))
            total += 1
    # check up right diagonal
    if x - 3 >= 0 and y + 3 < len(lines[0]):
        if lines[x-1][y+1] == 'M' and lines[x-2][y+2] == 'A' and lines[x-3][y+3] == 'S':
            found.add((x,y))
            found.add((x-1, y+1))
            found.add((x-2, y+2))
            found.add((x-3, y+3))
            total += 1
    # check up left diagonal
    if x - 3 >= 0 and y - 3 >= 0:
        if lines[x-1][y-1] == 'M' and lines[x-2][y-2] == 'A' and lines[x-3][y-3] == 'S':
            found.add((x,y))
            found.add((x-1, y-1))
            found.add((x-2, y-2))
            found.add((x-3, y-3))
            total += 1
    
    return total





with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()


total = 0
found = set()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            total += find_xmas(lines, i, j, found)
            
print(total)

# for i in range(len(lines)):
#     for j in range(len(lines[i])):
#         if (i, j) in found:
#             print(lines[i][j], end='')
#         else:
#             print('.', end='')
#     print()