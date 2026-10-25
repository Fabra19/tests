import unittest
from .app import *


class TestInputCalculator(unittest.TestCase):
    def test_input_available(self):
        obj = Calculator()
        try:
            obj.input('2 + 2')
        except AttributeError:
            self.fail('Функция input не доступна.')

    def test_correct(self):
        obj = Calculator()
        self.assertEqual(obj.input('2 + 2'), (2, '+', 2))
        self.assertEqual(obj.input('-2 - 2'), (-2, '-', 2))
        self.assertEqual(obj.input('2 * -2'), (2, '*', -2))
        self.assertEqual(obj.input('-2 / -2'), (-2, '/', -2))


    def test_incorrect(self):
        obj = Calculator()
        with self.assertRaises(TypeError):
            obj.input(True)
        with self.assertRaises(ValueError):
            obj.input('2+2')
        with self.assertRaises(ValueError):
            obj.input('2+ 2')
        with self.assertRaises(ValueError):
            obj.input('-2 +2')
        with self.assertRaises(ValueError):
            obj.input('2 + 2 - 3')
        with self.assertRaises(ValueError):
            obj.input('2 + True')
        with self.assertRaises(ValueError):
            obj.input('2 + =')
        with self.assertRaises(ValueError):
            obj.input('2 + 2.65')
        with self.assertRaises(ValueError):
            obj.input('2 2 2')
        with self.assertRaises(ValueError):
            obj.input('2 +- 2')
        with self.assertRaises(ZeroDivisionError):
            obj.input('2 / 0')



class TestExecute(unittest.TestCase):
    def test_execute_available(self):
        obj = Calculator()
        try:
            obj.execute('2 + 2')
        except AttributeError:
            self.fail('Функция execute не доступна.')

    def test_execute_correct(self):
        obj = Calculator()
        self.assertEqual(obj.execute('3 + 6'), 9)
        self.assertEqual(obj.execute('-3 - 6'), -9)
        self.assertEqual(obj.execute('3 * -6'), -18)
        self.assertEqual(obj.execute('-3 / -6'), 0.5)


if __name__ == '__main__':
    unittest.main()
