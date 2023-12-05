"""Day 5 part 1"""

seeds = []
maps = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 0:
            seeds = line.split(':')[1].strip().split(' ')
            seeds = [int(x) for x in seeds]
        else:
            line = line.strip()
            if line == '':
                continue
            if "map" in line:
                maps.append({})
            else:
                #
                destination = int(line.split(' ')[0].strip())
                source = int(line.split(' ')[1].strip())
                range_ = int(line.split(' ')[2].strip())
                maps[-1][range((source), source + range_)
                         ] = destination - source

locations = []

for seed in seeds:
    for i, m in enumerate(maps):
        for key in m:
            if seed in key:
                seed += m[key]
                break
        else:
            continue
    locations.append(seed)

print(min(locations))
