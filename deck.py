from functools import total_ordering


@total_ordering
class Deck:
    """Двунаправленная очередь.

    Упорядоченная последовательность заданного размера с возможностью
    добавления и удаления элементов в начале и в конце последовательности.

    Attributes:
        __array (list): Python-list заданного размера.
        __head (int): Указатель на начало последовательности.
        __tail (int): Указатель на первое пустое место в последовательности.
        __size (int): Размер выделенного массива.
        __empty (int): Количество пустых мест в последовательности.

    Examples:
        >>> deck = Deck(5)
        >>> deck
        Deck: size=5, fullness=0
    """
    def __init__(self, __size):
        self.__array = [None] * __size
        self.__empty = __size
        self.__head = 0
        self.__tail = 0
        self.__size = __size
        self.__empty = __size

    def __str__(self):
        """
        Examples:
        >>> deck = Deck(5)
        >>> str(deck)
        '[None, ..., None]'
        """
        return (
            f"[{self.__array[self.__head]}, ..., "
            f"{self.__array[self.__tail - 1]}]"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}: "
            f"size={self.__size}, fullness={len(self)}"
        )

    def __len__(self):
        """Показывает количество заполненных ячеек.

        Examples:
        >>> deck = Deck(5)
        >>> len(deck)
        0
        >>> deck.push_back(9)
        >>> len(deck)
        1
        """
        return self.__size - self.__empty

    def __eq__(self, __o):
        """
        Examples:
        >>> deck_1 = Deck(5)
        >>> deck_1 == 5
        False
        >>> deck_2 = Deck(5)
        >>> deck_1 == deck_2
        True
        >>> deck_1.push_back(9)
        >>> deck_1 == deck_2
        False
        """
        if not isinstance(__o, Deck):
            return False
        if self.__size != __o.__size:
            return False
        return len(self) == len(__o)

    def __lt__(self, __o):
        """
        Examples:
        >>> deck_1 = Deck(5)
        >>> deck_2 = Deck(5)
        >>> deck_1 < deck_2
        False
        >>> deck_1.push_back(9)
        >>> deck_2 < deck_1
        True
        >>> deck_3 = Deck(6)
        >>> deck_1 < deck_3
        True
        """
        if not isinstance(__o, Deck):
            raise TypeError(
                "Supports between instances of "
                f"'{self.__class__.__name__}' only"
            )
        if self.__size < __o.__size:
            return True
        return len(self) < len(__o)

    def size(self):
        """
        Examples:
        >>> deck = Deck(5)
        >>> deck.size()
        5
        >>> deck.push_back(9)
        >>> deck.size()
        5
        """
        return self.__size

    def clear(self):
        """Очищает последовательность.

        Examples:
        >>> deck = Deck(5)
        >>> deck.push_back(9)
        >>> deck.clear()
        >>> deck
        Deck: size=5, fullness=0
        """
        __size = len(self.__array)
        self.__array = [None] * __size
        self.__empty = __size
        self.__head = 0
        self.__tail = 0

    def push_back(self, value):
        """Добавляет элемент в конец последовательности.

        Args:
            value (obj): Объект, который необходимо добавить.

        Returns:
            str: `error`, если последовательность заполнена.

        Examples:
        >>> deck = Deck(5)
        >>> deck.push_back(4)
        >>> deck.push_back(9)
        >>> deck
        Deck: size=5, fullness=2
        >>> str(deck)
        '[4, ..., 9]'

        """
        if not self.__empty:
            return 'error'
        self.__array[self.__tail] = value
        self.__empty -= 1
        self.__tail += 1
        if self.__tail == len(self.__array):
            self.__tail = 0

    def push_front(self, value):
        """Добавляет элемент в начало последовательности.

        Args:
            value (obj): Объект, который необходимо добавить.

        Returns:
            str: `error`, если последовательность заполнена.
        Examples:
        >>> deck = Deck(5)
        >>> deck.push_front(4)
        >>> deck.push_front(9)
        >>> deck
        Deck: size=5, fullness=2
        >>> str(deck)
        '[9, ..., 4]'
        """
        if not self.__empty:
            return 'error'
        self.__head -= 1
        if self.__head < 0:
            self.__head = len(self.__array) - 1
        self.__array[self.__head] = value
        self.__empty -= 1

    def pop_back(self):
        """Удаляет и возвращает элемент в конце последовательности.

        Returns:
            str: `error`, если последовательность пустая.
            value (obj): Удалённый из последовательности объект.

        Examples:
        >>> deck = Deck(5)
        >>> deck.push_back(4)
        >>> deck.push_back(9)
        >>> deck.pop_back()
        9
        >>> deck
        Deck: size=5, fullness=1
        """
        if self.__empty == len(self.__array):
            return 'error'
        self.__tail -= 1
        if self.__tail < 0:
            self.__tail = len(self.__array) - 1
        value = self.__array[self.__tail]
        self.__array[self.__tail] = None
        self.__empty += 1
        return value

    def pop_front(self):
        """Удаляет и возвращает элемент в начале последовательности.

        Returns:
            str: `error`, если последовательность пустая.
            value (obj): Удалённый из последовательности объект.

        Examples:
        >>> deck = Deck(5)
        >>> deck.push_back(4)
        >>> deck.push_back(9)
        >>> deck.pop_front()
        4
        >>> deck
        Deck: size=5, fullness=1
        """
        if self.__empty == len(self.__array):
            return 'error'
        value = self.__array[self.__head]
        self.__array[self.__head] = None
        self.__empty += 1
        self.__head += 1
        if self.__head == len(self.__array):
            self.__head = 0
        return value

    def get_back(self):
        """Возвращает последний элемет последовательности.

        Returns:
            str: `error`, если последовательность пустая.
            value (obj): Запрошенный элемент.

        Examples:
        >>> deck = Deck(5)
        >>> deck.push_back(4)
        >>> deck.push_back(9)
        >>> deck.get_back()
        9
        >>> deck
        Deck: size=5, fullness=2
        """
        if self.__empty == len(self.__array):
            return 'error'
        value = self.__array[self.__tail - 1]
        return value

    def get_front(self):
        """Возвращает первый элемет последовательности.

        Returns:
            str: `error`, если последовательность пустая.
            value (obj): Запрошенный элемент.

        Examples:
        >>> deck = Deck(5)
        >>> deck.push_back(4)
        >>> deck.push_back(9)
        >>> deck.get_front()
        4
        >>> deck
        Deck: size=5, fullness=2
        """
        if self.__empty == len(self.__array):
            return 'error'
        value = self.__array[self.__head]
        return value


def main():
    results = []
    commands = int(input())
    deck_size = int(input())
    deck = Deck(deck_size)
    for _ in range(commands):
        command, *args = input().split()
        attr = getattr(deck, command)
        if attr:
            result = attr(*args)
        if result is not None:
            results.append(result)

    results = '\n'.join(results)
    print(results)


if __name__ == '__main__':
    main()
