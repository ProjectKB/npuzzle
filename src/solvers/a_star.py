from __future__ import annotations

import heapq

from src.puzzle import Puzzle


def a_star(puzzle: Puzzle, goal: list[int]) -> Puzzle | None:
    puzzle.h = puzzle.distance(goal)

    open_list_q: list[tuple[float, float, float, str]] = [
        (puzzle.get_f(), puzzle.h, puzzle.g, puzzle.signature)]
    open_list: dict[str, Puzzle] = {puzzle.signature: puzzle}
    closed_list: dict[str, Puzzle] = {}

    # DEBUG
    step = 0

    while open_list:
        # DEBUG
        step += 1

        current_q = heapq.heappop(open_list_q)

        while closed_list.get(current_q[3]):
            current_q = heapq.heappop(open_list_q)

        current = open_list[current_q[3]]

        if current.h == 0:
            print(
                f"Steps: {step} - Open {len(open_list)} - Closed {len(closed_list)} - G: {current.g}")
            return current

        closed_list[current.signature] = current
        del open_list[current.signature]

        children = current.create_children()

        for child in children:
            old_closed = closed_list.get(child.signature)
            if old_closed:
                if child.g < old_closed.g:
                    old_closed.g = child.g
                    old_closed.parent = child.parent
                continue

            child.h = child.distance(goal)
            if open_list.get(child.signature) is None or child.g < open_list[child.signature].g:
                heapq.heappush(
                    open_list_q, (child.get_f(), child.h, child.g, child.signature))
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
