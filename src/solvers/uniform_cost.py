from __future__ import annotations

import heapq

from src.puzzle import Puzzle


def uniform_cost(puzzle: Puzzle, goal: list[int]):
    # A* but h == 0 for every node resulting in BFS algorithm (nodes are explored in width, and EVERY one of them are visited)
    pass
