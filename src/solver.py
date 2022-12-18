from __future__ import annotations

import heapq

from src.puzzle import Puzzle


def greedy_search(puzzle: Puzzle):
    # A* but g == 0 for every node
    # It can be really fast, but it can lead to suboptimal solution because of local minimum.
    # Meaning the algorithm doesn't consider the cost of an action but only his short term result,
    # resulting in possibly longer path or even no path at all
    pass


def uniform_cost(puzzle: Puzzle):
    # A* but h == 0 for every node resulting in BFS algorithm (nodes are explored in width, and EVERY one of them are visited)
    pass

def __print_all(puzzle: Puzzle):
    if puzzle.parent is not None:
        __print_all(puzzle.parent)
    print(puzzle)

def a_star(puzzle: Puzzle, goal: list[tuple[int, int]]) -> Puzzle | None:
    puzzle.h = puzzle.distance(goal)

    open_list_q: list[tuple[float, float, str]] = [
        (puzzle.get_f(), puzzle.g, puzzle.signature)]
    open_list: dict[str, Puzzle] = {puzzle.signature: puzzle}
    closed_list: dict[str, Puzzle] = {}

    # DEBUG
    step = 0

    while open_list:
        # DEBUG
        step += 1

        current_q = heapq.heappop(open_list_q)
        current = open_list[current_q[2]]

        if current.h == 0:
            __print_all(current)
            print(f"Steps: {step} - G: {current.g}")
            return current

        closed_list[current.signature] = current
        del open_list[current.signature]

        children = current.create_children()

        for child in children:
            if closed_list.get(child.signature):
                continue

            child.h = child.distance(goal)
            if open_list.get(child.signature) is None or child.g < open_list[child.signature].g:
                heapq.heappush(
                    open_list_q, (child.get_f(), child.g, child.signature))
                open_list[child.signature] = child

        # DEBUG
        if step % 10000 == 0:
            print(
                f"Running step {step}, open {len(open_list)}, closed {len(closed_list)}")

    # DEBUG
    print(f"Finished in {step} steps")

    # No solution found
    # return None
    return None
