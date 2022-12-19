from __future__ import annotations

from src.error import Error as e
from src.utils import manhattan_distance, euclidean_distance, chebyshev_distance, index_to_pos, pos_to_index

moves: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Puzzle:
    parent: Puzzle | None
    size: int
    grid: list[int]
    zero: int
    g: float
    h: float
    signature: str

    def __init__(self, parent: Puzzle | None, size: int, grid: list[int], zero: int):
        self.size = size
        self.grid = grid
        self.parent = parent
        self.zero = zero
        self.g = parent.g + 1 if parent is not None else 0
        self.h = 0
        self.signature = self.__get_signature()

    def __str__(self) -> str:
        max_len = len(str(self.size ** 2))
        output = f"{self.size} ({self.g})\n"
        for i in range(0, self.size ** 2, self.size):
            output += f" > {' '.join(str(e).rjust(max_len) for e in self.grid[i:i + self.size])}\n"
        return output

    def __get_signature(self) -> str:
        return str(self.grid)

    def create_children(self) -> list[Puzzle]:
        global moves

        children: list[Puzzle] = []
        for move in moves:
            pos = self.zero + pos_to_index(move, self.size)
            if pos < 0 or pos >= self.size ** 2:
                continue

            copy = self.grid.copy()
            copy[self.zero] = self.grid[pos]
            copy[pos] = 0
            children.append(Puzzle(self, self.size, copy, pos))
        return children

    def get_f(self) -> float:
        return self.g + self.h

    def distance(self, to: list[int]) -> float:
        # choose heuristic according to strategy (euclidian, manhattan...)
        # what's better between get h for every case or only for moving one ?

        distance: float = 0
        for i, nb in enumerate(self.grid):
            if nb != 0:
                distance += manhattan_distance(index_to_pos(i,
                                               self.size), index_to_pos(to[nb], self.size))
        return distance
