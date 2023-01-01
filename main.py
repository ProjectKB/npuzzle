import argparse as a

import src.nparser as parser
import src.utils as utils
from src.solvers.a_star import a_star
from src.solvers.greedy_search import greedy_search
from src.solvers.uniform_cost import uniform_cost

if __name__ == '__main__':
    argparse = a.ArgumentParser()

    argparse.add_argument("-f", "--file", default=False,
                          help="file containing the puzzle. Overrides -i")
    argparse.add_argument("-i", "--input", action="store_true", default=False,
                          help="read the puzzle as string")
    argparse.add_argument("-v", "--verbose", action="store_true", default=False,
                          help="add verbose while algo is running")
    argparse.add_argument("-p", "--process", action="store_true", default=False,
                          help="the output will show the algorithm process")
    argparse.add_argument("-d", "--distance", default="manhattan",
                          help='choose a distance method between "manhattan", "euclidean" and "chebyshev", default is '
                               '"manhattan"')
    argparse.add_argument("-a", "--algo", default="a_star",
                          help='choose a resolution algorithm between "a_star", "greedy" and "uniform", default '
                               'is "a_star"')

    args = argparse.parse_args()

    if not args.file and not args.input:
        argparse.error(
            'you have to use at least one argument between [-i] and [-f].')
    elif args.distance not in ["manhattan", "euclidean", "chebyshev"]:
        argparse.error(
            'distance available are "manhattan", "euclidean" or "chebyshev"')
    elif args.algo not in ["a_star", "greedy", "uniform"]:
        argparse.error(
            'algo available are "a_star", "greedy" or "uniform"')

    puzzle = parser.parse(args)
    puzzle.get_distance = utils.get_distance(args.distance)
    goal = utils.generate_control(puzzle.size)

    match args.algo:
        case "a_star": a_star(puzzle, utils.inverse(puzzle.size, goal), args.verbose, args.process)
        case "greedy": greedy_search(puzzle, utils.inverse(puzzle.size, goal), args.verbose, args.process)
        case "uniform": uniform_cost(puzzle, utils.inverse(puzzle.size, goal), args.verbose, args.process)
