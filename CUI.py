import argparse

from Instance import Instance
from Structures import Field


class InputHandler:
    @staticmethod
    def get_field(file_name, is_hexagonal):
        with open(file_name) as file:
            width, height = map(int, file.readline().split())
            if width <= 0 or height <= 0:
                raise ValueError("Параметры поля должны быть положительными "
                                 "целыми числами")
            field = []
            for line in file:
                if not line:
                    raise ValueError("Недостаточно строк")
                line = line.split()
                if len(line) > width:
                    raise ValueError("Слишком много символов в строке")
                if len(line) < width:
                    raise ValueError("Недостаточно символов в строке")
                else:
                    field.append(line)
            return Field((width, height), field)

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
                end = [(i, j), (i + 1, j)]
                if end in solution:
                    next_line.append('|' + ' ' * 2)
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
        is_hexagonal, file_name = self.input_handler.get_data()
        field = self.input_handler.get_field(file_name, is_hexagonal)
        self.output_handler = OutputHandler(field, is_hexagonal)
        return Instance(field, is_hexagonal)

    def show_solutions(self, solutions):
        self.output_handler.show_solutions(solutions)
