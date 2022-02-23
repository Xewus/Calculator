from typing import Any, Sequence, Union


class Stack:
    """Реализация методов стека на основе списка.

    Attributes:
        __array: Список, хранящий данные.
    """
    def __init__(self) -> None:
        self.__array: list = []

    def __len__(self) -> int:
        return len(self.__array)

    def add(self, value) -> None:
        """Добавляет переданный объект в стек.

        Args:
            value (obj): Объект, который необходимо добавить.
        """
        self.__array.append(value)

    def last(self) -> Any:
        """Возвращает последний элемент в стеке.

        Raises:
            IndexError: Если стек пустой.

        Returns:
            Any (obj): Последний элемент в стеке.
        """
        if not self.__array:
            raise IndexError("Stack is empty")
        return self.__array[-1]

    def pop(self) -> Any:
        """Удаляет и возвращает последний элемент стека.

        Raises:
            IndexError: Если стек пустой.

        Returns:
            Any (obj): Последний элемент в стеке.
        """
        if not self.__array:
            raise IndexError("Stack is empty")
        return self.__array.pop()

    def clear(self) -> None:
        """Очищает стек."""
        del self.__array[:]

    def get_operands(self, amount: int = 2) -> list:
        """Удаляет и возвращает требуемое количество элементов стека.

        По умолчанию возвращает два значения использующихся
        в большинстве простых арифметических операций.

        Args:
            amount (int, optional): Количество требуемых значений.
            Defaults to 2.

        Raises:
            ValueError:
                Запрошено не натуральное число.
            IndexError:
                Запрошено количество больше, чем имеется элементов в списке.

        Returns:
            operands (list): Список из требуемых значений.
        """
        if amount < 1:
            raise ValueError(
                "Значение `amount` должно быть натуральным числом."
            )
        if amount > len(self.__array):
            raise IndexError(
                "Значение `amount` больше, чем элементов в стеке."
            )
        operands: list = self.__array[-amount:]
        del self.__array[-amount:]
        return operands


class Calculator:
    """Сборник арифметических методов.
    """
    @staticmethod
    def string_to_number(value: str) -> Union[int, bool]:
        """Переводит переданное значение в int.

        Ожидает положительные или отрицательные целые числа.
        Если строка не подходит для перевода в тип int,
        возвращает False.

        Args:
            value (str):  Число в строковом формате.

        Returns:
            int: Если строка прошла проверку.
            False: Если строка не прошла проверку.

        Example:
            >>> Calculator.string_to_number("-9")
            -9
        """
        if value[-1].isdecimal():
            return int(value)
        return False

    @staticmethod
    def action(symbol: str, operands: Sequence[int]) -> int:
        """Вызывает необходимые вычислительные методы.

        Args:
            symbol (str): Символ математичнского действия.
                operands (sequence): Числа, с которыми необходимо
                произвести математическое действие.

        Raises:
            ValueError:
                Передано неверное количество чисел.
                Переданы не целые числа.
            AttributeError:
                Неподдерживаемое математическое действие.

        Returns:
            int: Результат вычислений.

        Example:
            >>> Calculator.action("+", (13, 4))
            17
        """
        if len(operands) != 2:
            raise ValueError(
                "`operands` должно быть последовательностью из двух элементов"
            )

        for operand in operands:
            if not isinstance(operand, int):
                raise ValueError("Переданы не целочисленные значения")

        if symbol == '+':
            return Calculator.__addition(*operands)
        if symbol == '-':
            return Calculator.__subtraction(*operands)
        if symbol == '*':
            return Calculator.__multiplication(*operands)
        if symbol == '/':
            return Calculator.__division(*operands)
        raise AttributeError(f"Не поддерживаемая операция: `{symbol}`")

    @staticmethod
    def __addition(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def __subtraction(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def __multiplication(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def __division(a: int, b: int) -> int:
        return a // b


class PolishCalculator(Calculator):
    """Калькулятор, считающий по правилам польской нотации.

    Attributes:
        _numbers: Стек, хранящий вводимые числа и результаты.
        save_results: Указывает, сохранять ли в стеке итоговый результат.

    Examples:
        >>> - * 5 8 3
        37
    """
    def __init__(self) -> None:
        self._numbers: Stack = Stack()
        self.save_results: bool = False

    def _get_operands(self, amount: int = 2) -> list:
        """Получает неообходимые значения для вычислений.

        Args:
            amount (int, optional): Количество необходимых значений.
            Defaults to 2.

        Returns:
            list: Список с необходимыми значениями.
        """
        return self._numbers.get_operands(amount)

    @staticmethod
    def _normal_string(string: str) -> str:
        """Нормализует введённую строку под правила калькулятора.

        Args:
            string (str): Строка с входными данными.

        Returns:
            str: Нормализованная строка.
        """
        return str(reversed(string))

    def get_result(self, data: str) -> int:
        """Производит вычисления согласно введённой строки.

        Args:
            data (str): Строка с числами и операторами.

        Returns:
            int: Вычисленное значение.
        """
        for value in self._normal_string(data):
            number = self.string_to_number(value)
            if number:
                self._numbers.add(number)
                continue
            operands: list = self._get_operands(2)
            result: int = self.action(value, operands)
            self._numbers.add(result)

        if not self.save_results:
            return self._numbers.pop()
        return self._numbers.last()


class ReversePolishCalculator(PolishCalculator):
    """Калькулятор, считающий по правилам обратной польской нотации.

    Example:
        >>> 7 2 + 4 * 2 +
        38
    """
    @staticmethod
    def _normal_string(string: str) -> str:
        return string


def test():
    calculator = ReversePolishCalculator()
    data = input().split()
    result = calculator.get_result(data)
    print(result)


if __name__ == '__main__':
    test()
