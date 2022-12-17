from __future__ import annotations

from src.error import Error as e
from src.utils import manhattan_distance, euclidean_distance, chebyshev_distance

moves: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Puzzle:
    parent: Puzzle | None
    size: int
    grid: list[list[int]]
    zero: tuple[int, int]
    g: int
    h: int | None
    f: int | None

    def __init__(self, parent: Puzzle | None, size: int, grid: list[list[int]], zero: tuple[int, int]):
        self.size = size
        self.grid = grid
        self.parent = parent
        self.zero = zero
        self.g = parent.g + 1 if self.parent is not None else 0
        self.h = None
        self.f = None

    def __str__(self) -> str:
        max_len = len(str(self.size ** 2))
        output = f"{self.size} {self.zero}\n > "
        output += "\n > ".join([" ".join([str(item).rjust(max_len)
                                          for item in line]) for line in self.grid])
        return output

    def __eq__(self, other: object) -> bool:
        if type(other) is Puzzle:
            return self.grid == other.grid
        return False

    def create_children(self) -> list[Puzzle]:
        global moves

        children: list[Puzzle] = []
        for move in moves:
            pos = (self.zero[0] + move[0], self.zero[1] + move[1])
            if pos[0] < 0 or pos[1] < 0 or pos[0] >= self.size or pos[1] >= self.size:
                continue

            copy = [l.copy() for l in self.grid.copy()]
            copy[self.zero[1]][self.zero[0]] = self.grid[pos[1]][pos[0]]
            copy[pos[1]][pos[0]] = 0
            children.append(Puzzle(self, self.size, copy, pos))
        return children

    def get_f(self):
        return self.f

    def set_f(self, goal_dict: {int: list[int]}) -> float:
        self.f = self.g + self.set_h(goal_dict)
        return self.f

    def set_h(self, goal_dict: {int: list[int]}) -> float:
        # choose heuristic according to strategy (euclidian, manhattan...)
        # what's better between get h for every case or only for moving one ?

        h: int = 0

        for y, row in enumerate(self.grid):
            for x, nb in enumerate(row):
                h += manhattan_distance([y, x], goal_dict[nb])
        self.h = h

        return self.h

    def set_f2(self, goal_zero: list[int]) -> float:
        self.f = self.g + self.set_h2(goal_zero)
        return self.f

    def set_h2(self, goal_zero: list[int]) -> float:
        self.h = manhattan_distance(self.zero, goal_zero)
        return self.h
