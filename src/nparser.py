import re

from src.error import Error
from src.puzzle import Puzzle


class Parser:
    def __init__(self, args):
        self.args = args

    def __get_file_content(self):
        lines: list[str] = []

        try:
            f = open(self.args.file, 'r')
            lines = f.readlines()
        except FileNotFoundError:
            Error.throw(Error.FAIL, Error.FILE_NOT_FOUND_ERROR,
                        f"no such file: {self.args.file}")
        except IsADirectoryError:
            Error.throw(Error.FAIL, Error.IS_A_DIRECTORY_ERROR,
                        f"is a directory: {self.args.file}")
        except PermissionError:
            Error.throw(Error.FAIL, Error.PERMISSION_ERROR,
                        f"permission denied: {self.args.file}")
        except UnicodeDecodeError:
            Error.throw(Error.FAIL, Error.UNICODE_DECODE_ERROR,
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
                Error.throw(Error.FAIL, Error.UNICODE_DECODE_ERROR,
                            f"'utf-8' codec can't decode byte")
            except KeyboardInterrupt:
                Error.throw(Error.FAIL, Error.KEYBOARD_INTERRUPT_ERROR,
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
                    Error.throw(Error.FAIL, Error.FILE_FORMAT_ERROR,
                                f"file format error: number too big: {nb}")
                elif puzzle_control[nb] == True:
                    Error.throw(Error.FAIL, Error.FILE_FORMAT_ERROR,
                                f"file format error: number repeated: {nb}")
                puzzle_control[nb] = True

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
                    r = re.search("[^\\d]", item)
                    if r:
                        Error.throw(Error.FAIL, Error.FILE_FORMAT_ERROR,
                                    f"file format error: forbidden char: '{item}'")
                    numbers.append(int(item))

        if not numbers:
            Error.throw(Error.FAIL, Error.FILE_FORMAT_ERROR,
                        f"File doesn't contains any number.")

        size = numbers.pop(0)

        if size < 2:
            Error.throw(Error.FAIL, Error.FILE_FORMAT_ERROR,
                        f"file format error: minimum size is 2, found {size}")

        if len(numbers) is not size ** 2:
            Error.throw(Error.FAIL, Error.FILE_FORMAT_ERROR,
                        f"file format error: size is {size}, {size ** 2} numbers should have been provided, found {len(numbers)}")

        # Convert the numbers list into a grid
        grid = [numbers[i * size:(i + 1) * size] for i in range(size)]
        self.__check_validity(size, grid)
        return Puzzle(size, grid)
