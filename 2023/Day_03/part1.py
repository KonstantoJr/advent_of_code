"""Day 3 part 1"""

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
numbers = {
}
engine = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        NUM = ""
        coords = []
        for j, char in enumerate(line):
            if char != '.' and char in digits:
                NUM += char
                coords.append((i, j))
            elif NUM != '' and (char not in digits or j == len(line) - 1):
                for coord in coords:
                    numbers[coord] = int(NUM)
                NUM = ""
                coords = []
        engine.append(line.strip())

TOTAL = 0
for i, row in enumerate(engine):
    for j, col in enumerate(row):
        if col != '.' and col not in digits:
            print(col)
            # check above row of numbers
            if (i - 1, j) in numbers:
                TOTAL += numbers[(i - 1, j)]
            if (i-1, j-1) in numbers and numbers[(i-1, j-1)] != numbers.get((i-1, j), None):
                TOTAL += numbers[(i - 1, j - 1)]
            if (i-1, j+1) in numbers and numbers[(i-1, j+1)] != numbers.get((i-1, j), None) \
                    and numbers[(i-1, j+1)] != numbers.get((i-1, j-1), None):
                TOTAL += numbers[(i - 1, j + 1)]
            # check left and right
            if (i, j-1) in numbers:
                TOTAL += numbers[(i, j-1)]
            if (i, j+1) in numbers:
                TOTAL += numbers[(i, j+1)]
            # check below row of numbers
            if (i+1, j) in numbers:
                TOTAL += numbers[(i+1, j)]
            if (i+1, j-1) in numbers and numbers[(i+1, j-1)] != numbers.get((i+1, j), None):
                TOTAL += numbers[(i+1, j-1)]
            if (i+1, j+1) in numbers and numbers[(i+1, j+1)] != numbers.get((i+1, j), None) \
                    and numbers[(i+1, j+1)] != numbers.get((i+1, j-1), None):
                TOTAL += numbers[(i+1, j+1)]

print(TOTAL)
