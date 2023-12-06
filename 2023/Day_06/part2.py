"""Day 6 part 2"""


def parse_input():
    """Parse input file and return time and distance lists"""
    time = ""
    distance = ""
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if "Time" in line:
                time = int("".join(line.split(":")[1].split()))
            elif "Distance" in line:
                distance = int("".join(line.split(":")[1].split()))
    return time, distance


def calculate_win(time, record):
    """Calculate how many times you can beat the record"""
    total_wins = 0
    for i in range(0, time+1):
        if (i % 1_000_000) == 0:
            print("Progress:", i)
        curr_speed = i
        curr_time = time - i
        curr_distance = curr_speed * curr_time
        if curr_distance > record:
            total_wins += 1

    return total_wins


if __name__ == "__main__":
    TIME, DISTANCE = parse_input()
    print("Time:", TIME)
    print("Distance:", DISTANCE)
    WINS = calculate_win(TIME, DISTANCE)
    print("Solution:", WINS)
