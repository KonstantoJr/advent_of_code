with open('input.txt', 'r') as f:
    win = {'C': 1, 'B': 3, 'A': 2}
    draw = {'A': 1, 'C': 3, 'B': 2}
    lose = {'B': 1, 'A': 3, 'C': 2}
    totalScore = 0
    for line in f:
        elf, me = line.split()
        if me == "X":
            totalScore += lose[elf]
        elif me == "Y":
            totalScore += draw[elf] + 3
        else:
            totalScore += win[elf] + 6
    print(totalScore)
