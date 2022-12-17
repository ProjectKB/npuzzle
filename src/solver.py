from __future__ import annotations

from src.puzzle import Puzzle
from src.error import Error as e
from src.utils import find_zero


def greedy_search(puzzle: Puzzle):
    # A* but g == 0 for every node
    # It can be really fast, but it can lead to suboptimal solution because of local minimum.
    # Meaning the algorithm doesn't consider the cost of an action but only his short term result,
    # resulting in possibly longer path or even no path at all
    pass


def uniform_cost(puzzle: Puzzle):
    # A* but h == 0 for every node resulting in BFS algorithm (nodes are explored in width, and EVERY one of them are visited)
    pass


def a_star(puzzle: Puzzle, goal: list[list[int]], goal_dict: {int: list[int]}) -> Puzzle | None:
    # A* algorithm is an algorithm of informed search -> you know what you're looking for

    open_list = [puzzle]
    closed_list = []

    # DEBUG
    step = 0

    goal_zero = find_zero(goal)

    while open_list:
        # DEBUG
        step += 1

        # find the node with the lowest f-value
        current = min(open_list, key=Puzzle.get_f)

        if current.grid == goal:
            return current

        # remove current from open_list and add it to closed_list
        open_list.remove(current)
        closed_list.append(current)

        children = current.create_children()

        for child in children:
            if child in closed_list:
                continue

            child.set_f(goal_dict)

            # set_f2 is for calculating f only for zero
            # child.set_f2(goal_zero)
            if child not in open_list:
                open_list.append(child)
            elif child in open_list:
                for state in open_list:
                    if state == child and state.g >= child.g:
                        state.parent = current
                        state.g = child.g
                        state.h = child.h
                        state.f = child.f
        print(f"Running step {step}, open {len(open_list)}, closed {len(closed_list)}")

    # DEBUG
    print(f"Finished in {step} steps")

    # No solution found
    # return None
    return None
