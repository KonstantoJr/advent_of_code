"""Day 15 part 2"""


class Lens():
    def __init__(self, label, focus):
        self.label = label
        self.focus = focus


def input_parse():
    """Parse input into list of ints"""
    steps = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            steps.extend(line.strip().split(','))
    return steps


def hash_step(step: str):
    """Hash a step"""
    c_value = 0
    for char in step:
        c_value += ord(char)
        c_value *= 17
        c_value = c_value % 256
    return c_value


def calculate_focusing_power(boxes):
    """Calculate focusing power"""
    focusing_power = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focusing_power += (i + 1) * (j + 1) * lens.focus
    return focusing_power


def main():

    steps = input_parse()
    boxes = [[] for _ in range(256)]
    for step in steps:
        if '=' in step:
            label, focus = step.split('=')
            label = label.strip()
            focus = int(focus.strip())
            index = hash_step(label)

            for i, lens in enumerate(boxes[index]):
                if lens.label == label:
                    lens.focus = focus
                    break
            else:
                boxes[index].append(Lens(label, focus))
        if '-' in step:
            label = step.split('-')[0].strip()
            index = hash_step(label)
            for i, lens in enumerate(boxes[index]):
                if lens.label == label:
                    boxes[index].pop(i)
                    break
    print(calculate_focusing_power(boxes))


if __name__ == "__main__":
    main()
