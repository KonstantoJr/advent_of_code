"""Day 4 part 1"""

cards = []
TOTAL = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(':')[1].strip()
        winning = line.split('|')[0].strip().split(" ")
        my = line.split('|')[1].strip().split(" ")
        points = 0
        for win in winning:
            if win == '':
                continue
            times = my.count(win)
            if points == 0 and times > 0:
                points = 1
                times = times - 1
            for i in range(times):
                points *= 2
        print(points)
        TOTAL += points

print(TOTAL)
