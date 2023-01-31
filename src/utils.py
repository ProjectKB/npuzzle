import math
import time


def index_to_pos(index: int, size: int) -> tuple[int, int]:
    return index % size, math.floor(index / size)


def pos_to_index(pos: tuple[int, int], size: int) -> int:
    return pos[0] + (pos[1] * size)


def generate_control(size: int) -> list[int]:
    control = [0 for _ in range(size ** 2)]

    step = 1
    count_step = 0
    count_sign = 1
    h = size ** 2 - 1

    x = math.floor(size / 2)
    y = math.floor(size / 2)
    if size % 2 == 0:
        x -= 1

    x_axis = True
    neg = True if size % 2 else False
    control[pos_to_index((x, y), size)] = 0

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
            control[pos_to_index((x, y), size)] = h
            h -= 1

        x_axis = not x_axis
        count_step += 1
        count_sign += 1

    return control


def inverse(size: int, grid: list[int]) -> list[int]:
    goal_dict: list[int] = [0 for _ in range(size ** 2)]
    for i, nb in enumerate(grid):
        goal_dict[nb] = i
    return goal_dict


def euclidean_distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    # The Euclidean distance or Euclidean metric is the "ordinary" distance between two points that one would
    # measure with a ruler, and is given by the Pythagorean formula.
    # -> (0,0) (3,4) = 5
    # sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2)

    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def manhattan_distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    # The Manhattan distance between two points is the sum of the absolute differences of their coordinates.
    # In other words, it is the total distance traveled on a grid to get from one point to the other.
    # -> (0,0) (3,4) = 7
    # |x1 - x2| + |y1 - y2|

    x1, y1 = point1
    x2, y2 = point2

    return abs(x1 - x2) + abs(y1 - y2)


def chebyshev_distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    # The Chebyshev distance between two points is the maximum of the absolute differences of their coordinates.
    # In other words, it is the greatest distance between any two coordinates of the two points.
    # -> (0,0) (3,4) = 4
    # max(x1 - x2, y1 - y2)

    x1, y1 = point1
    x2, y2 = point2

    return max(x1 - x2, y1 - y2)


def get_distance(name: str):
    distance: dict = {
        "manhattan": manhattan_distance,
        "euclidean": euclidean_distance,
        "chebyshev": chebyshev_distance,
    }

    return distance[name]


def print_success(open_list: dict, closed_list: dict, final_puzzle: object, process: bool):
    open_list_len: int = len(open_list)
    closed_list_len: int = len(closed_list)

    __funky_print_states(final_puzzle) if process else __print_states(final_puzzle)

    print(
        f"\n\tSuccess - Open {open_list_len} - Closed {closed_list_len} - G: {final_puzzle.g} - "
        f"OT {closed_list_len} - OS {open_list_len + closed_list_len}\n"
    )


def print_failure():
    print("\n\tThis puzzle is unsolvable\n")


def print_verbose(step: int, open_list: dict, closed_list: dict):
    print(f"Running step {step}, open {len(open_list)}, closed {len(closed_list)}")


def __print_states(puzzle: object):
    if puzzle.parent is not None:
        __print_states(puzzle.parent)
    print(puzzle)


def __remove_lines(size: int):
    for i in range(0, size + 3):
        print("\033[1A\x1b[2K", end='')


def get_field_size(size: int) -> int:
    pow: int = 1
    size: int = size ** 2 - 1
    while size > 10 ** pow:
        pow += 1
    return pow


def __funky_print(grid: list[int], size: int, case: int, field_size: int, data: list[int], color: str, remove: bool = True):
    if remove:
        __remove_lines(size)
    print("\n", end="\t")
    for i in range(0, size ** 2):
        if i == case:
            print(f"{color}{grid[i]:>{field_size}}\033[0m", end=' ')
        else:
            print(f"{grid[i]:>{field_size}}", end=' ')
        if not (i + 1) % size:
            print("\n", end="\t")
    print(f"\n\tF: {data[2]} - H: {data[1]} - G: {data[0]}")
    time.sleep(0.5)


def __funky_print_states(puzzle: object):
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    size: int = puzzle.size
    g: list[int] = []
    h: list[int] = []
    f: list[int] = []
    puzzles: list[object] = []

    end: int = puzzle.g - 1
    field_size: int = get_field_size(size)
    while puzzle is not None:
        g.append(puzzle.g)
        h.append(puzzle.h)
        f.append(puzzle.g + puzzle.h)
        puzzles.append(puzzle.grid)
        puzzle = puzzle.parent
    puzzles = puzzles[::-1]
    data = list(zip(g[::-1], h[::-1], f[::-1]))

    for i, [pick, move] in enumerate(zip(puzzles[:-1], puzzles[1:])):
        diff = [1 if p == m else 0 for p, m in zip(pick, move)]
        diff_index = [i for i, d in enumerate(diff) if d == 0]
        nb = pick[diff_index[0]] if pick[diff_index[0]] != 0 else pick[diff_index[1]]
        __funky_print(pick, size, pick.index(nb), field_size, data[i], OKCYAN, i != 0)
        __funky_print(move, size, move.index(nb), field_size, data[i + 1], OKBLUE if i != end else OKGREEN)
