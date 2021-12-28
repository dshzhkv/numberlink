import unittest
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


if __name__ == '__main__':
    unittest.main()
