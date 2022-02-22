class Stack:
    """Реализация методов стека на основе списка.
    """
    def __init__(self):
        self.__array = []

    def __len__(self) -> int:
        return len(self.__array) 
    
    def add(self, value):
        """Добавляет переданный объект в стек.
        
        Args:
            value (obj): Объект, который необходимо добавить.
        """
        self.__array.append(value)

    def last(self):
        """Возвращает последний элемент стека.

        Returns:
            None: Если в стеке нет элементов.
            obj: Запрошенный из стека элемент.
        """
        if not self.__array:
            return None
        return self.__array[-1]
    
    def pop(self):
        """Удаляет и возвращает последний элемент стека.

        Returns:
            None: Если в стеке нет элементов.
            obj: Удалённый из стека элемент.
        """
        if not self.__array:
            return None
        return self.__array.pop()

    def get_operands(self, amount=2):
        """Возвращает требуемое количество элементов с конца списка.

        По умолчанию возвращает два значения использующихся
        в большинстве простых арифметических операций.

        Args:
            amount (int): Количество требуемых значений.

        Returns:
            operands (list): Список из требуемых значений.

        Raises:
            ValueError:
                Запрошено не натуральное число.
            IndexError:
                Запрошено количество больше, чем имеется элементов в списке.
        """
        if amount < 1:
            raise ValueError(
                "Значение `amount` должно быть натуральным числом."
            )
        if amount > len(self.__array):
            raise IndexError(
                "Значение `amount` больше, чем элементов в стеке."
            )
        operands = self.__array[-amount:]
        del self.__array[-amount:]
        return operands


class Calculator:
    """Класс с арифметическими методами.
    """
    @staticmethod
    def action(symbol, operands) -> int:
        """Вызывает необходимые вычислительные методы.

        Args:
            symbol (str): Символ математичнского действия.
                operands (sequence): Числа, с которыми необходимо
                произвести математическое действие.

        Returns:
            int: Результат вычислений.
        
        Raises:
            ValueError:
                Передано неверное количество чисел.
            AttributeError:
                Неподдерживаемое математическое действие.
        
        Examples:
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

    def __addition(a, b) -> int:
        return a + b

    def __subtraction(a, b) -> int:
        return a - b

    def __multiplication(a, b) -> int:
        return a * b

    def __division(a, b) -> int:
        return a // b


class PolishCalculator(Calculator):
    """Калькулятор, считающий по правилам польской нотации.

    Examples:
        >>> - * 5 8 3
        37
    """
    def __init__(self) -> None:
        self._numbers = Stack()

    def _get_operands(self, amount=2):
        return self._numbers.get_operands(amount)

    @staticmethod
    def _normal_string(string):
        """Нормализует введённую строку.
        
        Args:
            string (str): Строка с входными данными.
        
        Returns:
            str: Нормализованная строка.
        """
        return reversed(string)

    @staticmethod
    def string_to_digit(value):
        """Переводит переданное значение в int.
        """
        if value[-1].isdecimal():
            return int(value)
        return False

    def get_result(self, data) -> int:
        """Производит вычисления согласно введённой строки.

        Args:
            data (str): Строка с числами и операторами.

        Returns:
            int: Вычисленное значение.
        """
        data = self._normal_string(data)
        for value in data:
            number = self.string_to_digit(value)
            if not number is False:
                self._numbers.add(number)
                continue
            operands = self._get_operands(2)
            result = self.action(value, operands)
            self._numbers.add(result)

        return self._numbers.last()


class ReversePolishCalculator(PolishCalculator):
    """Калькулятор, считающий по правилам обратной польской нотации.

    Examples:
        >>> 7 2 + 4 * 2 +
        38
    """
    @staticmethod
    def _normal_string(string):
        return string


def test():
    calculator = ReversePolishCalculator()
    data = input().split()
    result = calculator.get_result(data)
    print(result)


if __name__ == '__main__':
    test()
