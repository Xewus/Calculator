class Stack:
    """Реализация методов стека на основе списка."""
    def __init__(self) -> None:
        self.array = []
    
    def add(self, value):
        """Добавляет переданный элемент в конец списка."""
        self.array.append(value)

    def last(self):
        """Возвращает последний элемент стека."""
        if not self.array:
            return "Стек пуст"
        return self.array[-1]
    
    def pop(self):
        """Удаляет и возвращает последний элемент стека."""
        if not self.array:
            return "Стек пуст"
        return self.array.pop()
    
    def size(self):
        """Показывает длину стека"""
        return len(self.array)

    def get_operands(self, amount=2):
        """Возвращает требуемое количество элементов с конца списка.
        По умолчанию возвращает два значения использующихся
        в большинстве простых арифметических операций."""
        if amount < 1:
            raise ValueError("Значение `amount` должно быть натуральным числом.")
        if amount > len(self.array):
            raise IndexError("Значение `amount` больше, чем элементов в стеке.")
        operands = tuple(self.array[-amount:])
        del self.array[-amount:]
        return operands


class Calculator:
    """Класс с арифметическими методами."""
    @staticmethod
    def action(symbol, operands):
        if len(operands) != 2:
            raise ValueError(
                "`operands` должно быть последовательностью из двух элементов"
            )
        a, b = operands
        if not isinstance(a, int) and not isinstance(b, int):
            raise ValueError("Переданы не целочисленные значения")
        if symbol == '+':
            return Calculator.addition(a, b)
        if symbol == '-':
            return Calculator.subtraction(a, b)
        if symbol == '*':
            return Calculator.multiplication(a, b)
        if symbol == '/':
            return Calculator.division(a, b)
        raise AttributeError (f"Не поддерживаемая операция: `{symbol}`")

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        return a // b


def string_to_digit(value):
    if value.isdigit():
       return int(value)
    else:
        try:
            value = int(value)
            return value
        except ValueError:
            return False


def input_data():
    data = input().split()
    return data


def main():
    stack = Stack()   
    data = input_data()
    for value in data:
        number = string_to_digit(value)
        if not number is False:
            stack.add(number)
            continue
        operands = stack.get_operands(2)
        result = Calculator.action(value, operands)
        stack.add(result)
        
    print(stack.last())



if __name__ == '__main__':
    main()
