from __future__ import annotations

from src.error import Error as e
from src.utils import manhattan_distance, euclidean_distance, chebyshev_distance, inverse

moves: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Puzzle:
    parent: Puzzle | None
    size: int
    grid: list[list[int]]
    zero: tuple[int, int]
    g: float
    h: float
    signature: str

    def __init__(self, parent: Puzzle | None, size: int, grid: list[list[int]], zero: tuple[int, int]):
        self.size = size
        self.grid = grid
        self.parent = parent
        self.zero = zero
        self.g = parent.g + 1 if parent is not None else 0
        self.h = 0
        self.signature = self.__get_signature();

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
    
    def __get_signature(self) -> str:
        signature: str = ""

        for row in self.grid:
            for nb in row:
                signature += f"{str(nb)},"
        return signature

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

    def get_f(self) -> float:
        return self.g + self.h

    def distance(self, to: list[tuple[int, int]]) -> float:
        # choose heuristic according to strategy (euclidian, manhattan...)
        # what's better between get h for every case or only for moving one ?

        distance: float = 0
        for y, row in enumerate(self.grid):
            for x, nb in enumerate(row):
                if nb != 0:
                    distance += manhattan_distance((x, y), to[nb])
        return distance

    def distance2(self, to: tuple[float, float]) -> float:
        # choose heuristic according to strategy (euclidian, manhattan...)
        # what's better between get h for every case or only for moving one ?

        return manhattan_distance(self.zero, to)
