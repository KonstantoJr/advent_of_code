import math


class Piece:
    def __init__(self, rock: str, height: int) -> None:
        self.rock = rock
        self._rotation = None
        self._x, self._y = self.findStartingPosition(height)

    def findStartingPosition(self, height: int) -> tuple | None:
        if self.rock == 'flatLine':
            return (2, height + 4)
        elif self.rock == 'plus':
            return (3, height + 5)
        elif self.rock == 'invertedL':
            return (2, height + 4)
        elif self.rock == 'staightLine':
            return (2, height + 4)
        elif self.rock == 'square':
            return (2, height + 4)
        return None

    def findPoints(self) -> tuple | None:
        if self.rock == 'flatLine':
            return ((self._x, self._y), (self._x + 1, self._y), (self._x + 2, self._y), (self._x + 3, self._y))
        elif self.rock == 'plus':
            return ((self._x, self._y), (self._x + 1, self._y), (self._x - 1, self._y), (self._x, self._y + 1), (self._x, self._y - 1))
        elif self.rock == 'invertedL':
            return ((self._x, self._y), (self._x + 1, self._y), (self._x + 2, self._y), (self._x + 2, self._y + 1), (self._x + 2, self._y + 2))
        elif self.rock == 'staightLine':
            return ((self._x, self._y), (self._x, self._y + 1), (self._x, self._y + 2), (self._x, self._y + 3))
        elif self.rock == 'square':
            return ((self._x, self._y), (self._x + 1, self._y), (self._x, self._y + 1), (self._x + 1, self._y + 1))
        return None

    def moveLeft(self) -> None:
        points = self.findPoints()
        minX = min(points, key=lambda x: x[0])[0]
        if minX > 0:
            self._x -= 1

    def moveRight(self) -> None:
        points = self.findPoints()
        maxX = max(points, key=lambda x: x[0])[0]
        if maxX < 6:
            self._x += 1

    def moveDown(self) -> None:
        self._y -= 1

    def moveUp(self) -> None:
        self._y += 1


class Board:
    def __init__(self, movement: str) -> None:
        self.stack = []
        self.height = 0
        self.total_rocks = 0
        self.rocks = ['flatLine', 'plus', 'invertedL', 'staightLine', 'square']
        self.rock_index = 0
        self.movement_index = 0
        self.movement = movement
        self.points = set()
        self.lastNRocks = []
        self.seenStates = dict()
        self.cycle = False

    def addPiece(self, rock: str) -> None:
        self.stack.append(Piece(rock, self.height))
        self.total_rocks += 1

    def simulation(self) -> None:
        while self.total_rocks < 1_000_000_000_000:
            if not self.cycle:
                self.lastNRocks = list(map(
                    lambda rock: frozenset(
                        [(x, y - self.height) for x, y in rock.findPoints()]),
                    self.stack[-40:]))

                startState = frozenset([
                    self.movement_index,
                    self.rock_index,
                    frozenset(self.lastNRocks)
                ])
                if startState in self.seenStates:
                    self.cycle = True
                    r0, height0 = self.seenStates[startState]

                    cycle_length = self.total_rocks - r0
                    height_per_cycle = self.height - height0
                    remaining_rocks = 1_000_000_000_000 - r0
                    num_cycles = math.floor(remaining_rocks / cycle_length)

                    self.total_rocks = r0 + num_cycles * cycle_length
                    self.height = height0 + num_cycles * height_per_cycle

                    for rock in self.lastNRocks:
                        for x, y in rock:
                            self.points.add((x, y + self.height))
                else:
                    self.seenStates[startState] = (
                        self.total_rocks, self.height)

            print(
                f'Rock: {self.total_rocks} out of 1_000_000_000_000 {self.cycle}')
            self.addPiece(self.rocks[self.rock_index])
            if self.rock_index == 0 and self.movement_index == 0 and self.height != 0:
                break
            self.rock_index = (self.rock_index + 1) % len(self.rocks)
            cur_piece = self.stack[-1]
            self.simulatePieceMovement(cur_piece, True)
            self.points.update(cur_piece.findPoints())
            self.height = max(self.height, max(
                cur_piece.findPoints(), key=lambda x: x[1])[1])

    def simulatePieceMovement(self, piece: Piece, move: bool) -> None:
        if move:
            movement = self.movement[self.movement_index]
            if movement == '<':
                piece.moveLeft()
            elif movement == '>':
                piece.moveRight()
            points = piece.findPoints()
            for point in points:
                if point in self.points:
                    if movement == '<':
                        piece.moveRight()
                    else:
                        piece.moveLeft()
                    break
            self.movement_index = (
                self.movement_index + 1) % len(self.movement)
            move = not move
        else:
            piece.moveDown()
            points = piece.findPoints()
            for point in points:
                if point[1] == 0 or point in self.points:
                    piece.moveUp()
                    return
            move = not move
        self.simulatePieceMovement(piece, move)

    def printBoard(self):
        for y in range(self.height, -1, -1):
            for x in range(7):
                if (x, y) in self.points:
                    print('X', end='')
                else:
                    print('.', end='')
            print()


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

# Create a board
board = Board(movement)
board.simulation()
# board.printBoard()
print(board.height)
