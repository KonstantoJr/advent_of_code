"""Day 13 part 1"""


def input_parse():
    """Parse input into a dictionary of ints"""
    patterns = [[]]

    with open('input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line == '\n':
                patterns.append([])
            else:
                patterns[-1].append(line.strip())

    return patterns


def find_reflection(pattern):
    """Find reflection of pattern"""
    # Check for horizontal reflection
    # The reflection needs to be in the next line
    vertical = []
    horizontal = []
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            horizontal.append(i)

    # Check for vertical reflection
    # The reflection needs to be in the next column
    for i in range(len(pattern[0])-1):
        row1 = [row[i] for row in pattern]
        row2 = [row[i+1] for row in pattern]
        if row1 == row2:
            vertical.append(i)

    # Check which line is the reflection
    # You need to check the rest columns or rows
    # to see if the reflection is correct

    if len(vertical) != 0:
        for v in vertical:
            for i, j in zip(range(v-1, -1, -1), range(v+2, len(pattern[0]))):
                row1 = [row[i] for row in pattern]
                row2 = [row[j] for row in pattern]
                if row1 != row2:
                    break
            else:
                return v + 1, 'vertical'

    if len(horizontal) != 0:
        for h in horizontal:
            for i, j in zip(range(h-1, -1, -1), range(h+2, len(pattern))):
                if pattern[i] != pattern[j]:
                    break
            else:
                return h+1, 'horizontal'

    return 0, 'none'


def main():
    """Main"""
    patterns = input_parse()
    total = 0
    for i, pattern in enumerate(patterns):
        print(f'Pattern {i+1} / {len(patterns)}')
        reflection, direction = find_reflection(pattern)
        if direction == 'vertical':
            total += reflection
        elif direction == 'horizontal':
            total += reflection * 100
        else:
            print(pattern)

    print(total)


if __name__ == "__main__":
    main()
