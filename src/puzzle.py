import math


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
