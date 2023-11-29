def isInRange(x, y, sensors):
    for (x1, y1, d) in sensors:
        distance = abs(x - x1) + abs(y - y1)
        if distance <= d:
            return False
    return True


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

sensors = set()
beacons = set()
for i in data:
    sensor, value = i.split(':')
    x1, y1 = sensor.split(',')
    x1 = int(x1.split('=')[1])
    y1 = int(y1.split('=')[1])
    x2, y2 = value.split(',')
    x2 = int(x2.split('=')[1])
    y2 = int(y2.split('=')[1])
    d = abs(x1-x2) + abs(y1-y2)
    sensors.add((x1, y1, d))
    beacons.add((x2, y2))

checked = 0
for (sx, sy, d) in sensors:
    for dx in range(d+2):
        dy = (d+1) - dx

        for bx, by in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            checked += 1
            x = sx + (dx * bx)
            y = sy + (dy * by)
            if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                continue
            if isInRange(x, y, sensors):
                print(x*4_000_000 + y)
                exit()
