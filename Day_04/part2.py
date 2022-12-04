with open("input.txt", 'r') as f:
    pairs = 0
    for line in f:
        pair1, pair2 = line.split(',')
        start1, end1 = pair1.split('-')
        start2, end2 = pair2.split('-')
        sub1 = set(range(int(start1), int(end1) + 1))
        sub2 = set(range(int(start2), int(end2) + 1))
        if sub1.intersection(sub2) != set():
            pairs += 1
    print(pairs)
