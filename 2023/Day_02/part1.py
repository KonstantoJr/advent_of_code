"""Solution for Advent of Code Challenge Day 2 part 1"""
games = {}
RED = 12
GREEN = 13
BLUE = 14

with open ("input.txt", "r", encoding='utf-8') as input_file:
    for line in input_file:
        line = line.split(':')
        # regex to match the numbers in string line[0]
        gameId = int(line[0].split(' ')[1])
        line = line[1]
        for game in line.split(';'):
            game = game.split(',')
            current_set = {
                'red': 0,
                'green': 0,
               ' blue': 0
            }
            for i, curr in enumerate(game):
                if 'red' in curr:
                    current_set['red'] = int(curr.split(" ")[1])
                    game[i] = 'red'
                elif 'green' in curr:
                    current_set['green'] = int(curr.split(" ")[1])
                    game[i] = 'green'
                elif 'blue' in curr:
                    current_set['blue'] = int(curr.split(" ")[1])
                    game[i] = 'blue'

            if gameId in games:
                games[gameId].append(current_set)
            else:
                games[gameId] = [current_set]

def check_valid_game(curr_game):
    """Checks if the game is valid"""
    # for each set in game the values for the color need to be less than the constants
    for curr_set in curr_game:
        if 'red' in curr_set and curr_set['red'] > RED:
            return False
        if 'green' in curr_set and curr_set['green'] > GREEN:
            return False
        if 'blue' in curr_set and curr_set['blue'] > BLUE:
            return False
    return True

# sum the ids of the valid games

TOTAL = 0
for game in games.items():
    if check_valid_game(game[1]):
        TOTAL += game[0]

print(TOTAL)
