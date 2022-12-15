import sys
import argparse
import re
import math


class Tools:
    # Colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Error Names
    FILE_NOT_FOUND_ERROR = "FileNotFoundError"
    IS_A_DIRECTORY_ERROR = "IsADirectoryError"
    PERMISSION_ERROR = "PermissionError"
    UNICODE_DECODE_ERROR = "UnicodeDecodeError"
    FILE_FORMAT_ERROR = "FileFormatError"

    @staticmethod
    def print_error(msg):
        print(msg)
        sys.exit(0)

    @staticmethod
    def throw(level, type, msg):
        print(f"\n\t{level}[{type}] -> {Tools.ENDC}{msg}\n")
        sys.exit(0)


class Puzzle:
    def __init__(self, size, puzzle):
        self.size = size
        self.puzzle = puzzle
        self.control = self.generate_control()
        self.field_size = self.get_field_size()

    def __str__(self):
        output = f"\n\t{self.size:>{self.field_size}}\n\n"
        for row in self.puzzle:
            output += '\t'
            for nb in row:
                output += f"{nb:>{self.field_size}} "
            output += '\n'
        return output

    def display_control(self):
        print("")
        for row in self.control:
            print("\t", end='')
            for nb in row:
                print(f"{nb:>{self.field_size}}", end=' ')
            print("")
        print("")

    def get_field_size(self):
        pow = 1
        size = self.size ** 2 - 1
        while size > 10 ** pow:
            pow += 1
        return pow

    def generate_control(self):
        control = [['0' for _ in range(self.size)] for _ in range(self.size)]
        center = {'y': math.floor(self.size / 2), 'x': math.floor(self.size / 2)} if math.floor(self.size % 2) else {
            'y': math.floor(self.size / 2), 'x': math.floor(self.size / 2) - 1}

        step = 1
        count_step = 0
        count_sign = 1
        h = self.size ** 2 - 1
        y = center['y']
        x = center['x']
        x_axis = True
        neg = True if self.size % 2 else False
        control[y][x] = '0'

        while h > 0:
            if count_step == 2:
                count_step = 0
                step += 1

            if count_sign == 2:
                count_sign = 0
                neg = not neg

            for i in range(step):
                if x_axis:
                    if neg:
                        x -= 1
                    else:
                        x += 1
                else:
                    if neg:
                        y -= 1
                    else:
                        y += 1
                if x < 0:
                    break
                control[y][x] = str(h)
                h -= 1

            x_axis = not x_axis
            count_step += 1
            count_sign += 1

        return control


class Parser:
    COMMENT_PATTERN = "#.*|"
    SIZE_PATTERN = "^\d+$"
    OTHER_THAN_SPACE_DIGITS_PATTERN = "[^ ?\d ?]"

    def __init__(self, args):
        self.args = args
        self.format = None

    def parse_file(self):
        size = False
        puzzle = []

        try:
            f = open(self.args.file, 'r')
            file = f.readlines()
        except FileNotFoundError:
            Tools.throw(Tools.FAIL, Tools.FILE_NOT_FOUND_ERROR, f"No such file: {self.args.file}")
        except IsADirectoryError:
            Tools.throw(Tools.FAIL, Tools.IS_A_DIRECTORY_ERROR, f"Is a directory: {self.args.file}")
        except PermissionError:
            Tools.throw(Tools.FAIL, Tools.PERMISSION_ERROR, f"Permission denied: {self.args.file}")
        except UnicodeDecodeError:
            Tools.throw(Tools.FAIL, Tools.UNICODE_DECODE_ERROR, f"'utf-8' codec can't decode byte: {self.args.file}")

        for line in file:
            # remove comment
            line = re.sub(Parser.COMMENT_PATTERN, '', line)

            # skip new line alone
            if line == "\n":
                continue

            # remove new line
            line = line.replace('\n', '')

            # search for size
            r = re.search(Parser.SIZE_PATTERN, line)
            if r:
                size = int(line)
                if size == 1:
                    Tools.throw(Tools.FAIL, Tools.FILE_FORMAT_ERROR, f"File format error: minimum size is 2")
                continue

            # search for forbidden chars
            r = re.search(Parser.OTHER_THAN_SPACE_DIGITS_PATTERN, line)
            if r:
                Tools.throw(Tools.FAIL, Tools.FILE_FORMAT_ERROR, f"File format error: forbidden char: {line}")

            # search for missing size
            if not size:
                Tools.throw(Tools.FAIL, Tools.FILE_FORMAT_ERROR, "File format error: size of puzzle is missing")

            # save line
            puzzle.append(line.split())

        f.close()

        # generate puzzle control template
        puzzle_control = {str(i): False for i in range(size ** 2)}

        # check that no number is repeated or too big
        for row in puzzle:
            for nb in row:
                if puzzle_control.get(nb) is None:
                    Tools.throw(Tools.FAIL, Tools.FILE_FORMAT_ERROR, f"File format error: number too big: {nb}")
                elif puzzle_control.get(nb) is not False:
                    Tools.throw(Tools.FAIL, Tools.FILE_FORMAT_ERROR, f"File format error: number repeated: {nb}")
                puzzle_control[nb] = nb

        # check that no number is missing
        if False in puzzle_control.values():
            Tools.throw(Tools.FAIL, Tools.FILE_FORMAT_ERROR,
                        f"File format error: at least one of 0..{size ** 2 - 1} number is missing")

        return Puzzle(size, puzzle)

    def parse_input(self):
        print(self.args.input)

    def determine_format(self):
        return 'file' if self.args.file else 'input'

    def parse(self):
        self.format = self.determine_format()

        func = {
            "file": lambda: self.parse_file(),
            'input': lambda: self.parse_input(),
        }

        return func[self.format]()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", default=False,
                        help="File containing the puzzle. Overrides -i")
    parser.add_argument("-i", "--input", default=False,
                        help="Read the puzzle as string")

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.error('You have to use at least one argument between [-i] and [-f].')

    p = Parser(args)
    puzzle = p.parse()
    puzzle.display_control()
    print(puzzle)
