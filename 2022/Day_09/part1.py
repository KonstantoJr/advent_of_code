def checkAdj(headPos, tailPos):
    # check if head and tail are adjacent
    if (headPos[0] == tailPos[0] and abs(headPos[1] - tailPos[1]) == 1) or (headPos[1] == tailPos[1] and abs(headPos[0] - tailPos[0]) == 1):
        return True
    # check if head and tail are diagonal
    elif abs(headPos[0] - tailPos[0]) == 1 and abs(headPos[1] - tailPos[1]) == 1:
        return True
    else:
        return False


def moveTail(headPos, tailPos):
    # move tail to head diagonaly so that head and tail are adjacent
    # if head and tail are on the same position do nothing
    if headPos == tailPos:
        pass
    # if they are on the same column or row move horizontally or vertically
    elif headPos[0] == tailPos[0]:
        if headPos[1] > tailPos[1]:
            tailPos[1] += 1
        else:
            tailPos[1] -= 1
    elif headPos[1] == tailPos[1]:
        if headPos[0] > tailPos[0]:
            tailPos[0] += 1
        else:
            tailPos[0] -= 1
    # if they are on different columns and rows move diagonally
    else:
        if headPos[0] > tailPos[0] and headPos[1] > tailPos[1]:
            tailPos[0] += 1
            tailPos[1] += 1
        elif headPos[0] > tailPos[0] and headPos[1] < tailPos[1]:
            tailPos[0] += 1
            tailPos[1] -= 1
        elif headPos[0] < tailPos[0] and headPos[1] > tailPos[1]:
            tailPos[0] -= 1
            tailPos[1] += 1
        elif headPos[0] < tailPos[0] and headPos[1] < tailPos[1]:
            tailPos[0] -= 1
            tailPos[1] -= 1
    return tailPos


with open('input.txt', 'r') as f:
    headPos = [0, 0]
    tailPos = [0, 0]
    tailsTotal = [(0, 0)]
    for line in f:
        direction, steps = line.strip().split()
        steps = int(steps)
        if direction == 'R':
            for i in range(steps):
                headPos[1] += 1
                if checkAdj(headPos, tailPos):
                    continue
                else:
                    tailPos = moveTail(headPos, tailPos)
                    tailsTotal.append((tailPos[0], tailPos[1]))
        elif direction == 'L':
            for i in range(steps):
                headPos[1] -= 1
                if checkAdj(headPos, tailPos):
                    continue
                else:
                    tailPos = moveTail(headPos, tailPos)
                    tailsTotal.append((tailPos[0], tailPos[1]))
        elif direction == 'U':
            for i in range(steps):
                headPos[0] += 1
                if checkAdj(headPos, tailPos):
                    continue
                else:
                    tailPos = moveTail(headPos, tailPos)
                    tailsTotal.append((tailPos[0], tailPos[1]))
        elif direction == 'D':
            for i in range(steps):
                headPos[0] -= 1
                if checkAdj(headPos, tailPos):
                    continue
                else:
                    tailPos = moveTail(headPos, tailPos)
                    tailsTotal.append((tailPos[0], tailPos[1]))
    # print(len(tailsTotal))
    # for i in tailsTotal:
    #     print(i)
    print(len(set(tailsTotal)))
