import src.error as e
import src.puzzle as p

import re


class Parser:
    COMMENT_PATTERN = "#.*|"
    SIZE_PATTERN = "^\d+$"
    OTHER_THAN_SPACE_DIGITS_PATTERN = "[^ ?\d ?]"

    def __init__(self, args):
        self.args = args

    def __get_file_content(self):
        lines: list[str] = []

        try:
            f = open(self.args.file, 'r')
            lines = f.readlines()
        except FileNotFoundError:
            e.Error.throw(e.Error.FAIL, e.Error.FILE_NOT_FOUND_ERROR,
                          f"no such file: {self.args.file}")
        except IsADirectoryError:
            e.Error.throw(e.Error.FAIL, e.Error.IS_A_DIRECTORY_ERROR,
                          f"is a directory: {self.args.file}")
        except PermissionError:
            e.Error.throw(e.Error.FAIL, e.Error.PERMISSION_ERROR,
                          f"permission denied: {self.args.file}")
        except UnicodeDecodeError:
            e.Error.throw(e.Error.FAIL, e.Error.UNICODE_DECODE_ERROR,
                          f"'utf-8' codec can't decode byte: {self.args.file}")
        return lines

    def __get_input(self):
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
                e.Error.throw(e.Error.FAIL, e.Error.KEYBOARD_INTERRUPT_ERROR,
                              "use Ctrl+D to interrupt input reading")

            contents.append(line)
        return contents

    def __check_validity(self, size: int, puzzle: list[list[int]]):
        # generate puzzle control template
        puzzle_control = [False for i in range(size ** 2)]

        # check that no number is repeated or too big
        for row in puzzle:
            for nb in row:
                if nb < 0 or nb >= size ** 2:
                    e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                                  f"file format error: number too big: {nb}")
                elif puzzle_control[nb] == True:
                    e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                                  f"file format error: number repeated: {nb}")
                puzzle_control[nb] = True

        # check that no number is missing
        if False in puzzle_control:
            e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                          f"file format error: at least one of 0..{size ** 2 - 1} number is missing")

    def parse(self):
        content: list[str] = []

        if self.args.file:
            content = self.__get_file_content()
        elif self.args.input:
            content = self.__get_input()

        numbers: list[int] = []
        for line in content:
            for item in line.split('#')[0].split(" "):
                item = item.removesuffix("\n")
                if item:
                    r = re.search(Parser.OTHER_THAN_SPACE_DIGITS_PATTERN, item)
                    if r:
                        e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                                      f"file format error: forbidden char: '{line}'")
                    numbers.append(int(item))

        if not numbers:
            e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                          f"File doesn't contains any number.")

        size = numbers.pop(0)

        if size < 2:
            e.Error.throw(e.Error.FAIL, e.Error.FILE_FORMAT_ERROR,
                          f"file format error: minimum size is 2, found {size}")

        print(size, numbers)

        # self.__check_validity(size, puzzle)

        e.Error.print_error("")
