with open('input.txt', 'r') as f:
    elf = 0
    topelf = 0
    for line in f:
        if line != '\n':
            elf += int(line)
        else:
            topelf = max(elf, topelf)
            elf = 0
print(topelf)
