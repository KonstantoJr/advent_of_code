

with open('input.txt', 'r') as f:
    cycle = 0
    X = 1
    importantCycles = [20, 60, 100, 140, 180, 220]
    signalStrength = []
    for line in f:
        line = line.strip()
        if line == 'noop':
            cycle += 1
            if cycle in importantCycles:
                signalStrength.append(X * cycle)
            continue
        command, value = line.split()
        value = int(value)
        for i in range(2):
            if i == 0:
                cycle += 1
                if cycle in importantCycles:
                    signalStrength.append(X * cycle)
            else:
                cycle += 1
                if cycle in importantCycles:
                    signalStrength.append(X * cycle)
                X += value
    print(sum(signalStrength))
