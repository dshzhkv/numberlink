import unittest

from Application.Instance import Instance
from Application.Solver import Solver
from UI.CUI import InputHandler, OutputHandler


class TestFieldParser(unittest.TestCase):

    input_handler = InputHandler()

    def test_params_error_hexagonal(self):
        context = self.setup_test('3 3', '1 2', '# # #', '1 2',
                                  is_hexagonal=True)

        self.assertTrue('В первой строке должно быть одно положительное '
                        'целое число - высота 6-угольного поля' in
                        str(context.exception))

    def test_params_error_rectangle(self):
        context = self.setup_test('2', '1 2', '1 2')

        self.assertTrue('В первой строке должно быть два положительных '
                        'целых числа - ширина и высота поля через пробел' in
                        str(context.exception))

    def test_width_error_long_hexagonal(self):
        context = self.setup_test('3', '1 2', '# # # #', '1 2',
                                  is_hexagonal=True)

        self.assertTrue("Количество символов в строке больше заявленной "
                        "ширины поля" in str(context.exception))

    def test_width_error_small_hexagonal(self):
        context = self.setup_test('3', '1 2', '# #', '1 2',
                                  is_hexagonal=True)

        self.assertTrue("Количество символов в строке меньше заявленной "
                        "ширины поля" in str(context.exception))

    def test_width_error_long_rectangle(self):
        context = self.setup_test('2 2', '1 2', '1 2 #')

        self.assertTrue("Количество символов в строке больше заявленной "
                        "ширины поля" in str(context.exception))

    def test_width_error_small_rectangle(self):
        context = self.setup_test('2 2', '1 2', '1')

        self.assertTrue("Количество символов в строке меньше заявленной "
                        "ширины поля" in str(context.exception))

    def setup_file(self, *lines):
        with open('test_file.txt', 'w') as test_file:
            self.write_to_file(test_file, *lines)

    def setup_test(self, *lines, is_hexagonal=False):
        self.setup_file(*lines)

        with self.assertRaises(Exception) as context:
            self.input_handler.get_field('test_file.txt', is_hexagonal)

        return context

    @staticmethod
    def write_to_file(test_file, *lines):
        for line in lines:
            test_file.write(line + '\n')


class TestOutput(unittest.TestCase):
    def test_output_hexagonal(self):
        field = InputHandler().get_field('../examples/3_h.txt', True)
        output_handler = OutputHandler(field, True)
        solution = output_handler.get_solution(list(Solver(
            Instance(field, True)).solve())[0])

        def space(length):
            return ' ' * length

        right = '  \\ '
        left = '/   '
        horizontal = '---'
        expected_output = [
            [space(6), '1', space(3), '2', space(3)],
            [space(5), right, right],
            [space(4), '4', space(3), '#', space(3), '#', space(3)],
            [space(3), right, right, right],
            [space(2), '5', space(3), '#', space(3), '#', space(3), '#', space(3)],
            [space(1), right, right, right, right],
            [space(0), '3', space(3), '5', space(3), '4', space(3), '#', space(3), '#', space(3)],
            [space(1), '\\ ', space(4), space(4), left, left],
            [space(2), '#', horizontal, '3', space(3), '#', space(3), '#', space(3)],
            [space(3), space(2), space(4), left, left],
            [space(4), '#', horizontal, '#', space(3), '#', space(3)],
            [space(5), '\\ ', space(4), left],
            [space(6), '1', space(3), '2', space(3)]]

        self.assertEqual(expected_output, solution)

    def test_output_rectangle(self):
        field = InputHandler().get_field('../examples/6.txt', False)
        output_handler = OutputHandler(field, False)
        solution = output_handler.get_solution(list(Solver(
            Instance(field, False)).solve())[0])

        def space(length):
            return ' ' * length

        vertical = '|   '
        horizontal = '---'

        expected_output = [['2', space(3), '1', horizontal, '#', space(3)],
                           [vertical, space(4), vertical],
                           ['#', horizontal, '2', space(3), '1', space(3)],
                           [space(4), space(4), space(4)],
                           ['3', horizontal, '#', horizontal, '3', space(3)]]

        self.assertEqual(expected_output, solution)


if __name__ == '__main__':
    unittest.main()
