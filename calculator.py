from typing import Any, Sequence, Union


class Stack:
    """Реализация методов стека на основе списка.

    Attributes:
        __array: Список, хранящий данные.

    Examples:
        >>> stack = Stack()
        >>> stack
        Stack: [...]
    """
    def __init__(self) -> None:
        self.__array: list = []

    def __repr__(self) -> str:
        if not self.__array:
            return f"{self.__class__.__name__}: [...]"
        return f"{self.__class__.__name__}: [..., {self.__array[-1]}]"

    def __len__(self) -> int:
        return len(self.__array)

    def add(self, value) -> None:
        """Добавляет переданный объект в стек.

        Args:
            value (obj): Объект, который необходимо добавить.

        Examples:
            >>> stack = Stack()
            >>> stack.add(7)
            >>> stack
            Stack: [..., 7]
        """
        self.__array.append(value)

    def extend(self, __iterable):
        """Добавляет в стек элементы переданной последовательности.

        Args:
            __iterable (_type_): Передаваемая последовательность.

        Examples:
            >>> stack = Stack()
            >>> stack.extend([1, 2, 3])
            >>> stack
            Stack: [..., 3]
        """
        self.__array.extend(__iterable)

    def last(self) -> Any:
        """Возвращает последний элемент в стеке.

        Raises:
            IndexError: Если стек пустой.

        Returns:
            Any (obj): Последний элемент в стеке.

        Examples:
            >>> stack = Stack()
            >>> stack.extend([3, 5, 7])
            >>> stack.last()
            7
            >>> stack
            Stack: [..., 7]
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

        Examples:
            >>> stack = Stack()
            >>> stack.extend([3, 5, 7])
            >>> stack.pop()
            7
            >>> stack
            Stack: [..., 5]
        """
        if not self.__array:
            raise IndexError("Stack is empty")
        return self.__array.pop()

    def clear(self) -> None:
        """Очищает стек.

        Examples:
            >>> stack = Stack()
            >>> stack.extend([3, 5, 7])
            >>> stack.clear()
            >>> stack
            Stack: [...]
        """
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

        Examples:
            >>> stack = Stack()
            >>> stack.extend([1, 3, 5, 7])
            >>> stack.get_operands()
            [5, 7]
            >>> stack.get_operands(1)
            [3]
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
            >>> Calculator.calculation("-", (13, 4))
            9
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
        >>> calculator = PolishCalculator()
        >>> calculator.get_result("- * 5 8 3")
        37
    """
    def __init__(self) -> None:
        self.__numbers: Stack = Stack()

    def _get_operands(self, amount: int = 2) -> list:
        """Получает неообходимые числа для вычислений.

        Args:
            amount (int, optional): Количество необходимых значений.
            Defaults to 2.

        Returns:
            list: Список с числами для вычислений.
        """
        return list(reversed(self.__numbers.get_operands(amount)))

    @staticmethod
    def _normal_input_data(data: Sequence) -> list:
        """Нормализует введённую последовательность под правила калькулятора.

        Args:
            data (Sequnce): Последовательность с входными данными.

        Returns:
            list: Нормализованный список.
        """
        if isinstance(data, (list, tuple)):
            return list(reversed(data))
        if isinstance(data, str):
            return list(reversed(data.split()))
        raise TypeError("На ввод ожидается str/list/tuple")

    def get_result(self, data: str, typ=int) -> Union[int, float, complex]:
        """Производит вычисления согласно введённой строки.

        Ожидает данные в форми строки/списка/кортежа, и проводит вычисления
        согласно переданным данным с требуемым типом чисел.
        По умолчанию использует тип `int`.

        Args:
            data (str): Строка с числами и операторами.
            typ (_type_, optional): Тип чисел для вычислений.
            Defaults to int.

        Returns:
            Union[int, float, complex]: Вычисленное значение.
        """
        for value in self._normal_input_data(data):
            if value[-1].isdecimal():
                self.__numbers.add(typ(value))
                continue
            operands: list = self._get_operands(2)
            result: int = self.calculation(value, operands)
            self.__numbers.add(result)

        return self.__numbers.last()


class ReversePolishCalculator(PolishCalculator):
    """Калькулятор, считающий по правилам обратной польской нотации.

    Example:
        >>> calculator = ReversePolishCalculator()
        >>> calculator.get_result("7 2 + 4 * 2 +")
        38
    """

    @staticmethod
    def _normal_input_data(data: Sequence) -> list:
        if isinstance(data, (list, tuple)):
            return list(data)
        if isinstance(data, str):
            return data.split()
        raise TypeError("На ввод ожидается str/list/tuple")

    def _get_operands(self, amount: int = 2) -> list:
        return list(reversed(super()._get_operands(amount)))


def main():
    calculator = ReversePolishCalculator()
    data = input().split()
    result = calculator.get_result(data)
    print(int(result))


if __name__ == '__main__':
    main()
