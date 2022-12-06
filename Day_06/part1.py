with open('input.txt', 'r') as f:
    chars = set()
    for line in f:
        for i, char in enumerate(line):
            if (i+1) % 4 == 0:
                chars.add(char)
                if len(chars) == 4:
                    print(i+1)
                    break
                chars = set()
            else:
                chars.add(char)
