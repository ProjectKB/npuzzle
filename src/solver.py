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


def a_star(puzzle: Puzzle, goal: list[list[int]]):
    # A* algorithm is an algorithm of informed search -> you know what you're looking for

    open_list = [puzzle]
    closed_list = []

    while open_list:
        # find the node with the lowest f-value
        current_puzzle = min(open_list, key=Puzzle.get_f)

        if current_puzzle.grid == goal:
            return current_puzzle

    # remove current_puzzle from open_list and add it to closed_list
    # open_list.remove(current)
    # closed_list.append(current)

    # current_children = function to calculate current_children
    # each child could be a puzzle object
    # in this case we should add a "parent" attribute to puzzle object for reconstructing the path later
    # the function to calculate children should be in puzzle class too
    # we could also move f, g and h function to puzzle class and create attribute according to it
    # this way it should be easier to manipulate them
    # calculate current children function should create n child, defining their g, h, f and parent at initialization

    # for child in current_children:
    # if child in closed_list:
    # continue

    # if child not in open_list:
    # add child to open_list
    # elif child in open list and child.g < old_child.g:
    # replace old_child by child

    # No solution found
    # return None

    pass
