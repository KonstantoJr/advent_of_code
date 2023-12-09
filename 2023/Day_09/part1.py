"""Day 9 part 1"""


def input_parse():
    """Reads the input file and returns a list of lists of integers."""
    history = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            history.append([int(x) for x in line.split()])
    return history


def predict_next(history):
    """Predicts the next number in the sequence."""
    diffs = [history]
    while True:
        diffs.append([diffs[-1][i+1] - diffs[-1][i]
                     for i in range(len(diffs[-1])-1)])
        check = set(diffs[-1])
        # break
        if len(check) == 1 and 0 in check:
            break

    prediction = 0
    for _, d in enumerate(diffs):
        prediction += d[-1]
    return prediction


def main():
    """Main program."""
    history = input_parse()
    total = 0
    for i, h in enumerate(history):
        print(f'Line {i+1}: {len(history)}')
        total += predict_next(h)
    print(total)


if __name__ == "__main__":
    main()
