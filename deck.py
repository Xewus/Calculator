class Deck:
    """Двунаправленная очередь.

    Упорядоченная последовательность заданного размера с возможностью
    добавления и удаления элементов в начале и в конце последовательности.

    Attributes:
        __array (list): Python-list заданного размера.
        head (int): Указатель на начало последовательности.
        tail (int): Указатель на первое пустое место в последовательности.
        empty (int): Количество пустых мест в последовательности.
    """
    def __init__(self, size) -> None:
        self.__array = [None] * size
        self.head = 0
        self.tail = 0
        self.empty = size
    
    def push_back(self, value):
        """Добавляет элемент в конец последовательности.
        
        Args:
            value (obj): Объект, который необходимо добавить.

        Returns:
            str: `error`, если последовательность заполнена.
        """
        if not self.empty:
            return 'error'
        self.__array[self.tail] = value
        self.empty -= 1
        self.tail += 1
        if self.tail == len(self.__array):
            self.tail = 0

    def push_front(self, value):
        """Добавляет элемент в начало последовательности.
        
        Args:
            value (obj): Объект, который необходимо добавить.

        Returns:
            str: `error`, если последовательность заполнена.
        """
        if not self.empty:
            return 'error'
        self.head -= 1
        if self.head < 0:
            self.head = len(self.__array) - 1
        self.__array[self.head] = value
        self.empty -= 1
    
    def pop_back(self):
        """Удаляет и возвращает элемент в конце последовательности.
        
        Returns:
            str: `error`, если последовательность пустая.
            value (obj): Удалённый из последовательности объект.
        """
        if self.empty == len(self.__array):
            return 'error'
        self.tail -= 1
        if self.tail < 0:
            self.tail = len(self.__array) - 1
        value = self.__array[self.tail]
        self.__array[self.tail] = None
        self.empty += 1
        return value
    
    def pop_front(self):
        """Удаляет и возвращает элемент в начале последовательности.
        
        Returns:
            str: `error`, если последовательность пустая.
            value (obj): Удалённый из последовательности объект.
        """
        if self.empty == len(self.__array):
            return 'error'
        value = self.__array[self.head]
        self.__array[self.head] = None
        self.empty += 1
        self.head += 1
        if self.head == len(self.__array):
            self.head = 0
        return value

    def get_back(self):
        """Возвращает последний элемет последовательности.

        Returns:
            str: `error`, если последовательность пустая.
            value (obj): Запрошенный элемент.
        """
        if self.empty == len(self.__array):
            return 'error'
        value = self.__array[self.tail - 1]
        return value

    def get_front(self):
        """Возвращает первый элемет последовательности.

        Returns:
            str: `error`, если последовательность пустая.
            value (obj): Запрошенный элемент.
        """
        if self.empty == len(self.__array):
            return 'error'
        value = self.__array[self.head]
        return value

    def clear(self):
        """Очищает последовательность.
        """
        size = len(self.__array)
        for index in range(size):
            self.__array[index] = None
        self.head = 0
        self.tail = 0
        self.empty = size


def input_data():
    commands = []
    amount_commands = int(input())
    deck_size = int(input())
    for _ in range(amount_commands):
        commands.append(input().split())
    return commands, deck_size


def test():
    result = None
    results = []
    commands, deck_size = input_data()
    deck = Deck(deck_size)
    for command, *args in commands:
        attr = getattr(deck, command, None)
        if attr:
            result = attr(*args)
        if not result is None:
            results.append(result)
    
    results = '\n'.join(results)
    print(results)


if __name__ == '__main__':
    test()
