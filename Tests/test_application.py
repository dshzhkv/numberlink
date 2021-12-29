import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))

from UI.CUI import InputHandler
from Application.Structures import *
from Application.Instance import Instance
from Application.Solver import Solver


class TestInstanceGeneration(unittest.TestCase):
    def test_no_pair_error(self):
        with self.assertRaises(Exception) as context:
            field = Field((3, 3), [['1', '#', '#'], ['2', '#', '2'],
                                   ['#', '#', '#']])
            instance = Instance(field, False)

        self.assertTrue('У некоторых чисел нет пары :(' in
                        str(context.exception))

    def test_excess_numbers_error(self):
        with self.assertRaises(Exception) as context:
            field = Field((3, 3), [['1', '#', '1'], ['2', '#', '2'],
                                   ['#', '#', '1']])
            instance = Instance(field, False)

        self.assertTrue('На поле не может быть больше двух одинаковых '
                        'чисел' in str(context.exception))


class TestSolver(unittest.TestCase):
    def test_solve_hexagonal(self):
        input_handler = InputHandler()
        field = input_handler.get_field('examples/1_h.txt', True)
        instance = Instance(field, True)
        solver = Solver(instance)
        solutions = list(solver.solve())
        assert len(solutions) > 0

    def test_solve_rectangle(self):
        input_handler = InputHandler()
        field = input_handler.get_field('examples/1.txt', False)
        instance = Instance(field, False)
        solver = Solver(instance)
        solutions = list(solver.solve())
        assert len(solutions) > 0

    def test_no_solutions_hexagonal(self):
        input_handler = InputHandler()
        field = input_handler.get_field('examples/4_h.txt', True)
        instance = Instance(field, True)
        solver = Solver(instance)
        solutions = list(solver.solve())
        assert len(solutions) == 0

    def test_no_solutions_rectangle(self):
        input_handler = InputHandler()
        field = input_handler.get_field('examples/7.txt', False)
        instance = Instance(field, False)
        solver = Solver(instance)
        solutions = list(solver.solve())
        assert len(solutions) == 0


if __name__ == '__main__':
    unittest.main()
