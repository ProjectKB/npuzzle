from __future__ import annotations

moves: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Puzzle:
    parent: Puzzle | None
    size: int
    grid: list[list[int]]
    zero: tuple[int, int]

    def __init__(self, parent: Puzzle | None, size: int, grid: list[list[int]], zero: tuple[int, int]):
        self.size = size
        self.grid = grid
        self.parent = parent
        self.zero = zero

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

    def get_f(self) -> float:
        # f = g + h
        return 0

    def get_g(self) -> float:
        # the number of nodes traversed from the start node to current node
        return 0

    def get_h(self) -> float:
        # choose heuristic according to strategy (euclidian, manhattan...)
        return 0
