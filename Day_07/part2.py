from collections import defaultdict

with open('input.txt', 'r') as f:
    currentDir = []
    structure = defaultdict(int)
    for line in f:
        if line[0] == '$':
            command = line.strip().split(" ")
            if command[1] == 'cd':
                if command[2] == '..':
                    currentDir.pop()
                else:
                    currentDir.append(command[2])
            elif command[1] == 'ls':
                continue
        else:
            if 'dir' in line:
                continue
            size, file = line.strip().split(" ")
            size = int(size)
            for i, dir in enumerate(currentDir):
                structure["".join(currentDir[:i]) + dir] += size

disk = 70000000
free = 30000000
total = structure['/']
need = total - (disk - free)

dirTodelete = 1e9
for dir in structure:
    if structure[dir] >= need:
        dirTodelete = min(dirTodelete, structure[dir])
print(dirTodelete)
