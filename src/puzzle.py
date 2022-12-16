from __future__ import annotations


class Puzzle:
    size: int
    grid: list[list[int]]
    parent: Puzzle | None

    def __init__(self, parent: Puzzle | None, size: int, grid: list[list[int]]):
        self.size = size
        self.grid = grid
        self.parent = parent

    def __str__(self):
        max_len = len(str(self.size ** 2))
        output = f"{self.size}\n > "
        output += "\n > ".join([" ".join([str(item).rjust(max_len)
                                          for item in line]) for line in self.grid])
        return output

    def create_childs(self):

        pass

    def get_f(self) -> int:
        # f = g + h
        return 0

    def get_g(self):
        # the number of nodes traversed from the start node to current node
        pass

    def get_h(self):
        # choose heuristic according to strategy (euclidian, manhattan...)
        pass
