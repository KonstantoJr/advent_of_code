with open('input.txt', 'r') as f:
    elf = 0
    topelfs = []
    for line in f:
        if line != '\n':
            elf += int(line)
        else:
            topelfs.append(elf)
            elf = 0
    topelfs.sort()
print(topelfs[-1] + topelfs[-2] + topelfs[-3])
