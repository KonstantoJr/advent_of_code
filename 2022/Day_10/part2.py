def drawPixel(pixels, X, pos):
    if pos == 0:
        pos = 40
    if pos == 1:
        pixels.append([])
    pos -= 1
    if pos in (X-1, X, X+1):
        pixels[-1].append('#')
    else:
        pixels[-1].append('.')
    return pixels


with open('input.txt', 'r') as f:
    cycle = 1
    X = 1
    pixels = []
    temp = []
    # importantCycles = [40, 80, 120, 160, 200, 240]
    for line in f:
        line = line.strip()
        pos = (cycle) % 40
        if line == 'noop':
            pixels = drawPixel(pixels, X, pos)
            cycle += 1
            temp.append((X, pos))
            continue

        command, value = line.split()
        value = int(value)
        for i in range(2):
            pos = (cycle) % 40
            if i == 0:
                pixels = drawPixel(pixels, X, pos)
                temp.append((X, pos))
            else:
                pixels = drawPixel(pixels, X, pos)
                X += value
                temp.append((X, pos))
            cycle += 1

    print(temp)
    for i in pixels:
        print(''.join(i))
