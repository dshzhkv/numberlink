import argparse

from Instance import Instance
from Structures import Field
import math


class InputHandler:
    def get_field(self, file_name, is_hexagonal):
        if is_hexagonal:
            return self.get_hexagonal_field(file_name)
        return self.get_rectangle_field(file_name)

    def get_hexagonal_field(self, file_name):
        with open(file_name) as file:
            line = file.readline().split()

            self.check_line(line)
            self.check_params_hexagon(line)

            height = int(line[0])

            field = []

            max_width = 2 + math.floor(height / 2)

            self.get_field_half(math.ceil(height / 2), file, 2, 1, field)
            self.get_field_half(math.ceil(height / 2) - 1, file, max_width - 1,
                                -1, field)

            self.check_height(field, height)
            return Field((max_width, height), field)

    def get_field_half(self, num_of_lines, file, width, delta, field):
        for i in range(num_of_lines):
            line = file.readline().split()
            self.check_line_width(line, width)
            width += delta
            field.append(line)

    @staticmethod
    def check_params_hexagon(line):
        if len(line) > 1 or int(line[0]) <= 0:
            raise ValueError('В первой строке должно быть одно положительное '
                             'целое число - высота 6-угольного поля')

    def get_rectangle_field(self, file_name):
        with open(file_name) as file:
            line = file.readline().split()

            self.check_line(line)
            self.check_params_rectangle(line)

            width, height = map(int, line)

            field = []
            for line in file:
                line = line.split()
                self.check_line(line)
                self.check_line_width(line, width)
                field.append(line)

            self.check_height(field, height)
            return Field((width, height), field)

    @staticmethod
    def check_params_rectangle(line):
        if len(line) < 2 or int(line[0]) <= 0 or int(line[1]) <= 0:
            raise ValueError('В первой строке должно быть два положительных '
                             'целых числа - ширина и высота поля через пробел')

    @staticmethod
    def check_line(line):
        if not line:
            raise ValueError('Пустая строка')

    @staticmethod
    def check_line_width(line, width):
        if len(line) > width:
            raise ValueError("Количество символов в строке больше заявленной "
                             "ширины поля")
        if len(line) < width:
            raise ValueError("Количество символов в строке меньше заявленной "
                             "ширины поля")

    @staticmethod
    def check_height(field, height):
        if len(field) < height:
            raise ValueError("Количество строк меньше заявленной высоты поля")
        if len(field) > height:
            raise ValueError("Количество строк больше заявленной высоты поля")

    @staticmethod
    def get_data():
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--hexagonal', help='6-угольное поле',
                            action='store_true', default=False)
        parser.add_argument("file_name",
                            help="имя или путь к файлу, в котором первая "
                                 "строка содержит два числа через пробел: "
                                 "ширину и высоту поля, каждая следующая j-я "
                                 "строка (j не превышает высоты поля) "
                                 "содержит i элементов поля через пробел (i = "
                                 "ширине поля). # - пустая клетка. можно "
                                 "использовать любой из примеров в "
                                 "examples/(номер от 1 до 6).txt",
                            type=str)
        args = parser.parse_args()
        return args.hexagonal, args.file_name


class OutputHandler:
    def __init__(self, field, is_hexagonal):
        self.field = field
        self.is_hexagonal = is_hexagonal

    def show_solutions(self, solutions):
        any_solutions = False
        for i, solution in enumerate(solutions):
            any_solutions = True
            print('Решение {}'.format(i + 1))
            if self.is_hexagonal:
                self.print_solution_hex(solution)
            else:
                self.print_solution(solution)
        if not any_solutions:
            print('Нет решений')

    def print_solution(self, solution):
        result = []
        for i in range(self.field.height):
            line = []
            next_line = []
            for j in range(self.field.width):
                line.append(self.field.field[i][j])
                if [(i, j), (i, j + 1)] in solution:
                    line.append('--')
                else:
                    line.append(' ' * 2)

                if [(i, j), (i + 1, j)] in solution:
                    next_line.append('|' + ' ' * 2)
                else:
                    next_line.append(' ' * 3)
            result.append(line)
            result.append(next_line)
        for i in range(len(result)):
            print(''.join(result[i]))

    def print_solution_hex(self, solution):
        result = []

        passed_middle = False
        for i in range(self.field.height):
            width = len(self.field.field[i])

            if not passed_middle:
                passed_middle = (width == self.field.width)

            line = []
            next_line = []

            line.append(' ' * 2 * (self.field.width - width))
            next_line.append(' ' * 2 * (self.field.width - width))
            for j in range(width):

                line.append(self.field.field[i][j])
                if [(i, j), (i, j + 1)] in solution:
                    line.append('--')
                else:
                    line.append(' ' * 2)

                if not passed_middle:
                    if [(i, j), (i + 1, j)] in solution:
                        next_line.append('/' + ' ' * 2)
                    elif [(i, j), (i + 1, j + 1)] in solution:
                        next_line.append('\\' + ' ' * 2)
                    else:
                        next_line.append(' ' * 3)

                else:
                    if [(i, j), (i + 1, j)] in solution:
                        next_line.append('\\' + ' ' * 2)
                    elif [(i, j), (i + 1, j - 1)] in solution:
                        next_line.append('/' + ' ' * 2)
                    else:
                        next_line.append(' ' * 3)

            result.append(line)
            result.append(next_line)
        for i in range(len(result)):
            print(''.join(result[i]))


class CUI:
    def __init__(self):
        self.input_handler = InputHandler()
        self.output_handler = None

    def get_instance(self):
        # is_hexagonal, file_name = self.input_handler.get_data()
        is_hexagonal, file_name = True, 'examples/1_h.txt'
        field = self.input_handler.get_field(file_name, is_hexagonal)
        self.output_handler = OutputHandler(field, is_hexagonal)
        return Instance(field, is_hexagonal)

    def show_solutions(self, solutions):
        self.output_handler.show_solutions(solutions)
