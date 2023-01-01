from __future__ import annotations

from src.utils import (manhattan_distance, index_to_pos, pos_to_index)

moves: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Puzzle:
    parent: Puzzle | None
    size: int
    grid: list[int]
    zero: int
    g: float
    h: float
    signature: str
    get_distance: callable(tuple[float, float], tuple[float, float])

    def __init__(self, parent: Puzzle | None, size: int, grid: list[int], zero: int):
        self.size = size
        self.grid = grid
        self.parent = parent
        self.zero = zero
        self.g = parent.g + 1 if parent is not None else 0
        self.h = 0
        self.signature = self.__get_signature()
        self.get_distance = parent.get_distance if parent is not None else manhattan_distance

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

        old_pos = index_to_pos(self.zero, self.size)
        children: list[Puzzle] = []
        for move in moves:
            pos = (old_pos[0] + move[0], old_pos[1] + move[1])
            if pos[0] < 0 or pos[1] < 0 or pos[0] >= self.size or pos[1] >= self.size:
                continue
            index = pos_to_index(pos, self.size)

            copy = self.grid.copy()
            copy[self.zero] = self.grid[index]
            copy[index] = 0
            children.append(Puzzle(self, self.size, copy, index))
        return children

    def get_f(self) -> float:
        return self.g + self.h

    def distance(self, to: list[int]) -> float:
        distance: float = 0
        for i, nb in enumerate(self.grid):
            if nb != 0:
                distance += self.get_distance(index_to_pos(i, self.size), index_to_pos(to[nb], self.size))
        return distance
