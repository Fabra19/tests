class Calculator:
    def __init__(self):
        pass

    def input(self, expression: str):
        if not isinstance(expression, str):
            raise TypeError('Выражение должно быть строкой')
        data = expression.split()
        if len(data) != 3:
            raise ValueError('Выражение не корректно')
        num1 = data[0]
        num2 = data[2]
        if num1.startswith('-'):
            num1 = num1[1:]
        if num2.startswith('-'):
            num2 = num2[1:]
        if not num1.isdigit() or not num2.isdigit():
            raise ValueError('Выражение не корректно')
        if data[1] not in '+-/*' or len(data[1]) != 1:
            raise ValueError('Неправильный знак')
        if num2 == '0' and data[1] == '/':
            raise ZeroDivisionError('На ноль делить нельзя')

        return int(data[0]), data[1], int(data[2])

    def execute(self, expression: str):
        data: tuple[int, str, int] = self.input(expression)
        if data[1] == '+':
            return data[0] + data[2]
        elif data[1] == '-':
            return data[0] - data[2]
        elif data[1] == '*':
            return data[0] * data[2]
        elif data[1] == '/':
            return data[0] / data[2]
        else:
            return 'Проверьте знак.'
