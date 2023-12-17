"""Day 16 part 2"""


class Beam:
    """Beam class"""
    moves = set()

    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self) -> None:
        """Move beam"""
        if self.direction == 'right':
            self.x += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1

    def mirror(self, grid: tuple[tuple[str]]) -> None:
        """Mirror beam"""
        if grid[self.y][self.x] == '/':
            if self.direction == 'right':
                self.direction = 'up'
            elif self.direction == 'left':
                self.direction = 'down'
            elif self.direction == 'up':
                self.direction = 'right'
            elif self.direction == 'down':
                self.direction = 'left'
        elif grid[self.y][self.x] == '\\':
            if self.direction == 'right':
                self.direction = 'down'
            elif self.direction == 'left':
                self.direction = 'up'
            elif self.direction == 'up':
                self.direction = 'left'
            elif self.direction == 'down':
                self.direction = 'right'

    def split(self, grid: tuple[tuple[str]]) -> tuple['Beam', 'Beam']:
        """Split beam"""
        if grid[self.y][self.x] == '-':
            if self.direction in ('up', 'down'):
                return Beam(self.x, self.y, 'left'), Beam(self.x, self.y, 'right')
        if grid[self.y][self.x] == '|':
            if self.direction in ('left', 'right'):
                return Beam(self.x, self.y, 'up'), Beam(self.x, self.y, 'down')

        return None, None

    def run(self, grid: tuple[tuple[str]]):
        """Run beam"""
        while True:
            self.move()
            if (self.x, self.y, self.direction) in Beam.moves:
                # This means the beam is in a loop
                return None, None
            # Check if the beam is out of bounds
            if self.x < 0 or self.x >= len(grid[0]) or self.y < 0 or self.y >= len(grid):
                return None, None
            Beam.moves.add((self.x, self.y, self.direction))
            self.mirror(grid)
            left, right = self.split(grid)
            if left and right:
                # When the beam splits, return the two beams
                return left, right

    def __repr__(self) -> str:
        return f'Beam({self.x}, {self.y}, {self.direction})'


def input_parse(filename: str) -> tuple[tuple[str]]:
    """Parse input"""
    with open(filename, 'r', encoding='utf-8') as f:
        return tuple(tuple(line.strip()) for line in f.readlines())


def main():
    """Main"""
    grid = input_parse('input.txt')
    starting_positions = []

    # loop through the top row
    for x, _ in enumerate(grid[0]):
        starting_positions.append((x, -1, 'down'))
    # loop through the bottom row
    for x, _ in enumerate(grid[-1]):
        starting_positions.append((x, len(grid), 'up'))
    # loop through the left column
    for y, _ in enumerate(grid):
        starting_positions.append((-1, y, 'right'))
    # loop through the right column
    for y, _ in enumerate(grid):
        starting_positions.append((len(grid[0]), y, 'left'))

    total = 0

    for i, (x, y, direction) in enumerate(starting_positions):
        print(f"Progress: {i+1}/{len(starting_positions)}")
        beams = []
        beams.append(Beam(x, y, direction))
        index = 0
        while index < len(beams):
            left, right = beams[index].run(grid)
            if left and right:
                beams.append(left)
                beams.append(right)
            index += 1

        energized = set()
        for beam in beams:
            for move in beam.moves:
                energized.add((move[0], move[1]))
        Beam.moves.clear()
        total = max(total, len(energized))

    print(total)


if __name__ == "__main__":
    main()
