import math


class Puzzle:
    size: int
    grid: list[list[int]]

    def __init__(self, size: int, grid: list[list[int]]):
        self.size = size
        self.grid = grid

    def __str__(self):
        max_len = len(str(self.size ** 2))
        output = f"{self.size}\n > "
        output += "\n > ".join([" ".join([str(item).rjust(max_len)
                                          for item in line]) for line in self.grid])
        return output

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
