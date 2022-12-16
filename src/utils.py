import math


def generate_control(size: int) -> list[list[int]]:
    control = [[0 for _ in range(size)] for _ in range(size)]
    center = {'y': math.floor(size / 2), 'x': math.floor(size / 2)} if math.floor(size % 2) else {
        'y': math.floor(size / 2), 'x': math.floor(size / 2) - 1}

    step = 1
    count_step = 0
    count_sign = 1
    h = size ** 2 - 1
    y = center['y']
    x = center['x']
    x_axis = True
    neg = True if size % 2 else False
    control[y][x] = 0

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
            control[y][x] = h
            h -= 1

        x_axis = not x_axis
        count_step += 1
        count_sign += 1

    return control


def euclidean_distance(point1: float, point2: float) -> float:
    # The Euclidean distance or Euclidean metric is the "ordinary" distance between two points that one would
    # measure with a ruler, and is given by the Pythagorean formula.
    # -> (0,0) (3,4) = 5
    # sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)

    return math.sqrt((point2 - point1) ** 2 + (point2 - point1) ** 2)


def manhattan_distance(point1: float, point2: float) -> float:
    # The Manhattan distance between two points is the sum of the absolute differences of their coordinates.
    # In other words, it is the total distance traveled on a grid to get from one point to the other.
    # -> (0,0) (3,4) = 7
    # |x1 - x2| + |y1 - y2|

    return abs(point1 - point2) + abs(point1 - point2)


def chebyshev_distance(point1: float, point2: float) -> float:
    # The Chebyshev distance between two points is the maximum of the absolute differences of their coordinates.
    # In other words, it is the greatest distance between any two coordinates of the two points.
    # -> (0,0) (3,4) = 4
    # max(x1 - x2, y1 - y2)

    return max(point1 - point2, point1 - point2)
