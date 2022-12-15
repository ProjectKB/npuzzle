import src.error as e
import src.puzzle as p

import re


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
            e.Error.throw(e.Error.FAIL, e.Error.FILE_NOT_FOUND_ERROR, f"no such file: {self.args.file}")
        except IsADirectoryError:
            e.Error.throw(e.Error.FAIL, e.Error.IS_A_DIRECTORY_ERROR, f"is a directory: {self.args.file}")
        except PermissionError:
            e.Error.throw(e.Error.FAIL, e.Error.PERMISSION_ERROR, f"permission denied: {self.args.file}")
        except UnicodeDecodeError:
            e.Error.throw(e.Error.FAIL, e.Error.UNICODE_DECODE_ERROR,
                          f"'utf-8' codec can't decode byte: {self.args.file}")

        for line in file:
            # remove comment
            line = re.sub(Parser.COMMENT_PATTERN, '', line)

            # skip new line alone
            if line == "\n":
                continue

            # remove new line
            line = line.replace('\n', '')

            # search for size
            if not size:
                r = re.search(Parser.SIZE_PATTERN, line)
                if r:
                    size = int(line)
                    if size < 2:
                        e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                                      f"file format error: minimum size is 2, found {size}")
                    continue

            # search for forbidden chars
            r = re.search(Parser.OTHER_THAN_SPACE_DIGITS_PATTERN, line)
            if r:
                e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, f"file format error: forbidden char: {line}")

            # search for missing size
            if not size:
                e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, "file format error: size of puzzle is missing")

            # check that there are at least size numbers on the line
            if len(line.split()) is not size:
                e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                              f"file format error: {size} numbers are expected for "
                              f"one line: {line}")

            # save line
            puzzle.append(line.split())

        f.close()

        # search for missing size
        if not size:
            e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, "file format error: size of puzzle is missing")

        # generate puzzle control template
        puzzle_control = {str(i): False for i in range(size ** 2)}

        # check that no number is repeated or too big
        for row in puzzle:
            for nb in row:
                if puzzle_control.get(nb) is None:
                    e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, f"file format error: number too big: {nb}")
                elif puzzle_control.get(nb) is not False:
                    e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, f"file format error: number repeated: {nb}")
                puzzle_control[nb] = nb

        # check that no number is missing
        if False in puzzle_control.values():
            e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                          f"file format error: at least one of 0..{size ** 2 - 1} number is missing")

        return p.Puzzle(size, puzzle)

    def get_input(self):
        contents = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            except UnicodeDecodeError:
                e.Error.throw(e.Error.FAIL, e.Error.UNICODE_DECODE_ERROR,
                              f"'utf-8' codec can't decode byte: {self.args.file}")
            except KeyboardInterrupt:
                e.Error.throw(e.Error.FAIL, e.Error.KEYBOARD_INTERRUPT_ERROR, "use Ctrl+D to interrupt input reading")

            contents.append(line)
        return contents

    def parse_input(self):
        input = self.get_input()
        size = False
        puzzle = []

        for line in input:
            # remove comment
            line = re.sub(Parser.COMMENT_PATTERN, '', line)

            # skip new/empty line
            if line == "\n" or line == "":
                continue

            # remove space
            line = line.strip()

            # search for size
            if not size:
                r = re.search(Parser.SIZE_PATTERN, line)
                if not r:
                    e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, f"file format error: forbidden char: {line}")
                size = int(line)
                if size < 2:
                    e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                                  f"file format error: minimum size is 2, found {size}")
                continue

            # search for forbidden chars
            r = re.search(Parser.SIZE_PATTERN, line)
            if not r:
                e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, f"file format error: forbidden char: {line}")

            puzzle.append(line)

        # search for missing size
        if not size:
            e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, "file format error: size of puzzle is missing")

        # check puzzle len then transform is format
        len_puzzle = len(puzzle)
        if len_puzzle is not size ** 2:
            e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                          f"file format error: size is {size}, {size ** 2} numbers should have been provided, found {len_puzzle}")
        puzzle = [[puzzle[j + size * i] for j in range(size)] for i in range(size)]

        # generate puzzle control template
        puzzle_control = {str(i): False for i in range(size ** 2)}

        # check that no number is repeated or too big
        for row in puzzle:
            for nb in row:
                if puzzle_control.get(nb) is None:
                    e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, f"file format error: number too big: {nb}")
                elif puzzle_control.get(nb) is not False:
                    e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR, f"file format error: number repeated: {nb}")
                puzzle_control[nb] = nb

        # check that no number is missing
        if False in puzzle_control.values():
            e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                          f"file format error: at least one of 0..{size ** 2 - 1} number is missing")

        return p.Puzzle(size, puzzle)

    def parse(self):
        self.format = 'file' if self.args.file else 'input'

        parse_func = {
            "file": lambda: self.parse_file(),
            'input': lambda: self.parse_input(),
        }

        return parse_func[self.format]()
