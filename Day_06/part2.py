with open('input.txt', 'r') as f:
    chars = []
    for line in f:
        for i, char in enumerate(line):
            if i < 14:
                chars.append(char)
            else:
                if len(set(chars)) == 14:
                    print(i)
                    break
                chars.pop(0)
                chars.append(char)
