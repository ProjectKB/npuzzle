from __future__ import annotations

import math
import time
import sys

from src.puzzle import Puzzle
from src.utils import get_field_size

OKGREEN: str = '\033[92m'
OKBLUE: str = '\033[94m'
OKCYAN = '\033[96m'


def vs(puzzle: Puzzle, goal: list[int], end: Puzzle):
    skip: bool = False
    size: int = puzzle.size
    current: Puzzle = puzzle
    g: int = end.g

    print("\tYou wanna try to beat our algo? Good luck...\n")

    while 42:
        if current.grid == goal:
            __vs_print(current, [choice], field_size, OKGREEN)
            __print_end(g)
            return

        if not skip:
            children = current.create_children()
            field_size: int = get_field_size(size)
            pos_values: list[int] = []
            for child in children:
                diff = [1 if p == m else 0 for p, m in zip(current.grid, child.grid)]
                diff_index = [i for i, d in enumerate(diff) if d == 0]
                nb = current.grid[diff_index[0]] if current.grid[diff_index[0]] != 0 else current.grid[diff_index[1]]
                pos_values.append(nb)
            zero: int = current.grid.index(0)
            p: dict = __associate_key(pos_values, zero, current.grid, size)

        __vs_print(current, pos_values, field_size, OKGREEN)
        user_input = __handle_input(g, list(p.keys()))
        __remove_lines(7 + size)

        if user_input in p.keys():
            g -= 1
            skip = False
            choice: int = pos_values[p[user_input]]

            __print_board_and_remove(current, choice, field_size, OKCYAN, size, g, list(p.keys()))
            current = children[p[user_input]]
            __print_board_and_remove(current, choice, field_size, OKBLUE, size, g, list(p.keys()))
        else:
            skip = True


def __print_end(g: int):
    if g < 0:
        print("\n\tOoooooooooh too bad... Noob!\n")
    elif g == 0:
        print("\n\tIt was... Almost good!\n")
    else:
        print("\n\tBeginner's luck...\n")


def __get_keys(keys: list[str]):
    possible_move = []
    for key in keys:
        match key:
            case 'w': possible_move.append(f'up: {key}')
            case 's': possible_move.append(f'down: {key}')
            case 'd': possible_move.append(f'left: {key}')
            case 'a': possible_move.append(f'right: {key}')
    return ' | '.join(possible_move)


def __handle_input(g: int, keys: list[str]) -> str | None:
    try:
        print(f"\n\tRemaining blows: {g}")
        print(f"\n\t{__get_keys(keys)}\n")
        return input("\t> ")
    except EOFError:
        print("\n\n\tNext time maybe...\n")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n\n\tNext time maybe...\n")
        sys.exit(0)


def __print_board_and_remove(current: Puzzle, choice: int, field_size: int, color: str, size: int, g: int, keys: list[str]):
    __vs_print(current, [choice], field_size, color)
    print(f"\n\tRemaining blows: {g}")
    print(f"\n\t{__get_keys(keys)}\n")
    time.sleep(0.5)
    __remove_lines(6 + size)


def __remove_lines(size: int):
    for i in range(0, size):
        print("\033[1A\x1b[2K", end='')


def __associate_key(pos_values: list[int], zero: int, grid: list[int], size: int) -> dict:
    grid: list[list[int]] = [grid[i * size:i * size + size] for i in range(0, size)]
    grid: list[list[int]] = [[-1, *row, -1] for row in grid]
    grid: list[list[int]] = [[-1] * (size + 2), *grid, [-1] * (size + 2)]

    zy: int = math.floor(zero / size) + 1
    zx: int = math.floor(zero % size) + 1
    match len(pos_values):
        case 3:
            if grid[zy - 1][zx] in pos_values and grid[zy][zx - 1] in pos_values and grid[zy + 1][zx] in pos_values:
                p = {'s': pos_values.index(grid[zy - 1][zx]), 'd': pos_values.index(grid[zy][zx - 1]),
                     'w': pos_values.index(grid[zy + 1][zx])}
            elif grid[zy][zx - 1] in pos_values and grid[zy][zx + 1] in pos_values and grid[zy + 1][zx] in pos_values:
                p = {'d': pos_values.index(grid[zy][zx - 1]), 'a': pos_values.index(grid[zy][zx + 1]),
                     'w': pos_values.index(grid[zy + 1][zx])}
            elif grid[zy - 1][zx] in pos_values and grid[zy][zx + 1] in pos_values and grid[zy + 1][zx] in pos_values:
                p = {'s': pos_values.index(grid[zy - 1][zx]), 'a': pos_values.index(grid[zy][zx + 1]),
                     'w': pos_values.index(grid[zy + 1][zx])}
            elif grid[zy - 1][zx] in pos_values and grid[zy][zx - 1] in pos_values and grid[zy][zx + 1] in pos_values:
                p = {'s': pos_values.index(grid[zy - 1][zx]), 'd': pos_values.index(grid[zy][zx - 1]),
                     'a': pos_values.index(grid[zy][zx + 1])}
        case 2:
            if grid[zy][zx + 1] in pos_values and grid[zy + 1][zx] in pos_values:
                p = {'a': pos_values.index(grid[zy][zx + 1]), 'w': pos_values.index(grid[zy + 1][zx])}
            elif grid[zy][zx - 1] in pos_values and grid[zy + 1][zx] in pos_values:
                p = {'d': pos_values.index(grid[zy][zx - 1]), 'w': pos_values.index(grid[zy + 1][zx])}
            elif grid[zy - 1][zx] in pos_values and grid[zy][zx + 1] in pos_values:
                p = {'s': pos_values.index(grid[zy - 1][zx]), 'a': pos_values.index(grid[zy][zx + 1])}
            elif grid[zy - 1][zx] in pos_values and grid[zy][zx - 1] in pos_values:
                p = {'s': pos_values.index(grid[zy - 1][zx]), 'd': pos_values.index(grid[zy][zx - 1])}
        case 4:
            p = {'s': pos_values.index(grid[zy - 1][zx]), 'd': pos_values.index(grid[zy][zx - 1]),
                 'a': pos_values.index(grid[zy][zx + 1]), 'w': pos_values.index(grid[zy + 1][zx])}
    return p


def __vs_print(current: Puzzle, pos_values: list[int], field_size: int, color: str):
    size: int = current.size

    print("\n", end="\t")
    for i in range(0, size ** 2):
        if current.grid[i] in pos_values:
            print(f"{color}{current.grid[i]:>{field_size}}\033[0m", end=' ')
        else:
            print(f"{current.grid[i]:>{field_size}}", end=' ')
        if not (i + 1) % size:
            print("\n", end="\t")
