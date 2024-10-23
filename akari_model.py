from enum import Enum

class State(Enum):
    EMPTY = 1
    CELL0 = 2
    CELL1 = 3
    CELL2 = 4
    CELL3 = 5
    CELL4 = 6
    FULL = 7
    LIGHT = 8

class Akari:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.height = len(puzzle)
        self.width = len(puzzle[0])
    
    def _is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def visible(self, x, y):
        visible = [(x, y)]

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for dx, dy in directions:
            x1, y1 = x + dx, y + dy
            while self._is_within_bounds(x1, y1) and self.puzzle[x1][y1] == State.EMPTY:
                visible.append((x1, y1))
                x1 += dx
                y1 += dy

        return visible

    def count_state_in_direction(self, x, y, dx, dy, state):
        if self.puzzle[x][y] != state:
            return 1 

        count = 1
        x += dx
        y += dy

        while self._is_within_bounds(x, y) and self.puzzle[x][y] == state:
            count += 1
            x += dx
            y += dy

        return count
    
    def neighbors(self, x, y):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            neighbor_x = x + dx
            neighbor_y = y + dy
            if self._is_within_bounds(neighbor_x, neighbor_y):
                neighbors.append((neighbor_x, neighbor_y))
        return neighbors