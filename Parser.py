import argparse
import itertools

from Structures import *
from NumberLinkSolver import NumberLinkInstance


class Parser:
    def __init__(self):
        self.field = None

    def parse_file(self):
        # file_name = self.get_file_name().file_name
        file_name = 'examples/4.txt'
        self.field = self.get_field(file_name)
        return NumberLinkInstance(self.field)

    @staticmethod
    def get_field(file_name):
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
    def get_file_name():
        parser = argparse.ArgumentParser()
        parser.add_argument("file_name",
                            help="имя или путь к файлу, в котором первая "
                                 "строка содержит два числа через пробел: "
                                 "ширину и высоту поля, каждая следующая j-я "
                                 "строка (j не превышает высоты поля) "
                                 "содержит i элементов поля через пробел (i = "
                                 "ширине поля). # - пустая клетка. можно "
                                 "использовать любой из примеров в "
                                 "examples/(номер от 1 до 2).txt",
                            type=str)
        return parser.parse_args()

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
