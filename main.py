import argparse as a
import src.parser as p

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
        argparse.error('you have to use at least one argument between [-i] and [-f].')

    parser = p.Parser(args)
    puzzle = parser.parse()

    if args.print:
        print(puzzle)

    if args.control:
        puzzle.display_control()
