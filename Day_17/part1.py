def findStartingPosition(height, rock):
    if rock == 'flatLine':
        return (2, height + 3)
    elif rock == 'plus':
        return (3, height + 5)
    elif rock == 'invertedL':
        return (4, height + 3)
    elif rock == 'staightLine':
        return (2, height + 3)
    elif rock == 'square':
        return (2, height + 3)


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

movement = data[0]
movement_index = 0
rocks = ['flatLine', 'plus', 'invertedL', 'staightLine', 'square']
# Flatline use the left most square to represent the rock
# Plus use the center square to represent the rock
# InvertedL use the left most square to represent the rock
# StraightLine use the down most square to represent the rock
# Square use the left and down most square to represent the rock
rock_index = 0
height = 0
total_rocks = 0
stack = []

while total_rocks < 2022:
    cur_rock = rocks[rock_index]
    cur_pos = findStartingPosition(height, cur_rock)
