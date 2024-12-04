
def find_mas(lines, x , y):
    # the x and y are the coordinates of the A
    # In order to check for the X-MAS, we need to check if the word mas creates an X in the grid
    # To do that we find the A and check if it is in the middle of 2 MAS
    first_mas = False
    second_mas = False

    if x - 1 >= 0 and y - 1 >= 0 and y + 1 < len(lines[0]) and x + 1 < len(lines):
        if (lines[x-1][y-1] == 'M' and lines[x+1][y+1]) == 'S' or (lines[x-1][y-1] == 'S' and lines[x+1][y+1] == 'M'):
            first_mas = True
        if (lines[x-1][y+1] == 'M' and lines[x+1][y-1]) == 'S' or (lines[x-1][y+1] == 'S' and lines[x+1][y-1] == 'M'):
            second_mas = True
    if first_mas and second_mas:
        return True
    
    return False





with open('input.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip()[::-1] for line in f]

found = set()
total = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'A':
            if find_mas(lines, i, j):
                found.add((i,j))
                total +=1

# for i in range(len(lines)):
#     for j in range(len(lines[i])):
#         if (i,j) in found:
#             print('A', end='')
#         else:
#             print('.', end='')
#     print()


print(total)

