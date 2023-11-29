with open('input.txt', 'r') as f:
    points = {'X': 1, 'Y': 2, 'Z': 3}
    win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    totalScore = 0
    for line in f:
        elf, me = line.split()
        if win[me] == elf:
            totalScore += points[me] + 6
        elif draw[me] == elf:
            totalScore += points[me] + 3
        else:
            totalScore += points[me]
    print(totalScore)
