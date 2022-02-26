# id 65491208
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

    Attributes:
        ACTIONS: Словарь с доступными операциями.
    """
    ACTIONS = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
    }

    @staticmethod
    def calculation(
        symbol: str, operands: Sequence[Union[int, float]]
    ) -> Union[int, float]:
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
            >>> Calculator.calculation("+", (13, 4))
            17
        """
        if len(operands) != 2:
            raise ValueError(
                "`operands` должно быть последовательностью из двух элементов"
            )

        for operand in operands:
            if not isinstance(operand, (int, float)):
                raise ValueError("Переданы не числовые значения")

        action = Calculator.ACTIONS.get(symbol)

        if action is None:
            raise AttributeError(f"Не поддерживаемая операция: `{symbol}`")

        return action(*operands)


class PolishCalculator(Calculator):
    """Калькулятор, считающий по правилам польской нотации.

    Attributes:
        __numbers: Стек, хранящий вводимые числа и результаты.

    Examples:
        >>> - * 5 8 3
        37
    """
    def __init__(self) -> None:
        self.__numbers: Stack = Stack()

    def _get_operands(self, amount: int = 2) -> list:
        """Получает неообходимые значения для вычислений.

        Args:
            amount (int, optional): Количество необходимых значений.
            Defaults to 2.

        Returns:
            list: Список с необходимыми значениями.
        """
        return self.__numbers.get_operands(amount)

    @staticmethod
    def _normal_string(string: str) -> str:
        """Нормализует введённую строку под правила калькулятора.

        Args:
            string (str): Строка с входными данными.

        Returns:
            str: Нормализованная строка.
        """
        return str(reversed(string))

    def get_result(self, data: str) -> Union[int, float]:
        """Производит вычисления согласно введённой строки.

        Args:
            data (str): Строка с числами и операторами.

        Returns:
            int: Вычисленное значение.
        """
        for value in self._normal_string(data):
            if value[-1].isdecimal():
                self.__numbers.add(float(value))
                continue
            operands: list = self._get_operands(2)
            result: int = self.calculation(value, operands)
            self.__numbers.add(result)

        return self.__numbers.last()


class ReversePolishCalculator(PolishCalculator):
    """Калькулятор, считающий по правилам обратной польской нотации.

    Example:
        >>> 7 2 + 4 * 2 +
        38
    """
    @staticmethod
    def _normal_string(string: str) -> str:
        return string


def main():
    calculator = ReversePolishCalculator()
    data = input().split()
    result = calculator.get_result(data)
    print(int(result))


if __name__ == '__main__':
    main()
