import argparse as a

import src.nparser as parser
import src.utils as utils
from src.puzzle import Puzzle
from src.solvers.a_star import a_star
from src.solvers.greedy_search import greedy_search
from src.solvers.uniform_cost import uniform_cost


def print_all(puzzle: Puzzle):
    if puzzle.parent is not None:
        print_all(puzzle.parent)
    print(puzzle)


if __name__ == '__main__':
    argparse = a.ArgumentParser()

    argparse.add_argument("-f", "--file", default=False,
                          help="file containing the puzzle. Overrides -i")
    argparse.add_argument("-i", "--input", action="store_true", default=False,
                          help="read the puzzle as string")
    argparse.add_argument("-c", "--control", action="store_true", default=False,
                          help="display control puzzle")
    argparse.add_argument("-p", "--print", action="store_true", default=False,
                          help="display puzzle before to be solved")

    args = argparse.parse_args()

    if not args.file and not args.input:
        argparse.error(
            'you have to use at least one argument between [-i] and [-f].')

    puzzle = parser.parse(args)
    goal = utils.generate_control(puzzle.size)

    if args.print:
        print(puzzle)

    if args.control:
        print(goal)

    # a_star(puzzle, utils.inverse(puzzle.size, goal))
    # greedy_search(puzzle, utils.inverse(puzzle.size, goal))
    uniform_cost(puzzle, utils.inverse(puzzle.size, goal))
