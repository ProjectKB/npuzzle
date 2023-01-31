from __future__ import annotations

import heapq

from src.puzzle import Puzzle
from src.utils import print_success, print_verbose, print_failure


def greedy_search(puzzle: Puzzle, goal: list[int], verbose: bool, process: bool) -> Puzzle | None:
    # A* but g == 0 for every node
    # It can be really fast, but it can lead to suboptimal solution because of local minimum.
    # Meaning the algorithm doesn't consider the cost of an action but only his short term result,
    # resulting in possibly longer path or even no path at all
    puzzle.h = puzzle.distance(goal)

    open_list_q: list[tuple[float, float, str]] = [(puzzle.h, puzzle.g, puzzle.signature)]
    open_list: dict[str, Puzzle] = {puzzle.signature: puzzle}
    closed_list: dict[str, Puzzle] = {}

    if verbose:
        step = 0

    while open_list:
        if verbose:
            step += 1

        current_q = heapq.heappop(open_list_q)

        while closed_list.get(current_q[2]):
            current_q = heapq.heappop(open_list_q)

        current = open_list[current_q[2]]

        closed_list[current.signature] = current
        del open_list[current.signature]

        if current.h == 0:
            print_success(open_list, closed_list, current, process)
            return current

        children = current.create_children()

        for child in children:
            if closed_list.get(child.signature):
                continue

            child.h = child.distance(goal)
            if open_list.get(child.signature) is None or child.g < open_list[child.signature].g:
                heapq.heappush(open_list_q, (child.h, child.g, child.signature))
                open_list[child.signature] = child

        if verbose and step % 10000 == 0:
            print_verbose(step, open_list, closed_list)

    print_failure()
